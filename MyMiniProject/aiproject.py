# Load libraries
import pandas as pd
from sklearn import tree  # Import Decision Tree Classifier
from sklearn import preprocessing  # to turn strings into numbers
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn import metrics  # Import scikit-learn metrics module for accuracy calculation
import numpy as np

import matplotlib.pyplot as plt

import warnings
from sklearn.exceptions import DataConversionWarning

warnings.filterwarnings("ignore", category=DataConversionWarning)


# [[1,0,0,1,3,5,0,]]
def main():
    col_names = ['alt', 'bar', 'fri', 'hun', 'pat', 'price', 'rain', 'res', 'type', 'est', 'willwait']
    # load dataset
    dataset = pd.read_csv("training_data.csv")
    dataset = pd.DataFrame(dataset)
    feature_cols = []

    for cols in dataset.columns:
        feature_cols.append(cols)

    target_cols = []
    target_cols = feature_cols.pop()

    X_col = dataset.iloc[:, 0:len(dataset) - 2]
    df1 = pd.DataFrame(X_col)
    # print(df1)

    y_col = dataset.iloc[:, -1]
    df2 = pd.DataFrame(y_col)
    # print(df2)
    le = preprocessing.LabelEncoder()

    X = df1  # Features
    y = df2  # Target variable
    X = X.apply(le.fit_transform)
    print(X)
    y = le.fit_transform(y)

    choice = input(
        "Please choose an option [1, 2, 3]: \n1. Visualize the decision tree\n2. Specify Parameter\n3. Exit\n")
    while choice != str(3):
        # choice = input("Please choose an option [1, 2, 3]: \n1. Specify Parameter\n2. Visualize the decision tree\n3. "
        #                "Exit\n")
        # 2. specify parameters
        if choice == str(2):
            user_input = input("Enter you user input, and separate with whitespace: ")
            user_input = user_input.split(" ")
            idx = 0
            for i in user_input:
                user_input[idx] = float(i)
                idx += 1
            user_input = [user_input]

            # print("Printing X_test: \n", X_test)
            # [[1,0,1,1,0,0,1,0,2,0]]
            y_pred = clf.predict(user_input)

            print("Predicted output: ", le.inverse_transform(y_pred))
            # split dataset in features and target variable
            choice = input("Please choose an option [1, 2, 3]: \n1. Visualize the decision tree\n2. Specify "
                           "Parameter\n3. Exit\n")
            continue



        # 1. visualize the constructed decision tree
        elif choice == str(1):
            # Create Decision Tree classifer object
            clf = tree.DecisionTreeClassifier(criterion='entropy', random_state=2)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.001,
                                                                random_state=0)  # 80% training and 20% test
            # Train Decision Tree Classifer
            clf = clf.fit(X_train, y_train)

            # #Predict the response for test dataset
            #

            # print("Accuracy:",metrics.accuracy_score([[1,0,1,1,0,0,1,0,3,0]], y_pred))

            plt.figure(figsize=(12, 6))

            tree.plot_tree(clf, feature_names=feature_cols, class_names=['No', 'Willwait'], filled=True, rounded=True)

            plt.show()
            print("The Decision Tree has been printed!")
            print()
            choice = input("Please choose an option [1, 2, 3]: \n1. Visualize the decision tree\n2. Specify "
                           "Parameter\n3. Exit\n")
        elif choice == str(3):
            exit()


main()
