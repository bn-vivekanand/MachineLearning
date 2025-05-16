import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Generate synthetic data (Hours studied vs. Exam scores)
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # Independent variable (Hours)
scores = np.array([45, 50, 55, 60, 65, 70, 75, 80, 85, 90])       # Dependent variable (Scores)

# Step 2: Fit a linear regression model
model = LinearRegression()
model.fit(hours, scores)

# Step 3: Predict scores for new study hours
new_hours = np.array([[7], [9], [11]])  # Predict for 7, 9, and 11 hours
predicted_scores = model.predict(new_hours)

# Display the predictions
print("Predicted Scores:")
for hr, score in zip(new_hours.flatten(), predicted_scores):
    print(f"Predicted score for studying {hr} hours: {score:.2f}")

# Step 4: Plot the data points and the regression line
plt.figure(figsize=(8, 5))
plt.scatter(hours, scores, color='blue', label='Actual data')
plt.plot(hours, model.predict(hours), color='red', linewidth=2, label='Regression line')
plt.scatter(new_hours, predicted_scores, color='green', marker='x', s=100, label='Predictions')
plt.title('Linear Regression: Study Hours vs. Exam Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.legend()
plt.show()

# OUTPUT:
# Predicted Scores:
# Predicted score for studying 7 hours: 75.00
# Predicted score for studying 9 hours: 85.00
# Predicted score for studying 11 hours: 95.00