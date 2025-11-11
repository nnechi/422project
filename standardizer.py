import pandas as pd
import os
from consts import feature_names

def standardize(df) -> pd.DataFrame:
    """
    Standardizes the given DataFrame by dividing each nutrition value
    by the number of calories, to calculate the density of each value.
    This will be used to measure whether a food item is healthy or not.

    Returns: Pandas DataFrame
    """

    # Features of the new standardized dataframe
    new_feature_names = ["Food", "Calories", "Fat Density", "Saturated Fats Density",
                         "Monounsaturated Fats Density", "Polyunsaturated Fats Density",
                         "Carbohydrates Density", "Sugars Density", "Protein Density",
                         "Dietary Fiber Density", "Cholesterol Density", "Sodium Density",
                         "Water Density", "Vitamin A Density", "Vitamin B1 Density", "Vitamin B11 Density",
                         "Vitamin B12 Density", "Vitamin B2 Density", "Vitamin B3 Density",
                         "Vitamin B5 Density", "Vitamin B6 Density", "Vitamin C Density", "Vitamin D Density",
                         "Vitamin E Density", "Vitamin K Density", "Calcium Density", "Copper Density",
                         "Iron Density", "Magnesium Density", "Manganese Density", "Phosphorus Density",
                         "Potassium Density", "Selenium Density", "Zinc Density"]

    standardized_df = pd.DataFrame(columns=new_feature_names)

    # For every food in the dataset
    for row in df.iterrows():
        # Represents the new row that'll be put into standardized_df
        new_row = []
        # Number of calories of the current food item
        num_calories = 0

        # For every index, value pair of that food
        # index = column name
        # value = the actual value at that column
        for index, value in row[1].items():
            # If the current column is the "food" column, no calculations required
            # Just add the food name to the new row
            if index == "food":
                new_row.append(value)

            # If the current column is the "Caloric Value" column, no calculations required
            # Just add the calories to the new row and save the current number of calories
            elif index == "Caloric Value":
                new_row.append(value)
                num_calories = value

            # Else, need to calculate the density
            else:
                # If calories > 0, then we can calculate density
                if num_calories > 0:
                    new_value = value / num_calories
                    new_row.append(new_value)

                # If calories <= 0, then we can't calculate density (b/c of division by 0)
                # Instead, create an arbitrarily high number to represent a high density
                else:
                    new_row.append(value * 100)

        # Add new row to standardized_df
        standardized_df.loc[row[0]] = new_row

    return standardized_df


def main():
    """Main function to standardize each dataset."""
    # Get the path to the files folder
    path = os.path.join(os.getcwd(), "Files")

    # Create a new folder to put the standardized files in
    os.makedirs("Standardized Files", exist_ok=True)

    # For every food dataset csv
    for i in range(1,6):
        # Get the path of the current dataset csv we're working on
        file = os.path.join(path, "FOOD-DATA-GROUP" + str(i) + ".csv")

        # Read the csv and store in a DataFrame
        df = pd.read_csv(file)

        # Clean up the DataFrame by removing unnecessary columns
        # i.e. "Unnamed: 0", "ID", "Nutrition Density"
        df = df.drop(columns=feature_names[1], axis=1) # Unnamed: 0
        df = df.drop(df.columns[0], axis=1) # ID
        df = df.drop("Nutrition Density", axis=1) # Nutrition Density

        # Standardize the current DF and create a csv of the DF, store in "Standardized Files" folder
        standardized_df = standardize(df)
        new_path = os.path.join(os.getcwd(), "Standardized Files/")
        csv_name = "standardized_data" + str(i) + ".csv"
        standardized_df.to_csv(new_path + csv_name, index=False)

# Call main
main()