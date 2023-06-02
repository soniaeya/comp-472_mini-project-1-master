import numpy as np
from sklearn import tree
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd

dataset = np.array([
    ['sunny', 85, 85, 0, "Don't Play"],
    ['sunny', 80, 90, 1, "Don't Play"],
    ['overcast', 83, 78, 0, 'Play'],
    ['rain', 70, 96, 0, 'Play'],
    ['rain', 68, 80, 0, 'Play'],
    ['rain', 65, 70, 1, "Don't Play"],
    ['overcast', 64, 65, 1, 'Play'],
    ['sunny', 72, 95, 0, "Don't Play"],
    ['sunny', 69, 70, 0, 'Play'],
    ['rain', 75, 80, 0, 'Play'],
    ['sunny', 75, 70, 1, 'Play'],
    ['overcast', 72, 90, 1, 'Play'],
    ['overcast', 81, 75, 0, 'Play'],
    ['rain', 71, 80, 1, "Don't Play"],
])

df2 = pd.DataFrame(dataset,
                   columns=['Outlook', 'Temperature', 'Humidity', 'Windy', 'Play / Don’t Play'])
blankIndex = [''] * len(df2)
df2.index = blankIndex
df2

X = dataset[:, 0:4]
print(X)
y = dataset[:, 4]
# print(y)

le = preprocessing.LabelEncoder()
X[:, 0] = le.fit_transform(X[:, 0])
y = le.fit_transform(y)
print(X[:, 0])
# print(y)

dtc = tree.DecisionTreeClassifier(criterion="entropy")
dtc.fit(X, y)

fig, ax = plt.subplots(figsize=(12, 8))
tree.plot_tree(dtc, feature_names=['Outlook', 'Temperature', 'Humidity', 'Windy'], class_names=le.classes_,
               filled=True, rounded=True, ax=ax)
plt.show()
