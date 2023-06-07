# Load libraries
import pandas as pd
from sklearn import tree  # Import Decision Tree Classifier
from sklearn import preprocessing  # to turn strings into numbers
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn import metrics  # Import scikit-learn metrics module for accuracy calculation
import numpy as np

import matplotlib.pyplot as plt
def main():
    filename = input("To start, please provide the file name of your dataset?: ")
    col_names = ['alt', 'bar', 'fri', 'hun', 'pat', 'price', 'rain', 'res', 'type', 'est', 'willwait']
    # load dataset
    dataset = pd.read_csv(filename, header=None, names=col_names)
    df_test = pd.DataFrame(dataset, columns=col_names)
    df = df_test.drop(0, axis=0)

    df.index = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    print(df)
    # training_data.csv

    choice = input(
        "Please choose an option [1, 2, 3]: \n1. Specify Parameter\n2. Visualize the decision tree\n3. Exit\n")
    while choice != str(3):

        # 1. specify parameters
        if choice == str(1):
            classification(df)
            # data_values = [True, False, False, True, Some, 3, False, True, French, 1]

            param = input(
                "Write you parameters in a dictionary format (eg: True, False, False, True, Full, 1, False, False, Thai, 3): ")
            # if type(param) != 'list':
            #     print("Please input a list!")
            #     continue

            print("Your expected outcome is: ")
            print("___________________________________________________________")
            # True, False, False, True, Full, 1, False, False, Thai, 3
            choice = input(
                "Please choose an option [1, 2, 3]: \n1. Specify Parameter\n2. Visualize the decision tree\n3. Exit\n")
            continue
        # 2. visualize the constructed decision tree
        elif choice == str(2):
            decision_tree_construction()
            choice = input(
"Please choose an option [1, 2, 3]: \n1. Specify Parameter\n2. Visualize the decision tree\n3. Exit\n")
            continue















    X_col = df.drop('willwait', axis=1)

    # split dataset in features and target variable
    feature_cols = ['alt', 'bar', 'fri', 'hun', 'pat', 'price', 'rain', 'res', 'type', 'est']
    X = X_col  # Features
    y = df['willwait']  # Target variable

    le = preprocessing.LabelEncoder()
    X = X.apply(le.fit_transform)
    y = le.fit_transform(y)

    # Create Decision Tree classifer object 1
    clf = tree.DecisionTreeClassifier(criterion='entropy', random_state=2)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.001,
                                                        random_state=0)  # 80% training and 20% test
    # Train Decision Tree Classifer
    clf = clf.fit(X_train, y_train)



    # print("Accuracy:",metrics.accuracy_score([[1,0,1,1,0,0,1,0,3,0]], y_pred))

    plt.figure(figsize=(12, 6))
    tree.plot_tree(clf, feature_names=feature_cols, class_names=['No', 'Willwait'], filled=True, rounded=True)

    plt.show()

from six import StringIO
from IPython.display import Image
import pydotplus



def classification(clf, user_list, le):
    # Predict the response for test dataset

    # print("Printing X_test: \n", X_test)
    # [[1,0,1,1,0,0,1,0,2,0]]
    y_pred = clf.predict([user_list])

    print("Predicted output: ", le.inverse_transform(y_pred))
def decision_tree_construction():
    print()

def splitting_criteria():
    print()

main()



