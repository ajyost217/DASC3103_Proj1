#reducer

import sys
import numpy as np
from sklearn.linear_model import LogisticRegression

# Define the reducer function
def reduce_function():
    # Initialize lists to store target and predictor variables
    y = []
    X = []

    # Iterate over key-value pairs from the map phase
    current_key = None
    for line in sys.stdin:
        try:
            key, value = line.strip().split('\t')
            indicator, predictor = value.split(',')
            
            # Check if the key has changed (new predictor variable)
            if key != current_key:
                # If it's a new predictor variable, process the previous predictor variable (if any)
                if current_key is not None:
                    # Convert lists to numpy arrays
                    y = np.array(y)
                    X = np.array(X)

                    # Ensure X is a 2D array
                    if X.ndim == 1:
                        X = X.reshape(-1, 1)

                    # Create and fit a logistic regression model
                    model = LogisticRegression()
                    model.fit(X, y)

                    # Print the model parameters (coefficients and intercept)
                    slope = model.coef_
                    intercept = model.intercept_
                    print(f"Slope: {slope[0][0]}")
                    print(f"Intercept: {intercept[0]}")

                # Reset lists for the new predictor variable
                current_key = key
                y = []
                X = []

            # Add the indicator and predictor values to the lists
            y.append(int(indicator))
            X.append(float(predictor))

        except Exception as e:
            # Handle any exceptions gracefully
            pass

    # Process the last predictor variable (if any)
    if current_key is not None:
        # Convert lists to numpy arrays
        y = np.array(y)
        X = np.array(X)

        # Ensure X is a 2D array
        if X.ndim == 1:
            X = X.reshape(-1, 1)

        # Create and fit a logistic regression model
        model = LogisticRegression()
        model.fit(X, y)

        # Print the model parameters for the last predictor variable
        slope = model.coef_
        intercept = model.intercept_
        print(f"Slope: {slope[0][0]}")
        print(f"Intercept: {intercept[0]}")

# Call the reduce function
reduce_function()
