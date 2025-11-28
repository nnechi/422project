import pandas as pd
import numpy as np
import os

class Standardizer(): 
    def __init__(self):
        pass

    def std(self, df) -> pd.DataFrame:
        df = df.copy()
        df = df.drop(df.columns[:2], axis=1) 

        calories = df['Caloric Value'].replace(0, np.nan)

        nutrient_cols = df.columns.drop(['food', 'Caloric Value'])
        df_density = df[nutrient_cols].div(calories, axis=0)

        df_density.columns = [
            col if col.endswith("Density") else col + " Density"
            for col in df_density.columns
        ]


        result = pd.concat([df[['food', 'Caloric Value']], df_density], axis=1)
        result = result.fillna(0)
        result.columns = result.columns.str.replace(" ", "_")

        # Making total vitamin density column
        result["Total_Vitamin_Density"] = result[["Vitamin_A_Density", "Vitamin_B1_Density", "Vitamin_B11_Density",
                                                  "Vitamin_B12_Density", "Vitamin_B2_Density", "Vitamin_B3_Density",
                                                  "Vitamin_B5_Density", "Vitamin_B6_Density", "Vitamin_C_Density",
                                                  "Vitamin_D_Density", "Vitamin_E_Density", "Vitamin_K_Density"]].sum(axis=1)

        return result


    def standardize(self, frame : pd.DataFrame,name) -> pd.DataFrame:
        """Main function to standardize each dataset."""
        if not name.endswith(".csv"):
            name += ".csv"

        os.makedirs("Standardized_Files", exist_ok=True)
        df = frame
        df = self.std(df)
        new_path = os.path.join(os.getcwd(), f"Standardized_Files/{name}")
        df.to_csv(new_path, index=False)


        print(f"Standardized file saved to: {new_path}")

        return df
