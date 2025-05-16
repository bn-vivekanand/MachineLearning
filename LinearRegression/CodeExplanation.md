# Python Program: Linear Regression (Study Hours vs. Exam Scores)

This Python program demonstrates a simple linear regression model to predict exam scores based on study hours. The model uses the `scikit-learn` library for regression and `matplotlib` for visualization.

## Program Explanation

### Step 1: Import Libraries

We start by importing the necessary libraries:

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
```

* **numpy**: For handling arrays and numerical operations.
* **matplotlib**: For plotting data points and the regression line.
* **sklearn.linear\_model**: For creating and training the linear regression model.

### Step 2: Generate Data

The independent variable (`hours`) represents study hours, and the dependent variable (`scores`) represents exam scores.

```python
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # Independent variable (Hours)
scores = np.array([45, 50, 55, 60, 65, 70, 75, 80, 85, 90])       # Dependent variable (Scores)
```

* We use `reshape(-1, 1)` to convert the 1D array to a 2D column vector, as required by `scikit-learn`.

### Step 3: Fit the Model

We create and train the linear regression model:

```python
model = LinearRegression()
model.fit(hours, scores)
```

* **LinearRegression()**: Creates a linear regression model.
* **fit()**: Trains the model using the given data.

### Step 4: Predict Scores

Predict scores for new study hours (7, 9, 11):

```python
new_hours = np.array([[7], [9], [11]])  # Predict for 7, 9, and 11 hours
predicted_scores = model.predict(new_hours)
```

* We use the **predict()** function to generate predictions.

### Display the Predictions

```python
print("Predicted Scores:")
for hr, score in zip(new_hours.flatten(), predicted_scores):
    print(f"Predicted score for studying {hr} hours: {score:.2f}")
```

* The `zip()` function pairs study hours with predicted scores.
* `flatten()` converts the 2D array to 1D for easy iteration.

### Step 5: Plot the Data and Regression Line

```python
plt.figure(figsize=(8, 5))
plt.scatter(hours, scores, color='blue', label='Actual data')
plt.plot(hours, model.predict(hours), color='red', linewidth=2, label='Regression line')
plt.scatter(new_hours, predicted_scores, color='green', marker='x', s=100, label='Predictions')
plt.title('Linear Regression: Study Hours vs. Exam Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.legend()
plt.show()
```

* **plt.scatter()**: Plots actual data points.
* **plt.plot()**: Draws the regression line.
* **plt.title(), plt.xlabel(), plt.ylabel()**: Add a title and labels to the plot.
* **plt.legend()**: Shows the legend for clarity.

### Output:

```
Predicted Scores:
Predicted score for studying 7 hours: 75.00
Predicted score for studying 9 hours: 85.00
Predicted score for studying 11 hours: 95.00
```

### Interpretation:

The model predicts that studying:

* **7 hours** results in a score of **75.00**.
* **9 hours** results in a score of **85.00**.
* **11 hours** results in a score of **95.00**.

The regression line clearly shows a positive correlation between study hours and exam scores, indicating that more study hours lead to higher scores.
