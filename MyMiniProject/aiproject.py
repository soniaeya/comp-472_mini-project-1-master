# Load libraries
import pandas as pd
from sklearn import tree # Import Decision Tree Classifier
from sklearn import preprocessing #to turn strings into numbers
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import numpy as np

import matplotlib.pyplot as plt

from six import StringIO
from IPython.display import Image
import pydotplus


col_names = ['alt', 'bar', 'fri', 'hun', 'pat', 'price', 'rain', 'res', 'type','est', 'willwait']
# load dataset
dataset = pd.read_csv("training_data.csv", header=None, names=col_names)
df_test = pd.DataFrame(dataset, columns=col_names)
df = df_test.drop(0, axis=0)

df.index = ['1','2','3','4','5','6','7','8','9','10','11','12']
print(df)
X_col = df.drop('willwait', axis=1)

#split dataset in features and target variable
feature_cols = ['alt', 'bar', 'fri', 'hun','pat','price','rain','res','type','est']
X = X_col # Features
y = df['willwait'] # Target variable

le = preprocessing.LabelEncoder()
X = X.apply(le.fit_transform)
y = le.fit_transform(y)



# Create Decision Tree classifer object
clf = tree.DecisionTreeClassifier(criterion='entropy', random_state=2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.001, random_state=0) # 80% training and 20% test
# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset

#print("Printing X_test: \n", X_test)
#[[1,0,1,1,0,0,1,0,2,0]]
y_pred = clf.predict(X_train)

print("Predicted output: ", le.inverse_transform(y_pred))

#print("Accuracy:",metrics.accuracy_score([[1,0,1,1,0,0,1,0,3,0]], y_pred))

plt.figure(figsize=(12,6))
tree.plot_tree(clf, feature_names=feature_cols, class_names=['No','Willwait'], filled=True,rounded=True)

plt.show()

dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True,
                feature_names = feature_cols,
                class_names=le.classes_)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

graph.write_png('trainingdata.png')
Image(graph.create_png())