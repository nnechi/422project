import sys
import os 
import numpy as np 
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier

class RandomForest: 
    def __init__(self): 
        self.model = RandomForestClassifier(n_estimators=60, max_depth=None, random_state=42)

    def train(self, xtrain, ytrain): 
        self.model.fit(xtrain, ytrain)
    
    def predict(self, xtest): 
        return self.model.predict(xtest)
    
    def accuracy(self, xtest, ytest): 
        return self.model.score(xtest, ytest)
    