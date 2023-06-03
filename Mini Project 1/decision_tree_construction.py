from splitting_criteria import SplittingCriteria
import networkx as nx
import matplotlib

matplotlib.use('TkAgg')  # Set the backend to TkAgg before importing pyplot

import matplotlib.pyplot as plt


class DecisionTreeConstruction(SplittingCriteria):
    def decision_tree_construction(self):

        G = nx.DiGraph()
        G.add_nodes_from(["one", 2, 3])
        G.add_edges_from([("one", 2), ("one", 3)])
        pos = nx.nx_agraph.graphviz_layout(G, prog='dot')

        fig, ax = plt.subplots()
        nx.draw(G, pos, with_labels=True, arrows=True, ax=ax)

        ax.set_aspect('equal')

        plt.show()

        print()


# "./Mini\ Project\ 1/decision_tree_construction.py"