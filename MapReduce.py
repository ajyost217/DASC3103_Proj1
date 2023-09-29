from mrjob.job import MRJob
import numpy as np

class MyMRJob(MRJob):
    def configure_args(self):
        super(MyMRJob, self).configure_args()
        self.add_passthru_arg('--output-format', default='key_value')

    def map(self, _, line):
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
            yield unique_key, ('data', indicator, predictors)

        except Exception as e:
            # Handle any exceptions gracefully
            pass

    def reducer(self, key, values):
        try:
            X = []
            y = []

            for value_type, indicator, predictors in values:
                if value_type == 'data':
                    # Process data records
                    # Add predictors to X and indicator to y
                    X.append(list(map(float, predictors)))
                    y.append(indicator)

            if X and y:
                # Perform linear regression using NumPy
                X = np.array(X)
                y = np.array(y)
                X_transpose = np.transpose(X)

                # Calculate coefficients (b) using the normal equation
                b = np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)

                # Now, you can use the coefficients for prediction
                predicted_indicator = X.dot(b)

                # Emit the unique key and predicted indicator as the result
                yield key, ('result', predicted_indicator.tolist())

        except Exception as e:
            # Handle any exceptions gracefully
            pass

if __name__ == '__main__':
    MyMRJob.run()
