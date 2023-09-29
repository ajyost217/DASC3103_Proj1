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
    current_identifier = None
    for line in sys.stdin:
        try:
            key, value = line.strip().split('\t')
            indicator, *predictors = value.split(',')
            
            # Check if the identifier has changed (new record)
            if key != current_identifier:
                # If it's a new record, process the previous record (if any)
                if current_identifier is not None:
                    # Convert lists to numpy arrays
                    y = np.array(y)
                    X = np.array(X)

                    # Create and fit a logistic regression model
                    model = LogisticRegression()
                    model.fit(X, y)

                    # Make a prediction (e.g., probability of class 1)
                    prediction = model.predict_proba(X)[:, 1]

                    # Print the identifier and the prediction(s)
                    print(f'{current_identifier}\t{",".join(map(str, prediction))}')

                # Reset lists for the new record
                current_identifier = key
                y = []
                X = []

            # Add the indicator and predictors to the lists
            y.append(float(indicator))
            X.append([float(x) for x in predictors])

        except Exception as e:
            # Print the exception for debugging
            print(f'Error in reduce function: {e}, Line: {line.strip()}')

    # Process the last record (if any)
    if current_identifier is not None:
        y = np.array(y)
        X = np.array(X)
        model = LogisticRegression()
        model.fit(X, y)
        prediction = model.predict_proba(X)[:, 1]
        print(f'{current_identifier}\t{",".join(map(str, prediction))}')

# Call the reduce function
reduce_function()
