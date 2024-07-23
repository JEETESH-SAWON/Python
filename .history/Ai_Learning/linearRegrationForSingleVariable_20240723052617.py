import pandas as pd
input_data = pd.read_csv('linear_regression_data.csv')
# Extract x and y values
x = input_data['x'].values
y = input_data['y'].values


# NumPy for vectorized operations. NumPy operations are inherently optimized to perform calculations 
# on entire arrays without the need for explicit Python loops, making the code more efficient and concise
