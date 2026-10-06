import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Score': [48, 52, 58, 65, 70, 74, 82, 86, 91, 98]
}

df = pd.DataFrame(data)

X = df[['Hours']]
y = df['Score']

model = LinearRegression()
model.fit(X, y)

new_student_hours = np.array([[6.5]])
predicted_score = model.predict(new_student_hours)

print(f"Predicted score for 6.5 study hours: {predicted_score[0]:.1f} / 100")

Zplt.scatter(df['Hours'], df['Score'], color='blue', label='Actual Student Scores')
plt.plot(df['Hours'], model.predict(X), color='red', linewidth=2, label='Best-Fit Ruler Line')
plt.scatter(6.5, predicted_score[0], color='green', s=100, zorder=5, label='Our Prediction (6.5 hrs)')

plt.title('Study Hours vs Exam Score')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score (%)')
plt.legend()
plt.grid(True)
plt.show()
