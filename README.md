# Sales Performance Analysis Using Statistical Methods

## Project Overview

This project analyzes retail sales data to answer a critical business question: **Does our marketing campaign actually increase revenue?**

Using statistical methods, the analysis examines sales performance, tests hypotheses, and provides data-driven recommendations to management.

---

## Business Context

A retail company operating online and physical stores needs to:
- Understand overall sales performance.
- Assess revenue reliability and stability.
- Determine if their marketing strategy is effective.

The analysis uses 3 years of transaction data to provide statistical evidence for decision-making.

---

## Dataset

Transaction-level sales data with the following fields:

| Column             | Description                    |
|--------------------|--------------------------------|
| date               | Transaction date               |
| store_type         | Online / Physical              |
| region             | Geographic region              |
| units_sold         | Number of units per transaction|
| revenue            | Total revenue (KES)            |
| marketing_campaign | Whether campaign was active    |

---

## Analysis Components

### 1. Descriptive Statistics
- **Central Tendency**: Mean, median, mode of monthly revenue
- **Dispersion**: Range, variance, standard deviation to assess sales stability
- **Distribution Shape**: Histogram analysis, skewness, and kurtosis

### 2. Data Visualization
- Line chart: Revenue trends over time
- Bar chart: Performance by store type
- Box plot: Revenue distribution across regions
- Scatter plot: Marketing spend vs revenue relationship

### 3. Sampling Analysis
- Population vs sample definition
- Identification and mitigation of sampling bias
- Evaluation of sampling methodology

### 4. Statistical Foundations
- **Law of Large Numbers**: Sample mean convergence analysis
- **Central Limit Theorem**: Distribution of sample means demonstration

### 5. Hypothesis Testing
**Research Question**: Does the marketing campaign increase average revenue per transaction?

- Formulated null and alternative hypotheses
- Conducted t-test at 95% confidence level
- Calculated p-value and test statistics
- Made statistical decision (reject or fail to reject H₀)

### 6. Error Analysis
- Type I and Type II error interpretation
- Business implications of incorrect conclusions

### 7. Effect Size & Statistical Power
- Cohen's d calculation
- Effect size interpretation (small/medium/large)
- Power analysis and sample size considerations

---

## Key Findings

*Summary of results from the statistical analysis:*

- Marketing campaign shows statistically significant revenue increase (p < 0.05)
- Effect size is medium (Cohen's d = 0.5), indicating practical significance
- Revenue exhibits seasonal patterns with higher variance in Q4
- Online stores show more consistent performance compared to physical locations
- Sample size of 30+ transactions per segment ensures reliable statistical inferences

---

## Tools & Methods

- **Python**: pandas, numpy, scipy, matplotlib, seaborn
- **Statistical Tests**: Independent samples t-test
- **Visualization**: Matplotlib and Seaborn for exploratory analysis
- **Analysis Environment**: Jupyter Notebook

---

## Project Structure

```
sales-performance-statistical-analysis/
├── data/
│   └── sales_data.csv
├── src/
│   ├── __init__.py
│   └── helpers.py
├── notebooks/
│   └── statistical_analysis.ipynb
├── reports/
│   └── findings_report.pdf
├── README.md
├── pyproject.toml
└── uv.lock
```

---

## How to Run

### Setup Project
```bash
# Navigate to project root and initialize
uv init

# Create project folders
mkdir src, notebooks, data, reports
```

### Install Dependencies
```bash
# Install core dependencies
uv add pandas numpy scipy matplotlib seaborn

# Add development tools for Jupyter
uv add --dev jupyter ipykernel

# Create Jupyter kernel
uv run python -m ipykernel install --user --name=luxdev_analysis --display-name "Python (LuxDev Analysis)"
```

### Launch Analysis
```bash
# Start Jupyter Notebook
uv run jupyter notebook notebooks/statistical_analysis.ipynb
```

---

## Statistical Methods Applied

- Descriptive statistics (mean, median, variance, standard deviation)
- Inferential statistics (hypothesis testing, confidence intervals)
- Distribution analysis (normality testing, skewness assessment)
- Effect size calculation (Cohen's d)
- Sampling theory application (CLT, Law of Large Numbers)

---

## Business Recommendations

Based on statistical findings:

1. **Continue marketing campaign** - statistically significant revenue lift detected with medium effect size.
2. **Monitor regional performance** - high variance in certain regions requires investigation.
3. **Optimize Q4 strategy** - seasonal patterns suggest opportunity for targeted planning.
4. **Invest in online channels** - lower variance indicates more predictable revenue stream.
5. **Expand sample size** - improve statistical power for future segment-level analyses.

---

## Skills Demonstrated

- Statistical analysis and hypothesis testing
- Data-driven decision making
- Business problem formulation
- Statistical programming (Python)
- Clear communication of technical findings
- Understanding of sampling and bias
- Practical application of statistical theory

---

## About This Project

Completed as part of the **LuxDevHQ Data Analytics Program**, this project demonstrates the application of statistical methods to real business problems. The focus is on statistical analysis, appropriate test selection, and translating statistical results into actionable business insights.

---

## Author

kyegon | LuxDevHQ Program

---

## License

This project is available for educational purposes.