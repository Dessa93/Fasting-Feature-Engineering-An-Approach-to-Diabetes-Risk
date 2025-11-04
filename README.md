# 🩺 Fasting Feature Engineering: An Approach to Diabetes Risk

## Project Overview

This project executes a complete Data Science pipeline, emphasizing **SQL-based Feature Engineering** to create the novel **Fasting Duration (`fasting_duration_hours`)** variable from raw metabolic and timestamp data. The core analysis moves beyond standard risk prediction to specifically investigate the relationship between this engineered variable and **diabetes prevalence**, confirming that longer fasting periods are significantly associated with a higher-risk demographic. The study then assesses the predictive contribution of this new feature within a robust Machine Learning classification model, which was optimized via Grid Search to minimize the critical risk of **False Negatives** (undetected cases of diabetes).


## 🚀 Key Results and Conclusions

### 1. Statistical Analysis

* **Distribuion of Fasting Duration(hours)**: Biomodal Distribution -  peak 1 (short fasting - 8h) and peak 2 (long fasting - 12h). Most participants are divided in these two groups. Just a few participants fast between 10 to 12 hours.
* **Relationship Between Fasting Duration and Prevalence of Diabetes**: The graph reveals that the prevalence of diabetes is significantly higher in the group engaging in prolonged fasting (above 13 hours). This observed correlation may be a result of targeted clinical intervention or individual attempts to achieve better glycemic control by extending fasting windows.
* **Relationship Between Fasting Duration, Glucose Levels and Diabetes Outcome**: The scatter plot confirmed that Glucose Level is the strongest predictive factor for the diabetes outcome, given the clear vertical separation between the Diabetic and Healthy groups. Fasting Duration, although showing two distinct clusters (~8h and ~14h), functions as a secondary risk indicator, showing a slightly higher concentration of Diabetic cases in the Long Fasting group.
 

### 2. Final Model Performance (Optimized Random Forest)

The **Random Forest** model, optimized via **Grid Search** to maximize the **Recall** metric, achieved the following results on the test set:

| Metric | Optimized Model | Baseline Model (Logistic Regression) |
| :--- | :---: | :---: |
| **Accuracy** | $\approx 0.740$ | $0.721$ |
| **Precision** | $\approx 0.667$ | $0.612$ |
| **Recall (Sensitivity)** | **$0.611$ (61.1%)** | $0.556$ |
| **Reduction of False Negatives** | **21** FN | 24 FN |

> **Conclusion:** The optimization successfully improved **Recall by $5.5\%$** and reduced the most critical error, **False Negatives**, from 24 to **21**. This makes the final model safer and more effective for risk detection in a healthcare context.

### 3. Data Insights and Feature Engineering

* **Dominant Feature:** **Glucose** was confirmed as the strongest predictor (Correlation: 0.47).
* **Novel Feature Value:** Analysis of the engineered **`fasting_duration_hours`** revealed a bimodal distribution (peaks at approx 8h and approx 14h). The incidence of diabetes was significantly higher in the Long Fasting Group ($>13h$). Although the linear correlation was weak ($0.06$), the feature contributed to the performance gain in the optimized Random Forest model.

---

## 🛠️ Project Structure and Technologies

### Key Files

* **`data_analysis.ipynb`**: The main notebook containing the entire project flow: EDA, feature creation, model training, and optimization.
* **`feature_engineering.sql`**: The SQL script used to calculate the crucial `fasting_duration_hours` feature from raw timestamp data.
* **`metabolic_measurements.csv` / `participants_info.csv`**: Raw input data.

### Technologies Used

* **Languages:** Python (3.x), SQL
* **Tools:** Jupyter Notebook (VS Code)
* **Data Analysis & Viz:** Pandas, Matplotlib, Seaborn
* **Machine Learning:** Scikit-learn (RandomForestClassifier, GridSearchCV)
* **Database:** PostgreSQL / `psycopg2` (for data handling).

## 🚀 How to Replicate the Analysis

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Dessa93/Fasting-Feature-Engineering-An-Approach-to-Diabetes-Risk]
    cd Fasting-Feature-Engineering-An-Approach-to-Diabetes-Risk
    ```
2.  **Setup Environment:**
    (Ensure you have Python 3.x and optionally create a virtual environment, e.g., `venv_analise`)
    ```bash
    # Example setup command:
    pip install pandas matplotlib seaborn scikit-learn psycopg2-binary
    ```
    *Note: The project was developed using `venv_analise`.*
    
3.  **Run the Notebook:**
    Open `data_analysis.ipynb` and execute the cells sequentially. The notebook recreates the fasting feature (from the database query logic) and runs the complete ML analysis.
