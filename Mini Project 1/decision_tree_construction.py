import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn import tree
from splitting_criteria import SplittingCriteria
from entropy_calculation import EntropyCalculation
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor


class DecisionTreeConstruction(SplittingCriteria):





    def decision_tree_construction(self):
        data = pd.read_excel('../Dataset/data.xlsx')
        dataset = data.values.tolist()
        dataset = np.array(dataset)
        df2 = pd.DataFrame(dataset,
                           columns=['Alt', 'Bar', 'Fri', 'Hun', 'Pat', 'Price', 'Rain', 'Res', 'Type', 'Est',
                                    'WillWait'])
        blankIndex = [''] * len(df2)
        df2.index = blankIndex

        X = dataset[:, 0:10]

        y = dataset[:, 10]

        le = preprocessing.LabelEncoder()
        X[:, 0] = le.fit_transform(X[:, 0])

        y = le.fit_transform(y)
        clf = DecisionTreeRegressor(splitter=SplittingCriteria())



        clf.fit(X, y)
        fig, ax = plt.subplots(figsize=(12, 8))
        tree.plot_tree(clf,
                       feature_names=['Alt', 'Bar', 'Fri', 'Hun', 'Pat', 'Price', 'Rain', 'Res', 'Type', 'Est',
                                      'WillWait'],
                       class_names=le.classes_.astype(str),  # Convert class names to strings
                       filled=True, rounded=True, ax=ax)

        plt.show()














        # data = pd.read_excel('../Dataset/data.xlsx')
        #
        # # windows
        # # data = pd.read_excel('..\Dataset\data.xlsx')
        # dataset = data.values.tolist()
        # for x in dataset:
        #     count = 0
        #     for value in x:
        #         # For T/F variables
        #         if value == True:
        #             x[count] = 1
        #         elif value == False:
        #             x[count] = 0
        #
        #         # For Patrons
        #         if value == "Full":
        #             x[count] = 2
        #         elif value == "Some":
        #             x[count] = 1
        #         elif pd.isnull(value):
        #             x[count] = 0
        #
        #         # For Types
        #         if value == "Italian":
        #             x[count] = 3
        #         elif value == "French":
        #             x[count] = 2
        #         elif value == "Burger":
        #             x[count] = 1
        #         elif value == "Thai":
        #             x[count] = 0
        #
        #         count += 1
        #


    # This function returns a list of the entropy of each attr






    #
    # dtc = tree.DecisionTreeClassifier(criterion=splitting_criteria.splitting_criteria())
    # dtc.fit(X, y)
    #



# decision_tree_construction(splitting_criteria.splitting_criteria())




