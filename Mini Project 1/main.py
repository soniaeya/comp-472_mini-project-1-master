import math

import pandas as pd
from splitting_criteria import SplittingCriteria
from entropy_calculation import EntropyCalculation
from decision_tree_construction import DecisionTreeConstruction
from classification import Classification
#  provide input datasets
# filename = input("To start, please provide the file name of your dataset?: ")
# with user input
# data = pd.read_excel(filename)
data = pd.read_excel('../Dataset/data.xlsx')
# windows
# data = pd.read_excel('..\Dataset\data.xlsx')
dataset = data.values.tolist()
outcome = [sublist[-1] for sublist in dataset]


entropy_instance = EntropyCalculation()
entropy_list = entropy_instance.entropy_calculation(dataset)[0]
entropy_value_dict = entropy_instance.entropy_calculation(dataset)[3]

splitting_criteria_instance = SplittingCriteria()
splitting_criteria_output = splitting_criteria_instance.splitting_criteria(entropy_list, entropy_value_dict)
choice = 1

while choice != str(3):
    choice = input(
        "Please choose an option [1, 2, 3]: \n1. Specify Parameter\n2. Visualize the decision tree\n3. Exit\n")
    # 1. specify parameters
    if choice == str(1):
        # data_values = [True, False, False, True, Some, 3, False, True, French, 1]

        param = input("Write you parameters in a dictionary format (eg: True, False, False, True, 'Some', 3, False, True, 'French', 1): ")
        # if type(param) != 'list':
        #     print("Please input a list!")
        #     continue
        obj = Classification()
        user_input = param.split(', ')
        idx = 0
        for i in user_input:
            if i == 'True':
                user_input[idx] = True
            elif i == 'False':
                user_input[idx] = False
            else:
                try:
                    user_input[idx] = int(i)
                except:
                    print()
            idx += 1

        # REPLCAE nan with None
        for i in dataset:
            idx = 0
            i.pop()
            for j in i:
                try:
                    if math.isnan(j):
                        i[idx] = 'None'
                except:
                    continue
                idx += 1
        print("Your expected outcome is: "+str(obj.classification(dataset, outcome, user_input)[0]))
        print("___________________________________________________________")
        # True, False, False, True, Full, 1, False, False, Thai, 3

        continue
    # 2. visualize the constructed decision tree
    elif choice == str(2):


        decision_tree_instance = DecisionTreeConstruction()
        decision_tree_instance.decision_tree_construction(splitting_criteria_output[0], splitting_criteria_output[1], dataset)
        continue

