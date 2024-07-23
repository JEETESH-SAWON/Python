import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Define the true relationship (y = 3x + 5)
true_slope = 3
true_intercept = 5

# Generate independent variable data (x) np.linespace create x from 0 to 10 in 50 iteration
x = np.linspace(0, 10, 98)

# Calculate the dependent variable data (y) without noise find y with slope formula y=3x+5
y_true = true_slope * x + true_intercept

# Add noise to the dependent variable noise added to y where 0 is mean(0)= noise value is centered around 0
# 5 is standerd daviation means value is btw -5 and 5 x.shape array size of x which is single D 50 size array
noise = np.random.normal(0, 5, x.shape)
y = y_true + noise

# Plot the generated data
plt.scatter(x, y, color='blue', label='Training data')
plt.plot(x, y_true, color='red', label='True relationship')
plt.xlabel('Independent Variable (x)')
plt.ylabel('Dependent Variable (y)')
plt.title('Generated Training Data for Linear Regression')
plt.legend()
plt.show()

# Save data to CSV (optional)
data = pd.DataFrame({'x': x, 'y': y})
data.to_csv('linear_regression_data.csv', index=False)
