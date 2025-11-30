import sys
import os 
import numpy as np 
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
class RF: 
    def __init__(self): 
        self.model = RandomForestClassifier(n_estimators=60, max_depth=None, random_state=42) #Maybe we need tro switch the n estimators here. 

    def train(self, xtrain, ytrain): 
        self.model.fit(xtrain, ytrain)
    
    def predict(self, xtest): 
        predictions = self.model.predict(xtest)
        return predictions 
    
    def accuracy(self, ytest, predictions): 
        accuracy = accuracy_score(ytest, predictions)
        return accuracy
    