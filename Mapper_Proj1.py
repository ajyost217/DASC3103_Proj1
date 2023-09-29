#mapper

import sys

# Define the map function
def map_function(line):
    try:
        # Split the input line into fields (assuming CSV format)
        fields = line.strip().split(',')
        
        # Extract the indicator variable (0 or 1) and predictor variables
        identifier = fields[7]  # Assuming the identifier is in the first column
        indicator = fields[8]  # Assuming the indicator variable is in the second column
        predictors = fields[0:6]  # Assuming the remaining columns are predictor variables
        
        # Emit key-value pairs with the identifier as the key
        # and the value containing the indicator variable and predictors
        print(f'{identifier}\t{indicator},{",".join(predictors)}')
    except Exception as e:
        # Print the exception for debugging
        print(f'Error in map function: {e}, Line: {line.strip()}')

# Process input lines from standard input
for line in sys.stdin:
    map_function(line)
