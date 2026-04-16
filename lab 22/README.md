# Clustering World Economies with K-Means & PCA

## Objective
To identify underlying patterns in global economic development by clustering countries using multiple World Bank indicators and comparing these groupings to traditional income classifications.

## Methodology
- Collected 10 World Bank development indicators for ~160 countries using the `wbgapi` API  
- Cleaned and preprocessed the dataset, handling missing values and retaining usable features  
- Standardized variables using `StandardScaler` to ensure equal contribution to K-Means distance calculations  
- Applied K-Means clustering with K=4 to group countries based on development characteristics  
- Used Principal Component Analysis (PCA) to reduce dimensionality and visualize clusters in 2D  
- Evaluated clustering performance using the elbow method and silhouette scores for K=2 to K=10  
- Compared clusters to World Bank income classifications using cross-tabulation  
- Applied the same pipeline to the California Housing dataset to analyze regional housing patterns  

## Key Findings
- Both the elbow method and silhouette analysis identified **K=4** as the optimal number of clusters for global economies  
- Results showed one large cluster of similar countries and smaller clusters capturing differences in unemployment and digital connectivity  
- PCA visualization indicated most countries are closely grouped, with a few outliers driving separation  
- Comparison with World Bank income groups was limited due to API matching issues, but clustering still revealed structure beyond GDP-based classification  
- In the California Housing dataset, **K=2** was optimal, separating areas into higher-density urban markets and more suburban, lower-density regions  
