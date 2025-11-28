import sys 
import os 
import pandas as pd 
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier 

class KNN: 
    def __init__(self, k): 
        self.k =k 
        self.model = KNeighborsClassifier(n_neighbors = k)


    def train(self,features, ftargets): 
        self.model.fit(features,ftargets)


    def predict(self, xtest): 
        return self.model.predict(xtest) 

    def accuracy(self, xtest, ytest): 
        return self.model.score(xtest, ytest)
    


    