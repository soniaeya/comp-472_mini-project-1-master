import entropy_calculation
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


# TODO use inheritence
class SplittingCriteria(entropy_calculation.EntropyCalculation):
    # this function returns the infogain as a pandas dataframe (attr, infoGain)
    def splitting_criteria(self, entropy_list, entropy_value_dict):
        # Create information gain list
        gain_list = []
        for i in entropy_list:
            gain_list.append(1 - i)

        # Verify gain list outputs
        # attribute_list = ["entropy_alt", "entropy_bar", "entropy_fri", "entropy_hun", "entropy_patrons",
        #                   "entropy_price", "entropy_rain", "entropy_res", "entropy_type", "entropy_est"]
        #
        attribute_list = ["alt", "bar", "fri", "hun", "patrons", "price", "rain", "res", "type", "est"]

        # Create dict for attributes and their info gain values
        my_dict = {k: v for k, v in zip(attribute_list, gain_list)}
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
        # print(sorted_dict)

        data = {
            "attr": sorted_dict.keys(),
            "infoGain": sorted_dict.values()
        }
        df = pd.DataFrame(data)
        max_y = df['infoGain'].max()
        max_x = df.loc[df['infoGain'] == max_y, 'attr'].values

        best_feature = max_x
        best_threshold = 1.0
        child_nodes = entropy_value_dict.get(best_feature[0])
        print(type(child_nodes.values()))








        # for i in child_nodes:
        #     if i.value() == 0:
        #         print("ok")
        # left_indices =
        # right_indices =

        # load data into a DataFrame object:

        # Output info gain pandas dataframe
        # return best_feature, best_threshold, left_indices, right_indices



