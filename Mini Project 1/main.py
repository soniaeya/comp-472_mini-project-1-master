import pandas as pd
import splitting_criteria
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
entropy_instance = EntropyCalculation()
entropy_list = entropy_instance.entropy_calculation(dataset)[0]
entropy_value_dict = entropy_instance.entropy_calculation(dataset)[3]

splitting_criteria_instance = splitting_criteria.SplittingCriteria()
splitting_criteria_output = splitting_criteria_instance.splitting_criteria(entropy_list, entropy_value_dict)

choice = input("Please choose an option [1 or 2]: \n1. Specify Parameter\n2. Visualize the decision tree")
if choice == str(1):
    param = input("Write you paramaters in a dictionary format: ")
elif choice == str(2):
    decision_tree_instance = DecisionTreeConstruction()
    decision_tree_instance.decision_tree_construction(splitting_criteria_output[0], splitting_criteria_output[1])

# Please choose an option
# 1. specify parameters


# 2. visualize the constructed decision tree








