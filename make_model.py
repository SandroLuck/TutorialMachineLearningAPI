"""
This file generates and selects a suitable classifier for our question.
We will use the trained classifier to implement out API
"""
import pandas as pd
from joblib import dump
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier

# load data
df = pd.read_csv("data/titanic_train.csv")
y = df["survived"]

# These can all be used with decision trees and they make sense.
# Be careful if using some other features, may need to be transformed differently
# Also think about NaN values
X = df[["sex", "pclass"]].copy()
X.loc[:, "sex"] = X['sex'].apply(lambda gender_str: 1 if gender_str == "female" else 0)
print(X)
# train/test split, shuffle in real life
X_train = X[:int(X.shape[0] * 0.8)]
X_test = X[int(X.shape[0] * 0.8):]
y_train = y[:int(y.shape[0] * 0.8)]
y_test = y[int(y.shape[0] * 0.8):]

assert X_train.shape[0] == y_train.shape[0]

# make model
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)
print("Score:", score)
print("REPORT:\n", classification_report(y_test, clf.predict(X_test)))
# we could now retrain best_clf on all data, or do some model averaging
# we will simply store it however
dump(clf, "./model_weights/clf.bin")
