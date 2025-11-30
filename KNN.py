import sys 
import os 
import pandas as pd 
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score


#WRAPPER CLASS FOR KNN MODEL

class KNN: 
    def __init__(self, k): 
        self.k = k 
        self.model = KNeighborsClassifier(n_neighbors = k)


    def train(self,features, ftargets): 
        self.model.fit(features,ftargets)


    def predict(self, xtest): 
        predictions = self.model.predict(xtest) 
        return predictions
    
    def accuracy(self, ytest, predictions): 
        accuracy = accuracy_score(ytest, predictions)
        return accuracy
    


    