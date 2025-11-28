import sys 
import os 
import numpy as np 
import pandas as pd 
import tensorflow as tf 
from tensorflow.keras import layers, models, optimizers

class NN: 
    def __init__(self, features, target): 
        pass

    def train(self,features,target): 
        
        model = keras.Sequential(
            [ 
                layers.Dense(5, activation = 'relu', name = 'layer1'),
                layers.Dense(6, activation = 'relu', name = 'layer2'),
                layers.Dense(3, activation = 'relu', name = 'layer3'),
                layers.Dense(1, activation='sigmoid', name = 'output')
            ]
        )
        

        model.compile(
            optimizer = 'sgd', 
            loss =- 'binarycrossentropy',
            metrics = ['accuracy']
        )

        model.fit(self.features, self.target, epochs = 50)


        return model
    

    def predict(self, xtest): 


