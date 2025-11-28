import pandas as pd
import os
from consts import thresholds
from standardizer import Standardizer
from labeler import Labeler
from preprocessor import Preprocessor

def main():
    # Read every food nutrition csv and put into a dataframe
    df1 = pd.read_csv('Files/FOOD-DATA-GROUP1.csv')
    df2 = pd.read_csv('Files/FOOD-DATA-GROUP2.csv')
    df3 = pd.read_csv('Files/FOOD-DATA-GROUP3.csv')
    df4 = pd.read_csv('Files/FOOD-DATA-GROUP4.csv')
    df5 = pd.read_csv('Files/FOOD-DATA-GROUP5.csv')

    # Standardize every data set by using densities
    std = Standardizer()
    df1 = std.standardize(df1, 'standardized_data1.csv')
    df2 = std.standardize(df2, 'standardized_data2.csv')
    df3 = std.standardize(df3, 'standardized_data3.csv')
    df4 = std.standardize(df4, 'standardized_data4.csv')
    df5 = std.standardize(df5, 'standardized_data5.csv')

    # Add two new labels to every observation, health label (healthy/not healthy) and health score
    l = Labeler(thresholds)
    df1 = l.label(df1)
    df2 = l.label(df2)
    df3 = l.label(df3)
    df4 = l.label(df4)
    df5 = l.label(df5)

    print("Labeler has logged status in logger.txt.")

    # Create csv files of the DFs with labels, and save to its own folder
    os.makedirs("Labeled_Files", exist_ok=True)

    df1.to_csv("Labeled_Files/df1.csv", index=False)
    df2.to_csv("Labeled_Files/df2.csv", index=False)
    df3.to_csv("Labeled_Files/df3.csv", index=False)
    df4.to_csv("Labeled_Files/df4.csv", index=False)
    df5.to_csv("Labeled_Files/df5.csv", index=False)

    # Read in lifestyle data into df
    data = pd.read_csv("Files/meal_metadata.csv")

    # Create preprocessor to process the data
    columns = ["Daily meals frequency", "Carbs", "Proteins", "Fats", "Calories", "meal_name",
               "diet_type", "sugar_g", "sodium_g", "cholesterol_g", "serving_size_g",
               "cooking_method", "rating"]
    preprocessor = Preprocessor(data, columns)
    features = preprocessor.preprocess() # features used by model
    target = preprocessor.get_target(2.5) # target used by model
    meal_names = preprocessor.get_meal_names() # meal names, used as ID for each observation

main()