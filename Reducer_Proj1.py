#reducer

import sys
import numpy as np
from sklearn.linear_model import LinearRegression

# Define the reducer function
def reduce_function():
    # Initialize lists to store target and predictor variables
    y = []
    X = []

    # Iterate over key-value pairs from the map phase
    for line in sys.stdin:
        try:
            _, target, *predictors = line.strip().split('\t')
            
            # Add the target and predictor variables to the lists
            y.append(float(target))
            X.append([float(x) for x in predictors])

        except Exception as e:
            # Print the exception for debugging
            print(f'Error in reduce function: {e}, Line: {line.strip()}')

    # Convert lists to numpy arrays
    y = np.array(y)
    X = np.array(X)

    # Create and fit a linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Print the regression coefficients (slope and intercept)
    slope = model.coef_
    intercept = model.intercept_
    print(f"Slope (Regression Coefficient): {slope}")
    print(f"Intercept: {intercept}")

# Call the reduce function
reduce_function()
