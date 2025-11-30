# main.py
import pandas as pd
import numpy as np 
from consts import thresholds,FEATURE_NAMES
from standardizer import Standardizer
from labeler import Labeler
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.utils import resample 
from NN import NN
from RF import RF
from KNN import KNN


def KFoldCV(name_of_model, m, features, target, k):
    """K-Fold Cross Validation for each model. """
    
    print(f"====Starting Cross Validation for {name_of_model}====")
    kfold = KFold(n_splits=k, shuffle=True, random_state=42)
    scores = []
    for train, test in kfold.split(features):
        metrics = []  
        xtrain, xtest = features.iloc[train], features.iloc[test]
        ytrain, ytest = target.iloc[train], target.iloc[test]
        model = m.blank_cpy()
        model.train(xtrain, ytrain)
        yhat = model.predict(xtest)
        accuracy_NN, f1_NN, precision_NN, recall_NN = model.performance_metrics(ytest, yhat)
        metrics.append(f"{accuracy_NN:.8f}")
        metrics.append(f"{f1_NN:.8f}")
        metrics.append(f"{precision_NN:.8f}")
        metrics.append(f"{recall_NN:.8f}")
        scores.append(metrics)
        

        
    KFoldRes(name_of_model, scores)

def KFoldRes(name_of_model, KFScores): 
    i = 1
    print("Fold #:           Accuracy       F1            Precision       Recall")
    for score in KFScores: 
        print(f"Fold{i}: Metrics = {score}")
        i+=1 
    print("========================================\n")



def bootstrapEval(name_of_model, m, features, target, iterations):
    """Bootstrapping procedure for each model."""

    print(f"Starting Bootstrap Evaluations for {name_of_model}")
    BSscores = [] 

    for iteration in range(iterations):
        #grab bootstrap samples 
        BSFeatures, BSTargets = resample(features, target, replace = True)

        OOB = ~features.index.isin(BSFeatures.index)
        OOBFeatures = features[OOB]
        OOBTargets = target[OOB]
         
        if len(OOB) == 0:
            continue 
        model = m.blank_cpy() 
        model.train(BSFeatures, BSTargets)

        yhat = model.predict(OOBFeatures)

        BSscores.append(accuracy_score(OOBTargets, yhat))

    bootstrapRes(name_of_model, BSscores)

def bootstrapRes(name_of_model, BSscores):
    scores = np.array(BSscores)

    mean = scores.mean()
    std = scores.std()
    ci_lower = np.percentile(scores, 2.5)
    ci_upper = np.percentile(scores, 97.5)
    median = np.median(scores)
    iqr = np.percentile(scores, 75) - np.percentile(scores, 25)

    print(f"\n====Bootstrap Evaluation {name_of_model}====")
    print(f"Mean Accuracy:        {mean:.8f}")
    print(f"Std Deviation:        {std:.8f}")
    print(f"95% CI:               [{ci_lower:.8f}, {ci_upper:.8f}]")
    print(f"Median:               {median:.8f}")
    print(f"IQR:                  {iqr:.8f}")
    print("========================================\n")
    



def main():
    """Driver code to create, train, and evaluate the 3 models."""

    # Reads in the datasets from all 5 files
    # Assumes the directory of current directory -> Files -> FOOD-DATA-GROUP{1,2,3,4,5}.csv
    df1 = pd.read_csv("Files/FOOD-DATA-GROUP1.csv")
    df2 = pd.read_csv("Files/FOOD-DATA-GROUP2.csv")
    df3 = pd.read_csv("Files/FOOD-DATA-GROUP3.csv")
    df4 = pd.read_csv("Files/FOOD-DATA-GROUP4.csv")
    df5 = pd.read_csv("Files/FOOD-DATA-GROUP5.csv")

    # Combines the 5 DataFrames into a single DataFrame
    df = pd.concat([df1,df2,df3,df4,df5], ignore_index=True)

    # Uses standardizer to convert all nutritional values to densities
    std = Standardizer()
    df = std.standardize(df)

    # Uses Labeler to label each food as healthy or unhealthy
    # These labels will be used as the ground truth values for our models to compare to
    L = Labeler(thresholds)
    df = L.label(df)

    # Pull out features and target
    features = df[FEATURE_NAMES]
    target = df["Health_Label"]

    # Split data into training set and testing set
    xtrain, xtest, ytrain, ytest = train_test_split(
        features, target,
        train_size=0.7,
        test_size=0.3,
        stratify=target, #get binary classification split 
        random_state=42
    )

    # Scales the features using StandardScaler
    # Encoding not required because of model design
    scaler = StandardScaler()
    xtrain = scaler.fit_transform(xtrain)
    xtest = scaler.transform(xtest)

    # Creating the models we're testing
    Model1 = NN() # Neural network
    Model2 = KNN(k=7) # k-NN
    Model3 = RF() # Random forest

    # Training the models
    Model1.train(xtrain, ytrain)
    Model2.train(xtrain, ytrain)
    Model3.train(xtrain, ytrain)

    print("Training models:")

    # Evaluating each model's performance
    # Neural network metrics
    predictionsNN = Model1.predict(xtest)
    accuracy_NN, f1_NN, precision_NN, recall_NN = Model1.performance_metrics(ytest, predictionsNN)
    print("\n=== Neural Network===")
    print(f"Accuracy: {accuracy_NN}")
    print(f"F1 score: {f1_NN}")
    print(f"Precision: {precision_NN}")
    print(f"Recall: {recall_NN}")
    Model1.confusion_matrix(ytest, predictionsNN)
    Model1.roc_curve(xtest, ytest)

    # k-NN metrics
    predictionsKNN = Model2.predict(xtest)
    accuracy_KNN, f1_KNN, precision_KNN, recall_KNN = Model2.performance_metrics(ytest, predictionsKNN)
    print("\n=== k-NN ===")
    print(f"Accuracy: {accuracy_KNN}")
    print(f"F1 score: {f1_KNN}")
    print(f"Precision: {precision_KNN}")
    print(f"Recall: {recall_KNN}")
    Model2.confusion_matrix(ytest, predictionsKNN)
    Model2.roc_curve(xtest, ytest)

    # Random forest metrics
    predictionsRF = Model3.predict(xtest)
    accuracy_RF, f1_RF, precision_RF, recall_RF = Model3.performance_metrics(ytest, predictionsRF)
    print("\n=== Random Forest===")
    print(f"Accuracy: {accuracy_RF}")
    print(f"F1 score: {f1_RF}")
    print(f"Precision: {precision_RF}")
    print(f"Recall: {recall_RF}")
    Model3.confusion_matrix(ytest, predictionsRF)
    Model3.roc_curve(xtest, ytest)


    #Use KFold Method Above. 
    print("Cross Validation: ")

    KFoldCV("Neural Network", Model1, features, target, 10)
    KFoldCV("K-Nearest Neighbors", Model2, features, target, 10)
    KFoldCV("Random Forest", Model3, features, target, 10)  

    #Bootstrap Eval     


    bootstrapEval("Neural Network", Model1, features, target, 200)    
    bootstrapEval("K-Nearest Neighbors", Model2, features, target, 200)
    bootstrapEval("Random Forest", Model3, features, target, 200)





main()
