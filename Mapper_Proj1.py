#mapper

import sys

# Define the map function
def map_function(line):
    try:
        # Split the input line into fields (assuming CSV format)
        fields = line.strip().split(',')
        
        # Extract the indicator variable (0 or 1)
        indicator = int(fields[8])
        
        # Loop through predictor variables (starting from the second column)
        for i, predictor in enumerate(fields[0:7], start=1):
            # Emit key-value pairs with a common key for all predictor variables
            # Key: predictor variable index (e.g., '0', '1', '2', ...)
            # Value: indicator variable and the predictor value
            print(f'{i}\t{indicator},{predictor}')

    except Exception as e:
        # Handle any exceptions gracefully
        pass

# Process input lines from standard input
for line in sys.stdin:
    map_function(line)
