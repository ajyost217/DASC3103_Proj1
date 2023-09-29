#mapper

#!/usr/bin/env python

import sys

# Define the map function
def map_function(line):
    try:
        # Split the input line into fields (assuming CSV format)
        fields = line.strip().split(',')
        
        # Extract the target variable (first column) and predictor variables (remaining columns)
        target = float(fields[8])
        predictors = [float(x) for x in fields[0:7]]
        
        # Emit key-value pairs with a common key ('TRAIN') and the target and predictor variables
        # Serialize predictor variables as a comma-separated string
        print(f'TRAIN\t{target}\t{",".join(map(str, predictors))}')
    except Exception as e:
        # Print the exception for debugging
        print(f'Error in map function: {e}, Line: {line.strip()}')

# Process input lines from standard input
for line in sys.stdin:
    map_function(line)

