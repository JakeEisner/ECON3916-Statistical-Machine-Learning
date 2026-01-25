# The Cost of Living Crisis: A Data-Driven Analysis

## The Problem
Official inflation statistics often suggest that price pressures are stabilizing. However, this narrative frequently fails to reflect the lived experience of students. The Consumer Price Index (CPI) is designed to represent an “average” consumer, but students are not average consumers. Their budgets are disproportionately allocated toward tuition, rent, and food away from home—categories that receive relatively low weight in headline CPI. This project examines whether inflation experienced by students materially diverges from national inflation metrics.

---

## Methodology
This analysis was conducted using Python, pandas, matplotlib, and the Federal Reserve Economic Data (FRED) API. I constructed a student-relevant basket of goods and identified appropriate CPI proxy series for tuition, rent, food away from home, and streaming services. Because CPI components are published with different base years, all series were re-indexed to a common baseline (2016 = 100) to ensure valid comparisons, following standard index-number theory.

Using a Laspeyres-style framework, I applied student-specific expenditure weights—placing greater emphasis on tuition and housing—to calculate a weighted **Student Spending Price Index (Student SPI)**. The project includes normalized component trend analysis, a weighted comparison against official CPI, a demonstration of scale fallacy using raw CPI indices, and a regional comparison incorporating Boston-area CPI data.

---

## Key Findings
My analysis reveals a persistent and widening divergence between student costs and national inflation. Since 2016, the Student SPI has risen approximately **4–6% faster than official CPI**, driven primarily by housing, food away from home, and education costs. While national CPI reflects steady inflation, student-weighted inflation accelerates more sharply following 2021, creating a visible “inflation gap.” Regional analysis further shows that students in high-cost metropolitan areas such as Boston face stronger inflation pressures than the national average. These findings highlight how headline CPI can understate inflation for populations with non-average consumption patterns.

---

## Tools & Skills Demonstrated
- Python (pandas, matplotlib)
- API data ingestion (FRED)
- Time-series analysis
- Inflation measurement & index construction
- Laspeyres index methodology
- Data visualization & economic storytelling
