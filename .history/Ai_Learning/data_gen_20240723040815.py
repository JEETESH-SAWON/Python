import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Define the true relationship (y = 3x + 5)
true_slope = 3
true_intercept = 5

# Generate independent variable data (x)
x = np.linspace(0, 10, 50)

# Calculate the dependent variable data (y) without noise
y_true = true_slope * x + true_intercept

# Add noise to the dependent variable
noise = np.random.normal(0, 2, x.shape)
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
