import pandas as pd
import os
from consts import feature_names

# Main function that standardizes each file
def main():
    # Get the path to the files folder
    path = os.path.join(os.getcwd(), "Files")

    # For every food dataset csv
    for i in range(1,6):
        # Get the path of the current dataset csv we're working on
        file = os.path.join(path, "FOOD-DATA-GROUP" + str(i) + ".csv")

        # Read the csv and store in a DataFrame
        df = pd.read_csv(file)

        # Clean up the DataFrame by removing unnecessary columns
        # i.e. "Unnamed: 0"
        #df = df.drop(columns=feature_names[1], axis=1)

        print(df.head())
        print("\n")

# Call main
main()