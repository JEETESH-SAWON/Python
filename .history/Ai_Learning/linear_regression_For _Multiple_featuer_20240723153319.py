import numpy as np

# Generate some example data
np.random.seed(42)
m = 100  # number of samples
X = 2 * np.random.rand(m, 4)
y = 4 + 3 * X[:, 0] + 2 * X[:, 1] + X[:, 2] + 0.5 * X[:, 3] + np.random.randn(m)

# Initialize parameters
w = np.random.randn(4)  # weights for the 4 features
b = np.random.randn()   # bias term
learning_rate = 0.01
n_iterations = 10000

# Gradient descent
for iteration in range(n_iterations):
    w_gradient = np.zeros_like(w)
    b_gradient = 0.0
    for i in range(m):
        prediction = np.dot(X[i], w) + b
        error = prediction - y[i]
        for j in range(len(w)):
            w_gradient[j] += error * X[i, j]
        b_gradient += error
    w = w - learning_rate * (1 / m) * w_gradient
    b = b - learning_rate * (1 / m) * b_gradient

# Print the resulting parameters
print("Weights:", w)
print("Bias:", b)