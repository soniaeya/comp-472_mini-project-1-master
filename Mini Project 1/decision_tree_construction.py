
import networkx as nx
import matplotlib

matplotlib.use('TkAgg')  # Set the backend to TkAgg before importing pyplot

from treelib import Node, Tree

class DecisionTreeConstruction():
    def decision_tree_construction(self, sorted_nodes, ig_value_dict):
        sorted_nodes = ['patrons', 'est', 'hun', 'price', 'fri', 'rain', 'res', 'alt', 'bar', 'type']
        tree = Tree()
        idx = 0
        for i in sorted_nodes:
            path = []
            if idx == 0:
                tree.create_node(tag=i, identifier=i)
            sub_attr_dict = ig_value_dict.get(i)
            sum = 0
            for key, value in sub_attr_dict.items():
                # Reach a leaf node (information gain >= 1)
                if value == 1 or sum >= 1:
                    dict = {}
                    tree.create_node(tag=str("end (" + i + ": " + str(key) + ")"),
                                     identifier=str("end (" + i + ": " + str(key) + ")"), parent=i)

                else:
                    sum = sum + value
                    try:
                        tree.create_node(tag=sorted_nodes[idx + 1], identifier=sorted_nodes[idx + 1], parent=i)

                    except:
                        tree.create_node(tag=str("end (" + i + ": " + str(key) + ")"),
                                         identifier=str("end (" + i + ": " + str(key) + ")"), parent=i)
            path.append(i)
            idx += 1

        tree.show()








# "./Mini\ Project\ 1/decision_tree_construction.py"