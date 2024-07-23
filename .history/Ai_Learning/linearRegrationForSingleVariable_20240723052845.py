import pandas as pd
import numpy as np

input_data = pd.read_csv('linear_regression_data.csv')
# Extract x and y values
x = input_data['x'].values
y = input_data['y'].values


# NumPy for vectorized operations. NumPy operations are inherently optimized to perform calculations 
# on entire arrays without the need for explicit Python loops, making the code more efficient and concise

# Define the function f(x[i]) = w * x[i] + b
def f(x, w, b):
    return w * x + b

x = np.array([1, 2, 3, 4, 5])  # Example feature values
y = np.array([2, 4, 6, 8, 10])  # Example target values
w = 1.5  # Example weight
b = 0.5  # Example bias

# Number of data points
m = len(x)

# Compute the expression
# 1. Calculate f(x[i]) for each x[i]
f_x = f(x, w, b)

# 2. Compute (f(x[i]) - y[i]) * x[i] for each i
diff = (f_x - y) * x

# 3. Compute the sum
summation = np.sum(diff)

# 4. Apply the scaling factor
result = (1 / (2 * m)) * summation

print("f_x:", f_x)
print("diff:", diff)
print("Summation:", summation)
print("Result:", result)