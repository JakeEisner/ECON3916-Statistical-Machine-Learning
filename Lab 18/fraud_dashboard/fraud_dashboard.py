"""
=============================================================
  Interactive Fraud Detection Threshold Dashboard
  P.R.I.M.E. Expansion — Credit Card Fraud Lab
=============================================================
Run with:
    pip install streamlit scikit-learn matplotlib pandas
    streamlit run fraud_dashboard.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    confusion_matrix,
    roc_curve, roc_auc_score,
    precision_recall_curve, auc,
    precision_score, recall_score, f1_score,
)

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Fraud Threshold Dashboard",
    page_icon="🔍",
    layout="wide",
)

# ─────────────────────────────────────────────
#  CUSTOM CSS  (dark, industrial feel)
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
    background-color: #0d0f14;
    color: #e0e4ef;
}
h1, h2, h3 { font-family: 'IBM Plex Mono', monospace; letter-spacing: -0.5px; }
.metric-box {
    background: #161a24;
    border: 1px solid #2a2f3e;
    border-radius: 8px;
    padding: 16px 20px;
    text-align: center;
    margin-bottom: 8px;
}
.metric-label { font-size: 11px; color: #6b7395; text-transform: uppercase; letter-spacing: 1.5px; }
.metric-value { font-size: 28px; font-weight: 700; font-family: 'IBM Plex Mono', monospace; }
.good  { color: #4ade80; }
.warn  { color: #facc15; }
.bad   { color: #f87171; }
.section-divider { border: none; border-top: 1px solid #2a2f3e; margin: 24px 0; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  DATA LOADING
#  Expects creditcard.csv from Kaggle in the same directory.
#  Falls back to a synthetic dataset if the file is missing.
# ─────────────────────────────────────────────
@st.cache_data
def load_data():
    """Load and split the credit card fraud dataset."""
    try:
        df = pd.read_csv("creditcard.csv")
        X = df.drop(columns=["Class", "Time"])
        y = df["Class"]
        source = "Kaggle Credit Card Fraud (284,807 rows)"
    except FileNotFoundError:
        # ── Synthetic fallback so the dashboard still runs ──
        rng = np.random.default_rng(42)
        n, fraud_rate = 10_000, 0.017
        X = pd.DataFrame(rng.standard_normal((n, 29)),
                         columns=[f"V{i}" for i in range(1, 30)])
        y = pd.Series(rng.choice([0, 1], size=n,
                                  p=[1 - fraud_rate, fraud_rate]))
        source = "⚠️ Synthetic data (creditcard.csv not found)"

    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, stratify=y, random_state=42
    )
    return X_train, X_test, y_train, y_test, source


# ─────────────────────────────────────────────
#  MODEL TRAINING  (cached — runs once)
#  @st.cache_resource keeps fitted models in memory across
#  every slider drag, so reruns only recompute metrics.
# ─────────────────────────────────────────────
@st.cache_resource
def train_models(_X_train, _y_train):
    """Fit Logistic Regression and Random Forest."""
    log_reg = LogisticRegression(
        class_weight="balanced", max_iter=1000, random_state=42, n_jobs=-1
    )
    log_reg.fit(_X_train, _y_train)

    rf = RandomForestClassifier(
        n_estimators=150, class_weight="balanced",
        max_depth=8, random_state=42, n_jobs=-1
    )
    rf.fit(_X_train, _y_train)
    return log_reg, rf


# ─────────────────────────────────────────────
#  COST METRIC EXPLANATION
#  Total Cost = FN * cost_fn + FP * cost_fp
#
#  FN (False Negative) = a real fraud we missed → bank absorbs
#                        the full fraudulent charge.
#  FP (False Positive) = a legitimate transaction flagged →
#                        analyst time + customer friction.
#
#  As threshold rises: fewer flags → FP ↓, FN ↑ → cost may rise
#  or fall depending on which cost dominates.
#  The cost-minimising τ sits where the marginal saving from one
#  fewer FP exactly equals the marginal loss from one more FN.
# ─────────────────────────────────────────────
def compute_cost(y_true, y_pred, cost_fn, cost_fp):
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()
    return fn * cost_fn + fp * cost_fp, fp, fn, tp, tn


# ─────────────────────────────────────────────
#  COLOUR HELPERS
# ─────────────────────────────────────────────
def colour_class(value, thresholds=(0.5, 0.75)):
    if value >= thresholds[1]: return "good"
    if value >= thresholds[0]: return "warn"
    return "bad"


def metric_box(label, value, css_class=""):
    st.markdown(
        f'<div class="metric-box">'
        f'<div class="metric-label">{label}</div>'
        f'<div class="metric-value {css_class}">{value}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


# ═══════════════════════════════════════════════
#  MAIN APP
# ═══════════════════════════════════════════════
def main():
    # ── Header ──
    st.markdown("# 🔍 Fraud Detection — Threshold Dashboard")
    st.markdown("**P.R.I.M.E. Expansion** · Cost-Sensitive Evaluation · Model Comparison")
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # ── Load & train ──
    X_train, X_test, y_train, y_test, source = load_data()
    st.caption(f"Dataset: {source}")

    log_reg, rf = train_models(X_train, y_train)

    # Pre-compute predicted probabilities once
    y_prob      = log_reg.predict_proba(X_test)[:, 1]   # Logistic Regression
    y_prob_rf   = rf.predict_proba(X_test)[:, 1]         # Random Forest

    # ─────────────────────────────────────────
    #  SIDEBAR — controls
    # ─────────────────────────────────────────
    st.sidebar.markdown("## ⚙️ Controls")

    # Threshold slider
    # Every time the user drags this, Streamlit reruns the script from top.
    # Because models are @st.cache_resource, only the metric math below re-executes.
    tau = st.sidebar.slider(
        "Classification Threshold (τ)",
        min_value=0.01, max_value=0.99,
        value=0.50, step=0.01,
        help="Transactions with predicted fraud probability ≥ τ are flagged.",
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 💰 Cost Parameters")

    cost_fn = st.sidebar.number_input(
        "Cost of Missed Fraud (FN) — $",
        min_value=0, max_value=100_000,
        value=500, step=50,
        help="Average dollar loss when a real fraud transaction is NOT caught.",
    )
    cost_fp = st.sidebar.number_input(
        "Cost of False Alarm (FP) — $",
        min_value=0, max_value=10_000,
        value=25, step=5,
        help="Analyst time + customer friction per incorrectly flagged transaction.",
    )

    st.sidebar.markdown("---")
    model_choice = st.sidebar.radio(
        "Active model for threshold panel",
        ["Logistic Regression", "Random Forest"],
        index=0,
    )

    # Select probabilities for the active model
    y_prob_active = y_prob if model_choice == "Logistic Regression" else y_prob_rf

    # ─────────────────────────────────────────
    #  PANEL 1 — Threshold Analysis
    # ─────────────────────────────────────────
    st.markdown(f"## Panel 1 · Threshold Analysis — {model_choice}")

    y_pred = (y_prob_active >= tau).astype(int)
    total_cost, fp, fn, tp, tn = compute_cost(y_test, y_pred, cost_fn, cost_fp)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec  = recall_score(y_test, y_pred, zero_division=0)
    f1   = f1_score(y_test, y_pred, zero_division=0)

    # ── Key metrics row ──
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1: metric_box("Precision",  f"{prec:.1%}", colour_class(prec))
    with c2: metric_box("Recall",     f"{rec:.1%}",  colour_class(rec))
    with c3: metric_box("F1-Score",   f"{f1:.1%}",   colour_class(f1))
    with c4: metric_box("Total Cost", f"${total_cost:,.0f}", "bad" if total_cost > 50_000 else "warn")
    with c5: metric_box("Flagged",    f"{int((y_pred==1).sum()):,}")

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    col_cm, col_cost = st.columns([1, 2])

    # ── Confusion Matrix ──
    with col_cm:
        st.markdown("### Confusion Matrix")
        cm = confusion_matrix(y_test, y_pred)

        fig_cm, ax = plt.subplots(figsize=(4, 3.5))
        fig_cm.patch.set_facecolor("#0d0f14")
        ax.set_facecolor("#161a24")

        im = ax.imshow(cm, cmap="YlOrRd")
        labels = [["TN", "FP"], ["FN", "TP"]]
        for i in range(2):
            for j in range(2):
                ax.text(j, i, f"{labels[i][j]}\n{cm[i,j]:,}",
                        ha="center", va="center",
                        color="white" if cm[i,j] > cm.max() / 2 else "#ccc",
                        fontsize=13, fontweight="bold",
                        fontfamily="monospace")

        ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
        ax.set_xticklabels(["Pred: Legit", "Pred: Fraud"], color="#9aa3c0")
        ax.set_yticklabels(["Actual: Legit", "Actual: Fraud"], color="#9aa3c0")
        ax.tick_params(colors="#9aa3c0")
        for spine in ax.spines.values(): spine.set_edgecolor("#2a2f3e")
        plt.tight_layout()
        st.pyplot(fig_cm)

        st.markdown(f"""
        <div class="metric-box" style="margin-top:8px">
        <div class="metric-label">Cost Breakdown</div>
        <div style="font-family:'IBM Plex Mono',monospace;font-size:13px;text-align:left;padding-top:8px;line-height:1.8">
        FN ({fn}) × ${cost_fn:,} = <span class="bad">${fn*cost_fn:,.0f}</span><br>
        FP ({fp}) × ${cost_fp:,} = <span class="warn">${fp*cost_fp:,.0f}</span><br>
        <hr style="border-color:#2a2f3e;margin:6px 0">
        <b>Total: <span class="{'bad' if total_cost>50000 else 'warn'}">${total_cost:,.0f}</span></b>
        </div></div>
        """, unsafe_allow_html=True)

    # ── Cost Curve ──
    with col_cost:
        st.markdown("### Dollar-Cost Curve Across Thresholds")

        taus = np.arange(0.01, 1.00, 0.01)
        costs, f1s, precs, recs = [], [], [], []

        for t in taus:
            yp = (y_prob_active >= t).astype(int)
            cm_t = confusion_matrix(y_test, yp)
            tn_t, fp_t, fn_t, tp_t = cm_t.ravel()
            costs.append(fn_t * cost_fn + fp_t * cost_fp)
            f1s.append(f1_score(y_test, yp, zero_division=0))
            precs.append(precision_score(y_test, yp, zero_division=0))
            recs.append(recall_score(y_test, yp, zero_division=0))

        best_cost_tau = taus[np.argmin(costs)]
        best_f1_tau   = taus[np.argmax(f1s)]

        fig_cost, axes = plt.subplots(2, 1, figsize=(7, 6), sharex=True)
        fig_cost.patch.set_facecolor("#0d0f14")

        for ax in axes:
            ax.set_facecolor("#161a24")
            ax.tick_params(colors="#9aa3c0")
            for spine in ax.spines.values(): spine.set_edgecolor("#2a2f3e")
            ax.grid(axis="y", color="#2a2f3e", linewidth=0.5)

        # Top: cost curve
        axes[0].plot(taus, [c/1000 for c in costs], color="#f87171", linewidth=2, label="Total Cost ($k)")
        axes[0].axvline(best_cost_tau, color="#facc15", linestyle="--", linewidth=1.2, label=f"Min Cost τ={best_cost_tau:.2f}")
        axes[0].axvline(tau, color="#60a5fa", linestyle="-",  linewidth=1.5, label=f"Current τ={tau:.2f}")
        axes[0].set_ylabel("Total Cost ($k)", color="#9aa3c0")
        axes[0].legend(fontsize=9, framealpha=0.3, labelcolor="white")
        axes[0].set_title("Cost vs. Threshold", color="#e0e4ef", fontsize=11)

        # Bottom: P / R / F1
        axes[1].plot(taus, precs, color="#4ade80",  linewidth=1.8, label="Precision")
        axes[1].plot(taus, recs,  color="#f472b6",  linewidth=1.8, label="Recall")
        axes[1].plot(taus, f1s,   color="#facc15",  linewidth=1.8, label="F1-Score")
        axes[1].axvline(best_f1_tau, color="#facc15", linestyle="--", linewidth=1.2, label=f"Max F1 τ={best_f1_tau:.2f}")
        axes[1].axvline(tau, color="#60a5fa", linestyle="-", linewidth=1.5)
        axes[1].set_xlabel("Threshold (τ)", color="#9aa3c0")
        axes[1].set_ylabel("Score", color="#9aa3c0")
        axes[1].legend(fontsize=9, framealpha=0.3, labelcolor="white")
        axes[1].set_title("Precision / Recall / F1 vs. Threshold", color="#e0e4ef", fontsize=11)

        plt.tight_layout()
        st.pyplot(fig_cost)

        # Interpretation callout
        st.info(
            f"**Cost-minimising threshold:** τ = {best_cost_tau:.2f}  |  "
            f"**F1-maximising threshold:** τ = {best_f1_tau:.2f}\n\n"
            "Drag the slider to these values to see how the confusion matrix and cost breakdown change. "
            "When FN cost >> FP cost (typical in fraud), the cost-optimal τ sits **lower** than the F1-optimal τ — "
            "the model flags more aggressively to avoid missing real fraud."
        )

    # ─────────────────────────────────────────
    #  PANEL 2 — Model Comparison (ROC vs PR)
    # ─────────────────────────────────────────
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown("## Panel 2 · Model Comparison — Logistic Regression vs. Random Forest")

    # Why PR-AUC matters for imbalanced data:
    # ROC-AUC uses TN in its denominator (via FPR = FP/(FP+TN)).
    # With 99.8% legitimate transactions, TN is enormous, making FPR
    # tiny even when the model misses many frauds. ROC-AUC therefore
    # looks optimistic and masks poor fraud-detection performance.
    # PR-AUC ignores TN entirely — it only asks "of all our fraud
    # predictions, how many were right?" — which is precisely the
    # question that matters in a severely imbalanced setting.

    col_roc, col_pr = st.columns(2)

    # ── ROC curves ──
    with col_roc:
        st.markdown("### ROC Curve (AUC)")
        fpr_lr, tpr_lr, _ = roc_curve(y_test, y_prob)
        fpr_rf, tpr_rf, _ = roc_curve(y_test, y_prob_rf)
        auc_lr = roc_auc_score(y_test, y_prob)
        auc_rf = roc_auc_score(y_test, y_prob_rf)

        fig_roc, ax = plt.subplots(figsize=(5, 4.5))
        fig_roc.patch.set_facecolor("#0d0f14")
        ax.set_facecolor("#161a24")
        ax.plot(fpr_lr, tpr_lr, color="#60a5fa", linewidth=2, label=f"Logistic Reg (AUC={auc_lr:.3f})")
        ax.plot(fpr_rf, tpr_rf, color="#4ade80", linewidth=2, label=f"Random Forest (AUC={auc_rf:.3f})")
        ax.plot([0,1],[0,1], "--", color="#444", linewidth=1)
        ax.set_xlabel("False Positive Rate", color="#9aa3c0")
        ax.set_ylabel("True Positive Rate", color="#9aa3c0")
        ax.tick_params(colors="#9aa3c0")
        for spine in ax.spines.values(): spine.set_edgecolor("#2a2f3e")
        ax.legend(fontsize=9, framealpha=0.2, labelcolor="white")
        ax.grid(color="#2a2f3e", linewidth=0.5)
        plt.tight_layout()
        st.pyplot(fig_roc)

        st.caption(
            "ROC-AUC can be misleadingly high on imbalanced datasets because it credits the model "
            "for correctly classifying the huge number of legitimate transactions (TN)."
        )

    # ── PR curves ──
    with col_pr:
        st.markdown("### Precision-Recall Curve (PR-AUC)")
        prec_lr, rec_lr, _ = precision_recall_curve(y_test, y_prob)
        prec_rf, rec_rf, _ = precision_recall_curve(y_test, y_prob_rf)
        prauc_lr = auc(rec_lr, prec_lr)
        prauc_rf = auc(rec_rf, prec_rf)
        baseline  = y_test.mean()   # random classifier PR-AUC = fraud prevalence

        fig_pr, ax = plt.subplots(figsize=(5, 4.5))
        fig_pr.patch.set_facecolor("#0d0f14")
        ax.set_facecolor("#161a24")
        ax.plot(rec_lr, prec_lr, color="#60a5fa", linewidth=2, label=f"Logistic Reg (PR-AUC={prauc_lr:.3f})")
        ax.plot(rec_rf, prec_rf, color="#4ade80", linewidth=2, label=f"Random Forest (PR-AUC={prauc_rf:.3f})")
        ax.axhline(baseline, linestyle="--", color="#f87171", linewidth=1, label=f"Random baseline ({baseline:.3f})")
        ax.set_xlabel("Recall", color="#9aa3c0")
        ax.set_ylabel("Precision", color="#9aa3c0")
        ax.tick_params(colors="#9aa3c0")
        for spine in ax.spines.values(): spine.set_edgecolor("#2a2f3e")
        ax.legend(fontsize=9, framealpha=0.2, labelcolor="white")
        ax.grid(color="#2a2f3e", linewidth=0.5)
        plt.tight_layout()
        st.pyplot(fig_pr)

        st.caption(
            "PR-AUC is the preferred metric for fraud: it ignores true negatives entirely and "
            "focuses on the precision-recall tradeoff where fraud cases are the rare positive class."
        )

    # ── Summary comparison table ──
    st.markdown("### Summary Metrics at Current Threshold (τ = {:.2f})".format(tau))

    y_pred_rf = (y_prob_rf >= tau).astype(int)
    rows = []
    for name, yp, roc, pr in [
        ("Logistic Regression", y_pred,    auc_lr, prauc_lr),
        ("Random Forest",       y_pred_rf, auc_rf, prauc_rf),
    ]:
        rows.append({
            "Model":      name,
            "ROC-AUC":    f"{roc:.3f}",
            "PR-AUC":     f"{pr:.3f}",
            "Precision":  f"{precision_score(y_test, yp, zero_division=0):.1%}",
            "Recall":     f"{recall_score(y_test, yp, zero_division=0):.1%}",
            "F1":         f"{f1_score(y_test, yp, zero_division=0):.1%}",
            "Total Cost": f"${compute_cost(y_test, yp, cost_fn, cost_fp)[0]:,.0f}",
        })

    st.dataframe(pd.DataFrame(rows).set_index("Model"), use_container_width=True)

    # ─────────────────────────────────────────
    #  INTERPRETATION GUIDE
    # ─────────────────────────────────────────
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown("## 📖 How to Interpret the Dashboard")
    st.markdown("""
**Dragging the threshold from 0.01 → 0.99:**
- At **low τ**: almost every transaction is flagged → Recall ≈ 100%, Precision ≈ fraud rate (~0.17%), FP cost dominates.
- At **high τ**: barely anything is flagged → Precision near 100%, Recall collapses, FN cost dominates.
- The **dollar-cost curve** is U-shaped (or monotone if one cost vastly outweighs the other). The trough is your **cost-optimal operating point**.

**Cost-optimal τ vs. F1-optimal τ:**
| Objective | Preferred τ | Use when… |
|---|---|---|
| Minimise dollar loss | Cost-minimising τ (yellow dashed) | FN cost >> FP cost (typical fraud) |
| Balance P/R | F1-maximising τ | Costs roughly equal, or no dollar model |
| Regulatory / compliance | Low τ ≈ 0.10–0.20 | Must catch >X% of fraud by law |

**PR-AUC vs. ROC-AUC:**  
ROC-AUC rewards correct classification of the majority class (legit transactions). On a 99.8% / 0.2% split, even a naive model scores high. PR-AUC only cares about how well you catch and label the rare fraud class — a much harder and more meaningful bar.
""")

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.caption("Built with the P.R.I.M.E. Framework · Streamlit · scikit-learn · matplotlib")


if __name__ == "__main__":
    main()
