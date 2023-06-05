import math

import classification
import matplotlib

matplotlib.use('TkAgg')  # Set the backend to TkAgg before importing pyplot

from treelib import Node, Tree


class DecisionTreeConstruction(classification.Classification):
    def decision_tree_construction(self, sorted_nodes, ig_value_dict, dataset):
        my_dict = {
            'alt': 0,
            'bar': 1,
            'fri': 2,
            'hun': 3,
            'patrons': 4,
            'price': 5,
            'rain': 6,
            'res': 7,
            'type': 8,
            'est': 9,
            'willwait': 10
        }
        tree = Tree()
        idx = 0
        X = []
        outcome = [[sublist[10] for sublist in dataset]]

        input = []
        path_taken = []
        key_path = []
        sum = 0
        for i in sorted_nodes:
            path_taken.append(i)
            if i == 'alt':
                X.append([sublist[0] for sublist in dataset])
            elif i == 'bar':
                X.append([sublist[1] for sublist in dataset])
            elif i == 'fri':
                X.append([sublist[2] for sublist in dataset])
            elif i == 'hun':
                X.append([sublist[3] for sublist in dataset])
            elif i == 'patrons':
                X.append([sublist[4] for sublist in dataset])
            elif i == 'price':
                X.append([sublist[5] for sublist in dataset])
            elif i == 'rain':
                X.append([sublist[6] for sublist in dataset])
            elif i == 'res':
                X.append([sublist[7] for sublist in dataset])
            elif i == 'type':
                X.append([sublist[8] for sublist in dataset])
            elif i == 'est':
                X.append([sublist[9] for sublist in dataset])

            if idx == 0:
                # Create Root Node
                tree.create_node(tag=i, identifier=i)
            sub_attr_dict = ig_value_dict.get(i)

            for key, value in sub_attr_dict.items():

                prediction = ""
                input.append(value)
                # Reach a leaf node (information gain >= 1)
                if value == 1 or sum >= 1:
                    data_idx = my_dict[sorted_nodes[idx]] # 4
                    for k in dataset:
                        try:
                            if math.isnan(k[data_idx]) and key == "None":
                                prediction = k[10]
                        except:
                            continue
                        if k[data_idx] == key:
                            prediction = k[10]
                    # return output

                    # print(obj.classification(obj, X=X, Y=outcome, user_input=key))

                    tree.create_node(tag=str(str(prediction)+" (" + i + ": " + str(key) + ")"), identifier=str(str(prediction)+" (" + i + ": " + str(key) + ")"), parent=i)

                else:

                    new_node = {i: key}
                    key_path.append((new_node))
                    sum = sum + value
                    try:
                        # prep X
                        idx_list = [] # Column 2 and 3 of data set
                        for i in path_taken:
                            idx_list.append(my_dict[i])
                        X = []

                        for j in idx_list:
                            list = []
                            list.append([sublist[j] for sublist in dataset])
                            X.append(list)
                        # print("X"+str(X))
                        # print("outcome"+str(outcome))
                        #
                        # print("keypath"+str(key_path))


                        #TODO change X based on path taken

                        tree.create_node(tag=sorted_nodes[idx + 1], identifier=sorted_nodes[idx + 1], parent=i)
                    # Reach a leaf node (no more attributes)
                    except:
                        # key_path.append((new_node))
                        continue
                        # # obj = classification.Classification()
                        # # print(obj.classification(obj, X=X, Y=outcome, user_input=key_path))
                        #
                        # tree.create_node(tag=str(str(prediction)+" (" + i + ": " + str(key) + ")"),
                        #                  identifier=str(str(prediction)+" (" + i + ": " + str(key) + ") "+str(key_path)), parent=i)

            idx += 1

        tree.show()

# "./Mini\ Project\ 1/decision_tree_construction.py"
