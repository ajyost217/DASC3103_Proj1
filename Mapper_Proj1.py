#mapper

import sys

# Define the map function
def map_function(line):
    try:
        # Split the input line into fields (assuming CSV format)
        fields = line.strip().split(',')
        
        # Extract the target variable (first column) and predictor variables (remaining columns)
        target = float(fields[8])
        predictors = [float(x) for x in fields[6]]
        
        # Emit key-value pairs for the target variable (key: 'TARGET') and each predictor variable
        # Each predictor variable is emitted as a separate key-value pair
        print(f'TARGET\t{target}')
        for i, predictor in enumerate(predictors):
            print(f'PREDICTOR_{i}\t{predictor}')

    except Exception as e:
        # Print the exception for debugging
        print(f'Error in map function: {e}, Line: {line.strip()}')

# Process input lines from standard input
for line in sys.stdin:
    map_function(line)
