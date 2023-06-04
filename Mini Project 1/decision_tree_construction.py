from splitting_criteria import SplittingCriteria
import networkx as nx
import matplotlib

matplotlib.use('TkAgg')  # Set the backend to TkAgg before importing pyplot

import matplotlib.pyplot as plt
import decision_tree

class DecisionTreeConstruction(SplittingCriteria):
    def decision_tree_construction(self):
        sorted_nodes = ['patrons', 'est', 'hun', 'price', 'fri', 'rain', 'res', 'alt', 'bar', 'type']

        ig_value_dict = {'alt': {True: 0.0, False: 0.0}, 'bar': {True: 0.0, False: 0.0},
                         'fri': {True: 0.02904940554533142, False: 0.014771863965748366},
                         'hun': {True: 0.136879431433369, False: 0.2780719051126377},
                         'patrons': {'Full': 0.08170416594551044, 'Some': 1, 'None': 1},
                         'price': {'$': 1, '$$$': 0.08170416594551044},
                         'rain': {True: 0.02904940554533142, False: 0.014771863965748366},
                         'res': {True: 0.02904940554533142, False: 0.014771863965748366},
                         'type': {'Italian': 0.0, 'French': 0.0, 'Burger': 0.0, 'Thai': 0.0},
                         'est': {'0-10': 0.08170416594551044, '10-30': 0.0, '30-60': 0.0, '>60': 1.0}}
        tree = decision_tree.DecisionTree





# "./Mini\ Project\ 1/decision_tree_construction.py"