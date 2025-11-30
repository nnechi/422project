import sys 
import os 
import numpy as np 
import pandas as pd 
from sklearn.neural_network import MLPClassifier 
from sklearn.metrics import accuracy_score

#WRAPPER CLASS FOR NN 

class NN: 
    def __init__(self): 
        self.model = MLPClassifier(hidden_layer_sizes=(10,10,10,10), activation = 'relu', solver='adam', max_iter=2000,random_state=42)

    def train(self,features,target_train): 
        self.model.fit(features, target_train)
        return self.model 
    

    def predict(self, xtest):

        predictions = self.model.predict(xtest)
        return predictions
    
    def accuracy(self, ytest, predictions): 
        return accuracy_score(ytest, predictions)
    



