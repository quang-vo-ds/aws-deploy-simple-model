import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

data = load_iris()
X = data['data']
y = data['target']
## Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

## Save data
if not os.path.exists("data/train"):
    os.makedirs("data/train")
if not os.path.exists("data/test"):
    os.makedirs("data/test")

np.savetxt("data/train/X_train.csv", X_train, delimiter=',', header=",".join(data.feature_names))
np.savetxt("data/test/X_test.csv", X_test, delimiter=',', header=",".join(data.feature_names))
np.savetxt("data/train/y_train.csv", y_train, delimiter=',', header="label")
np.savetxt("data/test/y_test.csv", y_test, delimiter=',', header="label")