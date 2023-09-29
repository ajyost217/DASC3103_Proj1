import sys

def map_function(line):
    try:
        # Split the input line into fields (assuming CSV format)
        fields = line.strip().split(',')
        
        # Extract the indicator variable (0 or 1)
        indicator = int(fields[8])
        
        # Extract the unique key (assuming it's in a specific column, adjust the index as needed)
        unique_key = fields[7]  # Change the index to the appropriate column
        
        # Loop through predictor variables (starting from the second column)
        predictors = fields[0:6]  # Adjust the slice to include all predictor columns
        
        # Emit key-value pairs with the unique key as the key
        # Key: unique key read from the dataset
        # Value: Indicator variable and predictor values
        print(f'{unique_key}\t{indicator},{",".join(predictors)}')

    except Exception as e:
        # Handle any exceptions gracefully
        pass

# Process input lines from standard input
for line in sys.stdin:
    map_function(line)
