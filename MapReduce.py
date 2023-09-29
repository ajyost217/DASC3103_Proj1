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
            # Collect the data for linear regression
            X = []  # Predictor variables
            y = []  # Indicator variable

            for value_type, indicator, predictors in values:
                if value_type == 'data':
                    X.append(predictors)
                    y.append(indicator)

            if X and y:
                X = np.array(X, dtype=float)
                y = np.array(y, dtype=float)

                # Perform linear regression
                coefficients = np.linalg.lstsq(X, y, rcond=None)[0]

                # Predict the indicator variable
                predicted_indicator = np.dot(X[0], coefficients)

                # Emit the result
                yield key, ('result', predicted_indicator, list(coefficients))

        except Exception as e:
            # Handle any exceptions gracefully
            pass

if __name__ == '__main__':
    MyMRJob.run()
