# Student Exam Score Predictor (Linear Regression)

A simple Machine Learning project built with Python that demonstrates the core fundamentals of **Linear Regression**. The model predicts a student's final exam score based on the number of hours they dedicated to studying.

---

# Overview

Linear regression is like laying a straight ruler through scattered data points to find the best-fit line. This project maps the relationship between:
- **Feature ($X$):** Hours studied
- **Target ($y$):** Final exam score

---

# Tech Stack

- **Language:** Python
- **Libraries:**
  - `scikit-learn` — model building and linear regression fitting
  - `pandas` & `numpy` — data handling and array transformation
  - `matplotlib` — visualising data points and the regression line

---

# Getting Started

### 1. Clone the Repository
\`\`\`bash
git clone https://github.com/your-username/student-score-predictor.git
cd student-score-predictor
\`\`\`

### 2. Install Dependencies
\`\`\`bash
pip install pandas numpy scikit-learn matplotlib
\`\`\`

### 3. Run the Script
\`\`\`bash
python score_predictor.py
\`\`\`

---

# Results & Visualisation

- Displays a scatter plot of historical student study hours against test scores.
- Draws the best-fit regression line ($y = mx + c$).
- Generates a real-time score prediction for custom test inputs (e.g., studying 6.5 hours).

---

# Key Takeaways
- Understanding features vs. labels in supervised learning.
- How the Ordinary Least Squares (OLS) line minimizes prediction error.
- Reshaping input data for `scikit-learn` pipelines.
