## Global Purchasing Power Parity Analysis  
**Using the Big Mac Index to Test the Law of One Price**

### Objective
This project evaluates the Law of One Price by using the Big Mac Index to assess whether exchange rates across countries reflect relative purchasing power parity when measured through a standardized consumer good.

### Methodology
- Constructed a structured dataset from The Economist’s 2015 Big Mac Index by manually ingesting country-level price data using Python dictionaries.
- Calculated implied purchasing power parity (PPP) exchange rates by comparing local Big Mac prices to the U.S. benchmark price.
- Computed currency misalignment by measuring the percentage overvaluation or undervaluation of each currency relative to the U.S. dollar.
- Organized and analyzed results using Pandas to ensure clarity, reproducibility, and economic interpretability.

### Key Findings
The analysis reveals meaningful deviations from purchasing power parity across countries, indicating persistent inefficiencies in foreign exchange markets. Several currencies appear overvalued relative to the U.S. dollar, while others are significantly undervalued, suggesting potential long-run adjustment pressures through trade flows and arbitrage mechanisms.

For example, the results indicate that the Norwegian krone was overvalued by approximately X%, whereas currencies in several emerging markets exhibited systematic undervaluation. These findings are consistent with economic theory, which suggests that factors such as non-tradable inputs, taxation, labor costs, and market frictions can prevent full price convergence even for globally standardized goods.

### Economic Insight
Overall, this project demonstrates how simplified measures like Burgernomics can provide intuitive yet analytically useful insights into exchange rate distortions, reinforcing the idea that while purchasing power parity may hold in the long run, short- and medium-run deviations are both common and economically meaningful.
