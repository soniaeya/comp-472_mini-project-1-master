import entropy_calculation
import decision_tree_construction
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


# TODO use inheritence
class SplittingCriteria(entropy_calculation.EntropyCalculation):

    # this function returns the infogain as a pandas dataframe (attr, infoGain)
    def splitting_criteria(self, entropy_attr_dict, ig_value_dict):
        # print(ig_value_dict)
        #Returns node order
        sorted_nodes = sorted(entropy_attr_dict, key=lambda x: entropy_attr_dict[x])


        return [sorted_nodes, ig_value_dict]


# my_obj = SplittingCriteria()
# my_obj.splitting_criteria(entropy_calculation.EntropyCalculation.entropy_attr_dict, entropy_calculation.EntropyCalculation.ig_value_dict)
#

