import pandas as pd

# Preprocessor class, will be used to preprocess the data for models
class Preprocessor:
    # Constructor, initializes the data attribute with the dataset that we're preprocessing
    def __init__(self, data : pd.DataFrame):
        self.data = data

    def preprocess(self):
        pass