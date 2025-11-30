from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (accuracy_score, f1_score, precision_score, recall_score,
                             confusion_matrix, ConfusionMatrixDisplay, RocCurveDisplay)
import matplotlib.pyplot as plt

#WRAPPER CLASS FOR NN
class NN: 
    def __init__(self):
        """Constructor to initialize the model."""
        self.model = MLPClassifier(hidden_layer_sizes=(10,10,10,10), activation = 'relu', solver='adam', max_iter=2000,random_state=42)

    def train(self,features,target_train):
        """
        Trains the model
        :param features: The feature data that the model will be trained on.
        :param target_train: The target data that the model will be trained on.
        :return: The trainined model
        """
        self.model.fit(features, target_train)
        return self.model 
    

    def predict(self, xtest):
        """
        Creates the predictions based on the trained model.
        :param xtest: The feature data that will be fed into the model to create the predictions.
        :return: The predictions created by the model.
        """
        predictions = self.model.predict(xtest)
        return predictions

    def performance_metrics(self, ytest, predictions):
        """
        Calculates the performance metrics based on the model's predictions.
        :param ytest: The correct values.
        :param predictions: The predictions created by the model.
        :return: accuracy score, f1 score, precision score, and recall score
        """
        return (accuracy_score(ytest, predictions),
                f1_score(ytest, predictions, pos_label="Healthy"),
                precision_score(ytest, predictions, pos_label="Healthy"),
                recall_score(ytest, predictions, pos_label="Healthy"))

    def confusion_matrix(self, ytest, predictions):
        """
        Calculates the confusion matrix based on the model's predictions. Prints a basic
        confusion matrix to the terminal and also creates a pretty display of the confusion
        matrix using matplotlib.
        :param ytest: The correct values.
        :param predictions: The predictions created by the model.
        :return: None
        """
        cm = confusion_matrix(ytest, predictions, labels=["Unhealthy", "Healthy"])
        print(f"Confusion Matrix:\n {cm}")
        cm_disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Unhealthy", "Healthy"])
        cm_disp.plot()
        plt.title("Neural Network")
        plt.show()

    def roc_curve(self, xtest, ytest):
        """
        Calculates and plots the ROC curve.
        :param xtest: The feature data that corresponds to the correct target values,
        used to get the predicted probabilities.
        :param ytest: The correct values.
        :return: None
        """
        # Get predicted probabilities for positive class
        y_probabilities = self.model.predict_proba(xtest)
        y_probabilities = y_probabilities[:, 0]

        RocCurveDisplay.from_predictions(ytest, y_probabilities, pos_label="Healthy")
        plt.plot([0, 1], [0, 1], linestyle='--')
        plt.title("Neural Network")
        plt.show()

    def blank_cpy(self): 
        return NN()
