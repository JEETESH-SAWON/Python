import pandas as pd
import numpy as np

input_data = pd.read_csv('linear_regression_data.csv')
# Extract x and y values
x = input_data['x'].to_numpy
y = input_data['y'].to_numpy


# NumPy for vectorized operations. NumPy operations are inherently optimized to perform calculations 
# on entire arrays without the need for explicit Python loops, making the code more efficient and concise

# Define the function f(x[i]) = w * x[i] + b
def f(x, w, b):
    return w * x + b

x = np.array(x)
y = np.array(y)

w = 0.0  # Initial weight
b = 0.0  # Initial bias
learning_rate = 0.01  # Learning rate
iterations = 1000  # Number of iterations

# Number of data points
m = len(x)

# Gradient descent algorithm
for _ in range(iterations):
    # Compute predictions
    f_x = f(x, w, b)

    # Compute gradients
    b_gradient = (1 / m) * np.sum(f_x - y)
    w_gradient = (1 / m) * np.sum((f_x - y) * x)

    # Update parameters
    w = w - learning_rate * w_gradient
    b = b - learning_rate * b_gradient

    # Print the values of w and b after each iteration for debugging
    print(f"Iteration {_+1}: w = {w}, b = {b}")

print(f"Final values: w = {w}, b = {b}")