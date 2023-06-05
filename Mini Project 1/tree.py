import networkx as nx
import matplotlib

matplotlib.use('TkAgg')  # Set the backend to TkAgg before importing pyplot

from treelib import Node, Tree


class DecisionTreeConstruction():
    def decision_tree_construction(self):
        user_path = [True, False, False, True, 'Some', 3, False, True, 'French']

        ig_value_dict = {'alt': {True: 0.0, False: 0.0}, 'bar': {True: 0.0, False: 0.0}, 'fri': {True: 0.02904940554533142, False: 0.014771863965748366}, 'hun': {True: 0.136879431433369, False: 0.2780719051126377}, 'patrons': {'Full': 0.08170416594551044, 'Some': 1, 'None': 1}, 'price': {'$': 0.014771863965748366, '$$': 1, '$$$': 0.08170416594551044}, 'rain': {True: 0.02904940554533142, False: 0.014771863965748366}, 'res': {True: 0.02904940554533142, False: 0.014771863965748366}, 'type': {'Italian': 0.0, 'French': 0.0, 'Burger': 0.0, 'Thai': 0.0}, 'est': {'0-10': 0.08170416594551044, '10-30': 0.0, '30-60': 0.0, '>60': 1.0}}
        sorted_nodes = ['patrons', 'est', 'hun', 'price', 'fri', 'rain', 'res', 'alt', 'bar', 'type']
        idx = 0
        tree = Tree()
        #TODO How to determine outcome? Y/N
        for i in sorted_nodes:

            if idx == 0:
                tree.create_node(tag=i, identifier=i)
            sub_attr_dict = ig_value_dict.get(i)
            sum = 0
            for key, value in sub_attr_dict.items():
                # Reach a leaf node (information gain >= 1)
                # TODO add outcome to path
                if value == 1 or sum >= 1:
                    tree.create_node(tag=str("end (" + i + ": " + str(key) + ")"),
                                     identifier=str("end (" + i + ": " + str(key) + ")"), parent=i)
                # Internal node
                else:
                    sum = sum + value
                    try:
                        # TODO add to path
                        tree.create_node(tag=sorted_nodes[idx + 1], identifier=sorted_nodes[idx + 1], parent=i)

                    # Reached last attribute
                    except:
                        # TODO add outcome to path
                        tree.create_node(tag=str("end (" + i + ": " + str(key) + ")"),
                                         identifier=str("end (" + i + ": " + str(key) + ")"), parent=i)

            idx += 1
        # tree.show()
obj = DecisionTreeConstruction()
obj.decision_tree_construction()




























