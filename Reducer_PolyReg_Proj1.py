import sys
import csv
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# Initialize variables to store data for regression analysis
unique_keys = []  # List to store unique keys
indicator_values = []  # List to store indicator values
predictor_values = []  # List to store predictor values

# Process input key-value pairs from standard input
for line in sys.stdin:
    try:
        # Split the input line into key and value
        key, value = line.strip().split('\t')

        # Use CSV reader to properly parse the value
        value_reader = csv.reader([value])
        row = next(value_reader)

        # Ensure that the row contains at least one value
        if len(row) < 1:
            sys.stderr.write(f'Error: Value field is missing or empty for key {key}\n')
            continue  # Skip this input line and continue processing

        # The row variable now contains a list of values
        indicator = int(row[0])
        
        # Check if there are enough predictor values
        if len(row) < 2:
            sys.stderr.write(f'Error: Not enough predictor values for key {key}\n')
            continue  # Skip this input line and continue processing
        
        predictors = [float(x) for x in row[1:]]

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

    # Create a polynomial regression model
    degree = 2  # You can change the degree as needed
    polyreg = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    
    # Fit the polynomial regression model
    polyreg.fit(X, y)

    # Get regression coefficients
    coefficients = polyreg.named_steps['linearregression'].coef_
    intercept = polyreg.named_steps['linearregression'].intercept_

    # Output the regression results
    print(f'Coefficients: {coefficients}')
    print(f'Intercept: {intercept}')
    print(f'Unique Keys: {unique_keys}')
