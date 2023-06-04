
from treelib import Node, Tree

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

# Create an example tree
tree = Tree()
no = 0
idx = 0
# for i in sorted_nodes:
#     if idx == 0:
#         tree.create_node(tag=i, identifier=i)
#     else:
#         tree.create_node(tag=i, identifier=i, parent=sorted_nodes[idx - 1])
#     idx += 1
#
idx = 0
id = 0
for i in sorted_nodes:
    if idx == 0:
        tree.create_node(tag=i, identifier=i)
    sub_attr_dict = ig_value_dict.get(i)
    sum = 0
    for key, value in sub_attr_dict.items():

        if value == 1 or sum >= 1:
            tree.create_node(tag=str("end ("+i+": "+str(key)+")"), identifier=str("end ("+i+": "+str(key)+")"), parent=i)
            no += 1
        else:
            sum = sum + value
            try:
                tree.create_node(tag=sorted_nodes[idx+1], identifier=sorted_nodes[idx+1], parent=i)
            except:
                tree.create_node(tag=str("end ("+i+": "+str(key)+")"), identifier=str("end ("+i+": "+str(key)+")"), parent=i)

    idx += 1



tree.show()