# main.py
import pandas as pd
from consts import thresholds,FEATURE_NAMES
from standardizer import Standardizer
from labeler import Labeler

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from NN import NN
from RF import RF
from KNN import KNN





def main():
    

    #assunmes directory of pwd -> files -> FOOD-DATA-GROUP{1,2,3,4,5}.csv

    df1 = pd.read_csv("Files/FOOD-DATA-GROUP1.csv")
    df2 = pd.read_csv("Files/FOOD-DATA-GROUP2.csv")
    df3 = pd.read_csv("Files/FOOD-DATA-GROUP3.csv")
    df4 = pd.read_csv("Files/FOOD-DATA-GROUP4.csv")
    df5 = pd.read_csv("Files/FOOD-DATA-GROUP5.csv")


    df = pd.concat([df1,df2,df3,df4,df5], ignore_index=True)


    #swapcols to densities. 
    std = Standardizer()
    df = std.standardize(df)


    #label densities. 
    L = Labeler(thresholds)
    df = L.label(df)

    features = df[FEATURE_NAMES]
    target = df["Health_Label"]

    xtrain, xtest, ytrain, ytest = train_test_split(
        features, target,
        train_size=0.7,
        test_size=0.3,
        stratify=target, #get binary classification split 
        random_state=42
    )


    #SCALE DATA HERE 
    scaler = StandardScaler()
    xtrain = scaler.fit_transform(xtrain)
    xtest = scaler.transform(xtest)
    #do not need to encode because of model design. 
    
    #MODELS

    Model1 = NN()
    Model2 = KNN(k=7)
    Model3 = RF()

    Model1.train(xtrain, ytrain)
    Model2.train(xtrain, ytrain)
    Model3.train(xtrain, ytrain)

    print("Training models:")
    print("\n=== Neural Network Accuracy ===")
    predictionsNN = Model1.predict(xtest)
    print(Model1.accuracy(ytest, predictionsNN))

    print("\n=== KNN Accuracy ===")
    predictionsKNN = Model2.predict(xtest)
    print(Model2.accuracy(ytest, predictionsKNN))

    print("\n=== Random Forest Accuracy ===")
    predictionsRF = Model3.predict(xtest)
    print(Model3.accuracy(ytest, predictionsRF))


main()
