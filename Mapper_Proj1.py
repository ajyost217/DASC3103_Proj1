def map_function(line):
    expected_headers = "Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome"
    
    if line.strip() == expected_headers:
        # Skip the header line
        return
    
    try:
        # Split the input line into fields (assuming CSV format)
        fields = line.strip().split(',')
        
        # Extract the indicator variable (0 or 1)
        indicator = int(fields[8])
        
        # Extract the unique key (assuming it's in a specific column, adjust the index as needed)
        unique_key = fields[7]  # Change the index to the appropriate column
        
        # Loop through predictor variables (use the specific column names)
        pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age, outcome = fields[:9]
        
        # Emit key-value pairs with the unique key as the key
        # Key: unique key read from the dataset
        # Value: Indicator variable and predictor values
        print(f'{unique_key}\t{indicator},{pregnancies},{glucose},{blood_pressure},{skin_thickness},{insulin},{bmi},{diabetes_pedigree},{age},{outcome}')

    except Exception as e:
        # Handle any exceptions gracefully and print the problematic line
        print(f"ERROR IN MAPPING: {line.strip()}")
        pass

# Process input lines from standard input
for line in sys.stdin:
    map_function(line)
