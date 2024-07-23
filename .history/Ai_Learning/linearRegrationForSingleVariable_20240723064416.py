import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# read data from csv
input_data = pd.read_csv('linear_regression_data.csv')

# Extract x and y values
x = input_data['x']
y = input_data['y']


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
iterations = 10000  # Number of iterations

# Number of data points
m = len(x)

# Gradient descent algorithm same as learned where w = (1/m)sum of (fwb(x[i]) - y[i])x[i]) 
# from i=0 to i=m where
# fwb(x[i]) or y(cap) = wx[i]+b and b = (1/m) sum of (fwb (x[i]) - y[i])) 
# ---until w_gradient or b_gradient is very small or reaches to zero

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
y_aprox = w*x + b
y_true = 3*x + 5 #orignal slope through which data is created
plt.scatter(x, y, color='blue', label='Training data')
plt.plot(x, y_true, color='red', label='True relationship')
plt.plot(x, y_aprox, color='green', label='approx relationship')
plt.xlabel('Independent Variable (x)')
plt.ylabel('Dependent Variable (y)')
plt.title('Generated Training Data for Linear Regression')
plt.legend()
plt.show()