import numpy as np 
import pandas as pd 
import sys 
import os 
from consts import thresholds
from standardizer import Standardizer

#Labels data based off given instructions 

f = open('logger.txt','+w') #debug log. 


class Labeler: 
    def __init__(self, thresholds : dict): 
        self.criteria = thresholds
        

#Take in a dataframe and label it accordingly with unhealthy/healthy according to given criteria. 
    def label(self, frame: pd.DataFrame) -> pd.DataFrame:


        f.write(f"\nStarting new frame log.\n")

        labels = []
        scores = []



        for row in frame.itertuples(index=False):

            #pull features using getattr
            fat = getattr(row, "Fat_Density", 0)
            sat_fat = getattr(row, "Saturated_Fats_Density", 0)
            mon_fat = getattr(row, "Monounsaturated_Fats_Density", 0)
            poly_fat = getattr(row, "Polyunsaturated_Fats_Density", 0)
            carbs = getattr(row, "Carbohydrates_Density", 0)
            sugars = getattr(row, "Sugars_Density", 0)
            protein = getattr(row, "Protein_Density", 0)
            fiber = getattr(row, "Dietary_Fiber_Density", 0)
            cholesterol = getattr(row, "Cholesterol_Density", 0)
            sodium = getattr(row, "Sodium_Density", 0)
            total_vitamin = getattr(row, "Total_Vitamin_Density", 0)



            vals = [getattr(row,f'food'), fat,sat_fat, mon_fat,poly_fat,carbs,sugars,protein,fiber,cholesterol,sodium, total_vitamin]

            
            res, score = self.test(vals)
            if (res):
                f.write(f"{getattr(row,'food')} is healthy.\n\n")
                labels.append("Healthy")
                
            else:
                f.write(f"{getattr(row,'food')} is unhealthy.\n\n")
                labels.append("Unhealthy")
            scores.append(score)
        # Add as new column
        frame['Health_Label'] = labels
        print(f"Added Health_Label column ({len(labels)} entries)")
        frame['Health_Score'] = scores
        print(f"Added Health_Score column ({len(scores)}) entries")
        return frame

    def test(self, values) ->  {bool,int}  :
        i =1
        score = 0
        test_order = [
            "Fat_Density",
            "Saturated_Fats_Density",
            "Monounsaturated_Fats_Density",
            "Polyunsaturated_Fats_Density",
            "Carbohydrates_Density",
            "Sugars_Density",
            "Protein_Density",
            "Dietary_Fiber_Density",
            "Cholesterol_Density",
            "Sodium_Density",
            "Total_Vitamin_Density"
        ]
        for test in test_order: 
            v = values[i]
            thresh = self.criteria[test]
            op = thresh[0]
            val = thresh[1]


            f.write(f"Testing: {test} V:{v}, Val:{val} for {values[0]}\n")
            if op == '<': 
                if (v < val): 
                    f.write(f'+{thresh[2]}\n')
                    score += thresh[2]
                else:
                    f.write(f'-{thresh[3]}\n')
                    score -= thresh[3]
            elif op == '>':
                if (v > val): 
                    f.write(f'+{thresh[2]}\n')
                    score += thresh[2]
                else:
                    f.write(f'-{thresh[3]}\n')
                    score -= thresh[3]

            i+=1

        
        f.write(f"Score for: {values[0]}: {score}\n")
        print()
        res = score >= 3#??? here need to set cutoff
        return res,score
            
            
 



#lil demo main for the selections (final project -> [Files[datasets], labeler.py])
def main(): 


    df1 = pd.read_csv('Files/FOOD-DATA-GROUP1.csv')
    df2 = pd.read_csv('Files/FOOD-DATA-GROUP2.csv')
    df3 = pd.read_csv('Files/FOOD-DATA-GROUP3.csv')
    df4 = pd.read_csv('Files/FOOD-DATA-GROUP4.csv')
    df5 = pd.read_csv('Files/FOOD-DATA-GROUP5.csv')


    #The labeler needs to be able to determine whether a given food is healthy or not. We will then use this data to train a binary classifier on supervised learning like knn, and use that to predict the user's eating habits. 

    STD = Standardizer()
    df1 = STD.standardize(df1, 'standardized_data1.csv')
    df2 = STD.standardize(df2, 'standardized_data2.csv')
    df3 = STD.standardize(df3, 'standardized_data3.csv')
    df4 = STD.standardize(df4, 'standardized_data4.csv')
    df5 = STD.standardize(df5, 'standardized_data5.csv')

    L = Labeler(thresholds)
    df1 = L.label(df1)
    df2 = L.label(df2)
    df3 = L.label(df3)
    df4 = L.label(df4)
    df5 = L.label(df5)


    print("Labeler has logged status in logger.txt.")

    os.makedirs("Labeled_Files", exist_ok=True)

    df1.to_csv("Labeled_Files/df1.csv", index=False)
    df2.to_csv("Labeled_Files/df2.csv", index=False)
    df3.to_csv("Labeled_Files/df3.csv", index=False)
    df4.to_csv("Labeled_Files/df4.csv", index=False)
    df5.to_csv("Labeled_Files/df5.csv", index=False)



main()







