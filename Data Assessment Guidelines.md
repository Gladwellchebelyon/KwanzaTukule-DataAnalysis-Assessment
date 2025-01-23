# Data Assessment Guidelines

## 1. Executive Summary
Provide a high-level summary of the dataset, including:
- The purpose of the dataset.
- Key findings from the assessment.
- High-level recommendations for next steps.

---

## 2. Data Overview
### Dataset Description
- Total number of rows and columns.
- Key features or columns in the dataset.
- Brief description of the dataset's purpose or business context.

### Basic Statistics
- Count of missing, duplicate, and unique values for each column.
- Summary statistics for numerical fields (mean, median, standard deviation, etc.).
- Cardinality for categorical fields.

---

## 3. Data Quality Assessment
### Duplicates
- Total number of duplicate rows.
- Examples of duplicate rows.
- Recommended actions for handling duplicates.

### Missing Data
- Missing values per column (absolute count and percentage).
- Patterns in missing data (e.g., are certain columns always missing together?).
- Proposed strategies for handling missing values (e.g., imputation, deletion, or flagging).

### Inconsistencies
- Formatting issues (e.g., inconsistent date/time or numeric formats).
- Mislabeling or typos in categorical data.
- Recommendations for resolving inconsistencies.

### Outliers
- Total outliers detected per column.
- Visual examples (e.g., boxplots or histograms).
- Recommendations for handling outliers (e.g., removal, transformation, or binning).

---

## 4. Feature-Level Analysis
For each feature/column, provide:
- **Description**: What the feature represents and its importance.
- **Value Distribution**:
  - For numerical columns: histograms, boxplots, or statistical summaries.
  - For categorical columns: bar charts, frequency tables.
- **Data Quality Check**:
  - Missing values.
  - Outliers.
  - Unique value counts (to detect low/high cardinality).

---

## 5. Correlation Analysis
- Heatmap or table showing correlations between numerical features.
- Analysis of key relationships between features:
  - Scatterplots for numeric pairs.
  - Cross-tabulations for categorical pairs.

---

## 6. Key Findings
Summarize unusual patterns, such as:
- Features with high missing value counts.
- Imbalanced distributions in categorical features.
- Significant outliers or anomalies.
- Possible errors or data entry issues.

---

## 7. Recommendations
For each identified issue, provide actionable recommendations:
- **Duplicates**: Remove, merge, or justify retention.
- **Missing Data**: Imputation, deletion, or further exploration.
- **Inconsistencies**: Standardization or normalization.
- **Outliers**: Transformation, removal, or flagging.
- **Specific Columns**: Tailored cleaning or enhancements based on analysis or modeling needs.

---

## 8. Supporting Visualizations
Include key visualizations to support your assessment:
- Boxplots, histograms, and bar charts to illustrate distributions and outliers.
- Heatmaps for correlation analysis.
- Frequency tables or bar charts for categorical data.

---

## 9. Action Plan
Provide a step-by-step outline of the following:
- Cleaning strategies (e.g., deduplication, imputation, normalization).
- Feature engineering ideas (e.g., extracting information from dates or binning categories).
- Preprocessing workflows (e.g., handling outliers or scaling data for models).

---

## 10. Appendix
- Include detailed examples of raw data issues.
- Document any assumptions made during the assessment.

---

This structured assessment ensures thorough analysis, highlights actionable insights, and provides a clear roadmap for the dataset’s preparation and use in analysis or modeling.


