# The Illusion of Growth & the Composition Effect  
**Deflating History with FRED**

## Objective
This lab investigates long-run wage dynamics in the United States by separating **nominal growth from real purchasing power** and correcting for a key statistical bias that emerged during the COVID-19 pandemic. Using live data from the Federal Reserve Economic Data (FRED) API, the project tests whether apparent wage gains reflect genuine improvements in worker welfare or are instead driven by inflation and compositional shifts in the labor force.

## Methodology
This analysis was built as a reproducible Python data pipeline centered on real-time macroeconomic data ingestion and transformation.

1. **Live Data Ingestion via FRED API**  
   I used the `fredapi` library to programmatically fetch official Federal Reserve time series, including:
   - **AHETPI** (Average Hourly Earnings, Total Private) as a measure of nominal wages  
   - **CPI** (Consumer Price Index) to deflate nominal wages into real terms  
   - **ECI (Employment Cost Index – Wages & Salaries)** as a composition-adjusted benchmark  

   Pulling data directly from FRED ensures transparency, reproducibility, and alignment with official macroeconomic sources.

2. **Deflating Nominal Wages**  
   Nominal wage data was converted into **real wages** by adjusting for inflation using CPI. This step isolates changes in purchasing power and allows for a direct test of the “money illusion,” where rising nominal pay masks stagnant real income.

3. **Detecting the Pandemic Anomaly**  
   Visual inspection of real wages revealed a sharp spike in 2020—suggesting a sudden and implausible surge in worker purchasing power during the height of the pandemic. This prompted further investigation into whether the increase reflected true wage growth or a statistical distortion.

4. **Correcting for the Composition Effect**  
   To control for workforce composition changes, I incorporated the **Employment Cost Index (ECI)**. Unlike simple averages, the ECI holds job composition constant, making it robust to shocks where low-wage workers disproportionately exit or re-enter employment.  
   
   By rebasing both wage series to a common index and plotting them together, I directly compared the biased average wage measure to the composition-adjusted benchmark.

## Key Findings: The Pandemic Paradox
The results highlight two core insights:

- **Long-Run Wage Stagnation:**  
  Despite decades of nominal wage growth, real wages have remained largely flat over the past half-century. Inflation absorbs most headline gains, reinforcing the persistence of the money illusion in public wage discourse.

- **The 2020 “Wage Boom” Was Artificial:**  
  The apparent surge in wages during 2020 disappears once composition bias is controlled for. The ECI shows steady, uninterrupted growth—while average wages spike due to the temporary exit of lower-paid workers from the labor force. This confirms that the pandemic-era wage boom was not driven by increased labor demand or productivity, but by statistical averaging effects.

## Takeaway
This lab demonstrates why **methodology matters in macroeconomic measurement**. Without correcting for inflation and composition bias, wage data can tell a deeply misleading story. By integrating theory, live API data, and careful empirical controls, the project shows how economic narratives can shift dramatically once the underlying statistics are properly deflated and adjusted.
