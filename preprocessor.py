import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

# Preprocessor class, will be used to preprocess the data for models
class Preprocessor:
    def __init__(self, data : pd.DataFrame, columns : list):
        """
        Constructor, initializes the data attribute with the dataset we're preprocessing
        and the columns to grab from the dataset.
        :param data: DataFrame containing the data
        :param columns: List containing the column names to grab from dataset
        """
        self.data = data
        self.columns = columns

    def preprocess(self) -> pd.DataFrame:
        """
        Preprocesses the data from the data attribute by:
        - Converting any numerical data in mg to g
        - Using one-hot encoding to store the categorical data
        - Scaling the numerical data with StandardScaler
        :return: features dataframe
        """

        # Converting columns in mg to g
        self.data.loc[:, "sodium_g"] = self.data["sodium_mg"].div(1000, axis=0)
        self.data.loc[:, "cholesterol_g"] = self.data["cholesterol_mg"].div(1000, axis=0)

        # Grabbing the columns we need
        columns_needed = self.data[self.columns]

        # Normalizing carbs, proteins, fats, and calories by calculating how much per meal
        meal_frequencies = columns_needed["Daily meals frequency"]
        daily_nutrition = ["Carbs", "Proteins", "Fats", "Calories"]
        nutrition_per_meal = columns_needed[daily_nutrition].div(meal_frequencies, axis=0)

        # Normalizing sugar, sodium, cholesterol with serving size
        serving_sizes = columns_needed["serving_size_g"]
        nutrition = ["sugar_g", "sodium_g", "cholesterol_g"]
        nutrition_per_serving = columns_needed[nutrition].div(serving_sizes, axis=0)

        # Use one-hot encoding for categorical features (diet_type and cooking_method)
        one_hot_encoder = OneHotEncoder(sparse_output=False)
        categorical_columns = ["diet_type", "cooking_method"]
        one_hot_encoded = one_hot_encoder.fit_transform(columns_needed[categorical_columns])
        one_hot_encoded = pd.DataFrame(one_hot_encoded, columns=one_hot_encoder.get_feature_names_out(categorical_columns))

        # Combine numerical features and standardize
        features = pd.DataFrame()
        features = pd.concat([features, nutrition_per_meal, nutrition_per_serving], axis=1)
        scaler = StandardScaler()
        standardized_features = pd.DataFrame(scaler.fit_transform(features), columns=features.columns)

        # Combine standardized features with one hot encoded features
        final_features = pd.DataFrame()
        final_features = pd.concat([final_features, standardized_features, one_hot_encoded], axis=1)

        return final_features

    def get_target(self, threshold : float) -> pd.Series:
        """
        Creates the target values using the ratings column, healthy/unhealthy based on whether
        the rating meets the threshold
        :param threshold: The threshold of healthy/unhealthy
        :return: Series containing the target values
        """

        # Grab ratings column
        ratings = self.data["rating"]
        target = [] # target data

        # For each rating
        for rating in ratings:
            # If it meets the threshold, label it healthy
            if rating > threshold:
                target.append("Healthy")
            # If it doesn't meet the threshold, label it unhealthy
            else:
                target.append("Unhealthy")

        # Convert to Series
        target = pd.Series(target)

        return target

    def get_meal_names(self) -> pd.Series:
        """
        Returns the name of each meal, used as an ID for each observation
        :return: Series that contains each meal name
        """
        return self.data["meal_name"]
