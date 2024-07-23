import pandas as pd
input_data = pd.read_csv('linear_regression_data.csv')
# Extract x and y values
x = input_data['x'].values
y = input_data['y'].values

print("x values:", x)
print("y values:", y)