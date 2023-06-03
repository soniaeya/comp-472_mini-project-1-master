import pandas as pd
from splitting_criteria import SplittingCriteria
from entropy_calculation import EntropyCalculation
from decision_tree_construction import DecisionTreeConstruction


#  provide input datasets
# filename = input("To start, please provide the file name of your dataset?: ")
# with user input
# data = pd.read_excel(filename)
data = pd.read_excel('../Dataset/data.xlsx')
# windows
# data = pd.read_excel('..\Dataset\data.xlsx')
dataset = data.values.tolist()

# Please choose an option
# 1. specify parameters


# 2. visualize the constructed decision tree
entropy_instance = EntropyCalculation()
entropy_list = entropy_instance.entropy_calculation(dataset)[0]
entropy_value_dict = entropy_instance.entropy_calculation(dataset)[1]
splitting_criteria_instance = SplittingCriteria()
splitting_criteria_instance.splitting_criteria(entropy_list, entropy_value_dict)
decision_tree_instance = DecisionTreeConstruction()
# decision_tree_instance.decision_tree_construction(entropy_instance, splitting_criteria_instance)
decision_tree_instance.decision_tree_construction()







