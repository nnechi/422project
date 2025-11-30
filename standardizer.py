# standardizer.py

vitaminColumns = [
            "Vitamin A", "Vitamin B1", "Vitamin B11", "Vitamin B12",
            "Vitamin B2", "Vitamin B3", "Vitamin B5", "Vitamin B6",
            "Vitamin C", "Vitamin D", "Vitamin E", "Vitamin K"
            ]

densities = {
            "Fat": "Fat_Density",
            "Saturated Fats": "Saturated_Fats_Density",
            "Monounsaturated Fats": "Monounsaturated_Fats_Density",
            "Polyunsaturated Fats": "Polyunsaturated_Fats_Density",
            "Carbohydrates": "Carbohydrates_Density",
            "Sugars": "Sugars_Density",
            "Protein": "Protein_Density",
            "Dietary Fiber": "Dietary_Fiber_Density",
            "Cholesterol": "Cholesterol_Density",
            "Sodium": "Sodium_Density",
            }

class Standardizer:
    def __init__(self):
       pass
        
    def standardize(self, df):
        df = df.copy()

        df = df.fillna(0)
        df["Caloric Value"] = df["Caloric Value"].replace(0, 1)

        cal = df["Caloric Value"]

        for item, item_density in densities.items():
            df[item_density] = df[item] / cal

        df["Total_Vitamin_Density"] = df[vitaminColumns].sum(axis=1) / cal

        df = df.fillna(0)

        return df