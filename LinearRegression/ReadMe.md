# Understanding the Linear Regression Equation

The equation of a simple linear regression line is:

$$
y = \beta_0 + \beta_1 x
$$

Where:

* **y** = Predicted value (dependent variable)
* **x** = Independent variable
* **$\beta_0$** = Intercept (the point where the line crosses the Y-axis)
* **$\beta_1$** = Slope (the rate of change of y with respect to x)

## Calculating the Slope ($\beta_1$):

The slope is calculated using the formula:

$$
\beta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}
$$

### Explanation:

* **$x_i$**: Each value of the independent variable (hours studied).
* **$\bar{x}$**: Mean of the independent variable.
* **$y_i$**: Each value of the dependent variable (exam scores).
* **$\bar{y}$**: Mean of the dependent variable.
* **$\sum$**: Summation over all data points.

## Step-by-Step Calculation of Slope:

1. **Calculate the Means:**

$$
\bar{x} = \frac{\sum x_i}{n} \quad \text{and} \quad \bar{y} = \frac{\sum y_i}{n}
$$

2. **Calculate the Numerator:**

$$
\sum (x_i - \bar{x})(y_i - \bar{y})
$$

3. **Calculate the Denominator:**

$$
\sum (x_i - \bar{x})^2
$$

4. **Calculate the Slope ($\beta_1$):**

$$
\beta_1 = \frac{\text{Numerator}}{\text{Denominator}}
$$

## Calculating the Intercept ($\beta_0$):

The intercept is calculated as:

$$
\beta_0 = \bar{y} - \beta_1 \bar{x}
$$

### Explanation:

The intercept indicates the predicted value of **y** when **x = 0**.

## Example Calculation:

Given Data:

| Hours Studied (x) | Marks Obtained (y) |
| ----------------- | ------------------ |
| 2                 | 50                 |
| 4                 | 60                 |
| 6                 | 65                 |
| 8                 | 80                 |
| 10                | 90                 |

### Step 1: Calculate Means:

$$
\bar{x} = \frac{2+4+6+8+10}{5} = 6
$$

$$
\bar{y} = \frac{50+60+65+80+90}{5} = 69
$$

### Step 2: Numerator Calculation:

$$
\sum (x_i - \bar{x})(y_i - \bar{y}) = 200
$$

### Step 3: Denominator Calculation:

$$
\sum (x_i - \bar{x})^2 = 40
$$

### Step 4: Slope Calculation:

$$
\beta_1 = \frac{200}{40} = 5
$$

### Step 5: Intercept Calculation:

$$
\beta_0 = 69 - 5 \times 6 = 39
$$

### Final Regression Equation:

$$
y = 39 + 5x
$$

## Interpretation:

* **Slope (5.0)**: For every additional hour studied, the score increases by 5 points.
* **Intercept (39.0)**: If no hours are studied (x = 0), the predicted score is 39.
