
import logging
import os
import json
import traceback
import sys

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import numpy as np
from joblib import dump, load

data_path = 'data/'
model_file_name = 'svm.dump'
model_path = os.path.join("model", model_file_name)
X_train_path = os.path.join(data_path, "train/X_train.csv")
X_test_path = os.path.join(data_path, "test/X_test.csv")
y_train_path = os.path.join(data_path, "train/y_train.csv")
y_test_path = os.path.join(data_path, "test/y_test.csv")


# The function to execute the training.
def train():
    print('Starting the training...')
    ## Read data
    X_train = np.genfromtxt(X_train_path, delimiter=',')
    y_train = np.genfromtxt(y_train_path, delimiter=',')
    X_test = np.genfromtxt(X_test_path, delimiter=',')
    y_test = np.genfromtxt(y_test_path, delimiter=',')
    # define and train model
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)

    # print abs error
    print('validating model...')
    y_pred = model.predict(X_test)
    print("Accuracy: ", accuracy_score(y_pred, y_test))

    # persist model
    print('saving model file to {}'.format(model_path))
    dump(model, model_path) 
    print('Training complete.')

if __name__ == '__main__':
    train()