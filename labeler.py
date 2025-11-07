import numpy as np 
import pandas as pd 
import sys 
import os 
from consts import thresholds, feature_names

#Labels data based off given instructions 

f = open('out.txt','+w')


class Labeler: 
    def __init__(self, thresholds : dict): 
        self.criteria = thresholds
        

#Take in a dataframe and label it accordingly with unhealthy/healthy according to given criteria. 
    def label(self, frame: pd.DataFrame) -> pd.DataFrame:



        labels = []

        cols = frame.columns.str.replace(' ', '_')
        frame.columns = cols


        for row in frame.itertuples(index=False):

            #pull features using getattr
            calories = getattr(row, "Caloric_Value", 0)
            fat = getattr(row, "Fat", 0)
            sat_fat = getattr(row, "Saturated_Fats", 0)
            mon_fat = getattr(row, "Monounsaturated_Fats", 0)
            poly_fat = getattr(row, "Polyunsaturated_Fats", 0)
            carbs = getattr(row, "Carbohydrates", 0)
            sugars = getattr(row, "Sugars", 0)
            protein = getattr(row, "Protein", 0)
            fiber = getattr(row, "Dietary_Fiber", 0)
            cholesterol = getattr(row, "Cholesterol", 0)
            sodium = getattr(row, "Sodium", 0)
            water = getattr(row, "Water", 0)
            density = getattr(row, "Nutrition_Density", 0)

            vals = [getattr(row,f'food'), calories,fat,sat_fat, mon_fat,poly_fat,carbs,sugars,protein,fiber,cholesterol,sodium,water,density]

            
         
            if (self.test(vals)):
                f.write(f"{getattr(row,'food')} is healthy.\n")
                labels.append("Healthy")
            else:
                f.write(f"{getattr(row,'food')} is unhealthy.\n")
                labels.append("Unhealthy")

        # Add as new column
        frame['Health_Label'] = labels
        print(f"✅ Added Health_Label column ({len(labels)} entries)")
        return frame

    def test(self, values) ->  bool  :
        i =1
        score = 0
        test_order = ["Caloric_Value", "Fat", "Saturated_Fats", "Monounsaturated_Fats", "Polyunsaturated_Fats", "Carbohydrates", "Sugars", "Protein", "Dietary_Fiber", "Cholesterol", "Sodium", "Water", "Nutrition_Density"]
        for test in test_order: 
            v = values[i]
            thresh = self.criteria[test]
            op = thresh[0]
            val = thresh[1]


            f.write(f"V:{v}, Val:{val} for {values[0]}\n")
            if op == '<': 
                if (v < val): 
                    f.write('+1\n')
                    score += thresh[2]
            elif op == '>':
                if (v > val): 
                    f.write('+1\n')
                    score += thresh[2]

            i+=1

        
        f.write(f"Score for: {values[0]}: {score}\n")
        print()
        return score >= 17
            
            
 



#lil demo main for the selections (final project -> [Files[datasets], labeler.py])
def main(): 
    path = os.path.join(os.getcwd(), "Files")
    
    p = input("Specify file.csv\n")  

    filename = f"FOOD-DATA-GROUP{p}.csv"
    
    df = pd.read_csv(os.path.join(path,filename))


    print(df.head())


    print("Columns:")
    print(df.columns)
    print("Rows:")
    print(df.index)

    #The labeler needs to be able to determine whether a given food is healthy or not. We will then use this data to train a binary classifier on supervised learning like knn, and use that to predict the user's eating habits. 

    L = Labeler(thresholds)
    df = L.label(df)

    print(df.head())
    print(df.columns)
    df.to_csv("full_dataframe_output.csv", index=False)
    print("✅ Full DataFrame saved to full_dataframe_output.csv")


main()







