import sys
import numpy as np
from sklearn.linear_model import LinearRegression

# Initialize variables to store data for regression analysis
unique_keys = []  # List to store unique keys
indicator_values = []  # List to store indicator values
predictor_values = []  # List to store predictor values

# Process input key-value pairs from standard input
for line in sys.stdin:
    try:
        # Split the input line into key and value
        key, value = line.strip().split('\t')
        
        # Split the value into indicator and predictor values
        indicator, predictors = value.split(',')
        
        # Convert to int and float as needed
        indicator = int(indicator)
        predictors = [float(x) for x in predictors.split(',')]
        
        # Append data to respective lists
        unique_keys.append(key)
        indicator_values.append(indicator)
        predictor_values.append(predictors)

    except Exception as e:
        # Handle exceptions and log the error message
        sys.stderr.write(f'Error processing input: {str(e)}\n')

# Check if we have data to perform regression analysis
if len(unique_keys) > 0:
    # Convert lists to NumPy arrays for regression
    X = np.array(predictor_values)
    y = np.array(indicator_values)

    # Perform linear regression
    model = LinearRegression()
    model.fit(X, y)

    # Get regression coefficients
    coefficients = model.coef_
    intercept = model.intercept_

    # Output the regression results
    print(f'Coefficients: {coefficients}')
    print(f'Intercept: {intercept}')
    print(f'Unique Keys: {unique_keys}')
