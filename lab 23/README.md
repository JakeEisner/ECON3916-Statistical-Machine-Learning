# FedSpeak Analysis — NLP on FOMC Minutes

## Objective
Quantify shifts in Federal Reserve communication style across two decades of FOMC meeting minutes by applying natural language processing techniques to extract sentiment signals and identify distinct monetary policy language regimes.

## Methodology
- Loaded 240 FOMC meeting minutes (2000–2026) from the `vtasca/fomc-statements-minutes` HuggingFace dataset
- Preprocessed text via lowercasing, stop word removal, and WordNet lemmatization using NLTK
- Constructed a 240 × 2,000 TF-IDF document-term matrix with unigrams and bigrams (`min_df=5`, `max_df=0.85`)
- Computed Loughran-McDonald (LM) sentiment scores — net sentiment and uncertainty — using a domain-specific financial dictionary to avoid false positives from general-purpose lexicons
- Visualized net sentiment and uncertainty trends across 25 years, annotating key macro events (Lehman, Taper Tantrum, COVID, Tightening cycle)
- Applied TruncatedSVD (50 components, 79.9% variance retained) followed by K-Means clustering (K=3) to identify distinct language regimes in TF-IDF space
- Compared pre-COVID (before March 2020) vs post-COVID sentiment distributions using box plots

## Key Findings
- K-Means identified three interpretable language regimes: a pre-GFC conventional policy cluster (2000–2008), a large post-crisis cluster reflecting unconventional policy vocabulary like quantitative easing and forward guidance (2008–2026), and a smaller cluster of crisis and pivot meetings distinguished by anomalous language regardless of time period
- Post-COVID FOMC minutes show a measurable decline in net sentiment (0.0028 vs 0.0081 pre-COVID), reflecting the Fed's more cautious tone through the pandemic recovery and the 2022–2023 tightening cycle
- Uncertainty scores remained stable across periods (~0.022), suggesting the Fed maintains a consistently hedged communication style independent of the policy environment
- Sentiment troughs align precisely with known macro stress events: the 2008 financial crisis produced the most negative meeting on record (December 2008), while the most positive meeting (June 2004) coincides with the mid-2000s expansion

## Tools & Libraries
`Python` · `HuggingFace Datasets` · `NLTK` · `scikit-learn` · `pandas` · `matplotlib`

## Course
ECON 3916: Data Science for Economists
