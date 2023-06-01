import entropy_calculation 
import pandas as pd

#TODO use inheritence

    # this function returns the infogain as a pandas dataframe (attr, infoGain)
def splitting_criteria():
    # Create information gain list
    gain_list = []
    for i in entropy_calculation.entropy_calculation():
        gain_list.append(1 - i)

    # Verify gain list outputs
    attribute_list = ["entropy_alt", "entropy_bar", "entropy_fri", "entropy_hun", "entropy_patrons",
                      "entropy_price", "entropy_rain", "entropy_res", "entropy_type", "entropy_est"]

    # Create dict for attributes and their info gain values
    my_dict = {k: v for k, v in zip(attribute_list, gain_list)}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    # print(sorted_dict)

    data = {
        "attr": sorted_dict.keys(),
        "infoGain": sorted_dict.values()
    }

    # load data into a DataFrame object:

    df = pd.DataFrame(data)

    # Output info gain pandas dataframe
    return df


print(splitting_criteria())
    


