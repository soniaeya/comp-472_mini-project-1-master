import math

import numpy as np
import pandas as pd



class EntropyCalculation:
    entropy_attr_dict = {}
    entropy_value_dict = {}
    ig_attr_dict = {}
    ig_value_dict = {}
    def entropy_calculation(self, dataset):

        entropy_value_list = []
        ig_value_list = []
        entropy_list = []  # [[1.0, 1.0], [1.0, 1.0], [0.9709505944546686, 0.9852281360342515], [0.863120568566631, 0.7219280948873623], [0.9182958340544896, 0, 0], [0.9852281360342515, 0, 0.9182958340544896], [0.9709505944546686, 0.9852281360342515], [0.9709505944546686, 0.9852281360342515], [1.0, 1.0, 1.0, 1.0], [0.9182958340544896, 1.0, 1.0, -0.0]]
        ig_list = []
        # Alt variables
        num_alt_true = 0
        num_alt_false = 0
        num_alt_t_true = 0
        num_alt_t_false = 0
        entropy_alt = 0

        # bar variables (1)
        num_bar_true = 0
        num_bar_false = 0
        num_bar_t_true = 0
        num_bar_t_false = 0
        entropy_bar = 0

        # fri variables (2)
        num_fri_true = 0
        num_fri_false = 0
        num_fri_t_true = 0
        num_fri_t_false = 0
        entropy_fri = 0

        # hun variables (3)
        num_hun_true = 0
        num_hun_false = 0
        num_hun_t_true = 0
        num_hun_t_false = 0
        entropy_hun = 0

        # price variables
        num_1_price = 0
        num_t_1_price = 0
        num_2_price = 0
        num_t_2_price = 0
        num_3_price = 0
        num_t_3_price = 0
        num_4_price = 0
        num_t_4_price = 0
        entropy_price = 0

        # rain variables
        num_rain_true = 0
        num_rain_false = 0
        num_rain_t_true = 0
        num_rain_t_false = 0
        entropy_rain = 0

        # res variables
        num_res_true = 0
        num_res_false = 0
        num_res_t_true = 0
        num_res_t_false = 0
        entropy_res = 0

        # type variables
        num_type_french = 0
        num_type_italian = 0
        num_type_thai = 0
        num_type_burger = 0

        num_type_t_french = 0
        num_type_t_italian = 0
        num_type_t_thai = 0
        num_type_t_burger = 0

        # Patron variables
        num_none = 0
        num_some = 0
        num_full = 0
        num_t_none = 0
        num_t_some = 0
        num_t_full = 0
        entropy_sum_patron = 0

        # Est variables

        num_1_est = 0
        num_t_1_est = 0
        num_2_est = 0
        num_t_2_est = 0
        num_3_est = 0
        num_t_3_est = 0
        num_4_est = 0
        num_t_4_est = 0
        entropy_est = 0

        for i in dataset:
            if i[0]:
                num_alt_true += 1
                num_alt_t_true += 1 if i[10] else 0
            if not i[0]:
                num_alt_false += 1
                num_alt_t_false += 1 if i[10] else 0

            if i[1]:
                num_bar_true += 1
                num_bar_t_true += 1 if i[10] else 0
            if not i[1]:
                num_bar_false += 1
                num_bar_t_false += 1 if i[10] else 0

            if i[2]:
                num_fri_true += 1
                num_fri_t_true += 1 if i[10] else 0
            if not i[2]:
                num_fri_false += 1
                num_fri_t_false += 1 if i[10] else 0
            if i[3]:
                num_hun_true += 1
                num_hun_t_true += 1 if i[10] else 0
            if not i[3]:
                num_hun_false += 1
                num_hun_t_false += 1 if i[10] else 0

            if i[4] == "Full":
                num_full += 1
                num_t_full += 1 if i[10] else 0
            elif i[4] == "Some":
                num_some += 1
                num_t_some += 1 if i[10] else 0
            elif np.isnan(i[4]):
                num_none += 1
                num_t_none += 1 if i[10] else 0

            if i[5] == 3:
                num_3_price += 1
                num_t_3_price += 1 if i[10] else 0
            elif i[5] == 2:
                num_2_price += 1
                num_t_2_price += 1 if i[10] else 0
            elif i[5] == 1:
                num_1_price += 1
                num_t_1_price += 1 if i[10] else 0

            if i[6]:
                num_rain_true += 1
                num_rain_t_true += 1 if i[10] == True else 0
            if not i[6]:
                num_rain_false += 1
                num_rain_t_false += 1 if i[10] == True else 0

            if i[7]:
                num_res_true += 1
                num_res_t_true += 1 if i[10] == True else 0
            if not i[7]:
                num_res_false += 1
                num_res_t_false += 1 if i[10] == True else 0

            if i[8] == "French":
                num_type_french += 1
                num_type_t_french += 1 if i[10] == True else 0
            elif i[8] == "Italian":
                num_type_italian += 1
                num_type_t_italian += 1 if i[10] == True else 0
            elif i[8] == "Thai":
                num_type_thai += 1
                num_type_t_thai += 1 if i[10] == True else 0
            elif i[8] == "Burger":
                num_type_burger += 1
                num_type_t_burger += 1 if i[10] == True else 0

            if i[9] == 3:
                num_3_est += 1
                num_t_3_est += 1 if i[10] == True else 0
            elif i[9] == 2:
                num_2_est += 1
                num_t_2_est += 1 if i[10] == True else 0
            elif i[9] == 1:
                num_1_est += 1
                num_t_1_est += 1 if i[10] == True else 0
            elif i[9] == 4:
                num_4_est += 1
                num_t_4_est += 1 if i[10] == True else 0

        #  ENTROPY CALCULATIONS
        # 1 - alt
        try:
            num_alt = num_alt_true + num_alt_false
            p_alt_true = num_alt_true / num_alt
            p_alt_false = num_alt_false / num_alt

            # Calculate entropy H(alt=true)
            t = num_alt_t_true / num_alt_true
            f = (num_alt_true - num_alt_t_true) / num_alt_true
            try:
                entropy_alt_true = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_alt_true = 0

            # Calculate entropy H(alt=false)
            t = num_alt_t_false / num_alt_false
            f = (num_alt_false - num_alt_t_false) / num_alt_false
            try:
                entropy_alt_false = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_alt_false = 0

            entropy_alt = entropy_alt_true * p_alt_true + entropy_alt_false * p_alt_false
        except:
            entropy_alt = 0
        entropy_alt_list = [entropy_alt_true, entropy_alt_false]
        entropy_list.append(entropy_alt_list)
        # Making entropy dict
        my_dict = {k: v for k, v in zip([True, False], entropy_alt_list)}

        ig_alt_list = [1 - entropy_alt_true, 1 - entropy_alt_false]
        ig_list.append(ig_alt_list)
        my_dict_ig = {k: v for k, v in zip([True, False], ig_alt_list)}
        ig_value_list.append(my_dict_ig)

        entropy_value_list.append(my_dict)

        # 2 - bar
        try:
            num_bar = num_bar_true + num_bar_false
            p_bar_true = num_bar_true / num_bar
            p_bar_false = num_bar_false / num_bar

            # Calculate entropy H(bar=true)
            t = num_bar_t_true / num_bar_true
            f = (num_bar_true - num_bar_t_true) / num_bar_true
            try:
                entropy_bar_true = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_bar_true = 0

            # Calculate entropy H(bar=false)
            t = num_bar_t_false / num_bar_false
            f = (num_bar_false - num_bar_t_false) / num_bar_false
            try:
                entropy_bar_false = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_bar_false = 0

            entropy_bar = entropy_bar_true * p_bar_true + entropy_bar_false * p_bar_false
        except:
            entropy_bar = 0
        entropy_bar_list = [entropy_bar_true, entropy_bar_false]
        entropy_list.append(entropy_bar_list)
        my_dict = {k: v for k, v in zip([True, False], entropy_bar_list)}
        entropy_value_list.append(my_dict)
        ig_bar_list = [1 - entropy_bar_true, 1 - entropy_bar_false]
        ig_list.append(ig_bar_list)
        my_dict_ig = {k: v for k, v in zip([True, False], ig_bar_list)}
        ig_value_list.append(my_dict_ig)

        # 2 - fri
        try:
            num_fri = num_fri_true + num_fri_false
            p_fri_true = num_fri_true / num_fri
            p_fri_false = num_fri_false / num_fri

            # Calculate entropy H(fri=true)
            t = num_fri_t_true / num_fri_true
            f = (num_fri_true - num_fri_t_true) / num_fri_true
            try:
                entropy_fri_true = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_fri_true = 0

            # Calculate entropy H(fri=false)
            t = num_fri_t_false / num_fri_false
            f = (num_fri_false - num_fri_t_false) / num_fri_false
            try:
                entropy_fri_false = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_fri_false = 0

            entropy_fri = entropy_fri_true * p_fri_true + entropy_fri_false * p_fri_false
        except:
            entropy_fri = 0
        entropy_fri_list = [entropy_fri_true, entropy_fri_false]
        entropy_list.append(entropy_fri_list)
        my_dict = {k: v for k, v in zip([True, False], entropy_fri_list)}

        entropy_value_list.append(my_dict)

        ig_fri_list = [1 - entropy_fri_true, 1 - entropy_fri_false]
        ig_list.append(ig_fri_list)
        my_dict_ig = {k: v for k, v in zip([True, False], ig_fri_list)}
        ig_value_list.append(my_dict_ig)
        # 3 - hun
        try:
            num_hun = num_hun_true + num_hun_false
            p_hun_true = num_hun_true / num_hun
            p_hun_false = num_hun_false / num_hun

            # Calculate entropy H(hun=true)
            t = num_hun_t_true / num_hun_true
            f = (num_hun_true - num_hun_t_true) / num_hun_true
            try:
                entropy_hun_true = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_hun_true = 0

            # Calculate entropy H(hun=false)
            t = num_hun_t_false / num_hun_false
            f = (num_hun_false - num_hun_t_false) / num_hun_false
            try:
                entropy_hun_false = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_hun_false = 0

            entropy_hun = entropy_hun_true * p_hun_true + entropy_hun_false * p_hun_false
        except:
            entropy_hun = 0
        entropy_hun_list = [entropy_hun_true, entropy_hun_false]
        entropy_list.append(entropy_hun_list)
        my_dict = {k: v for k, v in zip([True, False], entropy_hun_list)}

        entropy_value_list.append(my_dict)
        ig_hun_list = [1 - entropy_hun_true, 1 - entropy_hun_false]
        ig_list.append(ig_hun_list)
        my_dict_ig = {k: v for k, v in zip([True, False], ig_hun_list)}
        ig_value_list.append(my_dict_ig)

        # 4 - Patrons
        # Calculate entropy H(Patrons=Full)
        num_patrons = num_full + num_none + num_t_some  # Total num patrons
        # Probability of each event (full, some, none)
        p_num_full = num_full / num_patrons
        p_num_some = num_some / num_patrons
        p_num_none = num_none / num_patrons
        try:
            # Calculate Entropy of full variable
            p_t_full = num_t_full / num_full
            p_f_full = (num_full - num_t_full) / num_full
            try:
                entropy_patron_full = (-(p_t_full * math.log2(p_t_full) + p_f_full * math.log2(p_f_full)))
            except:
                entropy_patron_full = 0
            # Calculate entropy H(Patrons=Some)
            p_t_some = num_t_some / num_some
            p_f_some = (num_some - num_t_some) / num_some

            try:
                entropy_patron_some = -(p_t_some * math.log2(p_t_some) + p_f_some * math.log2(p_f_some))
            except:
                entropy_patron_some = 0
            # Calculate entropy H(Patrons=None)
            p_t_none = num_t_none / num_none
            p_f_none = (num_none - num_t_none) / num_none
            try:
                entropy_patron_none = -(p_t_none * math.log2(p_t_none) + p_f_none * math.log2(p_f_none))
            except:
                entropy_patron_none = 0

            entropy_patrons = p_num_full * entropy_patron_full + p_num_some * entropy_patron_some + p_num_none * entropy_patron_none
            # print("entropy_patron_full: " + str(entropy_patron_full))
            # print("entropy_patron_some: " + str(entropy_patron_some))
            # print("entropy_patron_none: "+str(entropy_patron_none))
            # print("entropy_patrons: "+str(entropy_patrons))
        except:
            entropy_patrons = 1.0

        entropy_patron_list = [entropy_patron_full, entropy_patron_some, entropy_patron_none]
        entropy_list.append(entropy_patron_list)
        my_dict = {k: v for k, v in zip(["Full", "Some", "None"], entropy_patron_list)}
        entropy_value_list.append(my_dict)

        ig_patron_list = [1 - entropy_patron_full, 1 - entropy_patron_some, 1 - entropy_patron_some]
        ig_list.append(ig_patron_list)
        my_dict_ig = {k: v for k, v in zip(["Full", "Some", "None"], ig_patron_list)}
        ig_value_list.append(my_dict_ig)

        # 5 - Price

        try:
            num_price = num_1_price + num_2_price + num_3_price
            p_price_1 = num_1_price / num_price
            p_price_2 = num_2_price / num_price
            p_price_3 = num_3_price / num_price

            # Calculate entropy H(price = 1)
            t = num_t_1_price / num_1_price
            f = (num_1_price - num_t_1_price) / num_1_price

            first = 0 if t == 0.0 or t == 1.0 else t * math.log2(t)
            second = 0 if f == 0.0 or t == 1.0 else f * math.log2(f)
            entropy_price_1 = -(first + second)

            # Calculate entropy H(price = 2)
            t = num_t_2_price / num_2_price
            f = (num_2_price - num_t_2_price) / num_2_price

            first = 0 if t == 0.0 or t == 1.0 else t * math.log2(t)
            second = 0 if f == 0.0 or t == 1.0 else f * math.log2(f)
            entropy_price_2 = -(first + second)

            t = num_t_3_price / num_3_price
            f = (num_3_price - num_t_3_price) / num_3_price

            first = 0 if t == 0.0 or t == 1.0 else t * math.log2(t)
            second = 0 if f == 0.0 or t == 1.0 else f * math.log2(f)

            entropy_price_3 = -(first + second)
            entropy_price = p_price_1 * entropy_price_1 + p_price_2 * entropy_price_2 + p_price_3 * entropy_price_3

        except:
            print()
        entropy_price_list = [entropy_price_1, entropy_price_2, entropy_price_3]
        entropy_list.append(entropy_price_list)
        my_dict = {k: v for k, v in zip(["$", "$$", "$$$"], entropy_price_list)}
        entropy_value_list.append(my_dict)

        ig_price_list = [1 - entropy_price_1, 1 - entropy_price_2, 1 - entropy_price_3]
        ig_list.append(ig_price_list)
        my_dict_ig = {k: v for k, v in zip(["$", "$$", "$$$"], ig_price_list)}
        ig_value_list.append(my_dict_ig)

        # 6 - rain
        try:
            num_rain = num_rain_true + num_rain_false
            p_rain_true = num_rain_true / num_rain
            p_rain_false = num_rain_false / num_rain

            # Calculate entropy H(rain=true)
            t = num_rain_t_true / num_rain_true
            f = (num_rain_true - num_rain_t_true) / num_rain_true
            try:
                entropy_rain_true = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_rain_true = 0

            # Calculate entropy H(rain=false)
            t = num_rain_t_false / num_rain_false
            f = (num_rain_false - num_rain_t_false) / num_rain_false
            try:
                entropy_rain_false = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_rain_false = 0

            entropy_rain = entropy_rain_true * p_rain_true + entropy_rain_false * p_rain_false
        except:
            entropy_rain = 0
        entropy_rain_list = [entropy_rain_true, entropy_rain_false]
        entropy_list.append(entropy_rain_list)
        my_dict = {k: v for k, v in zip([True, False], entropy_rain_list)}

        entropy_value_list.append(my_dict)
        ig_rain_list = [1 - entropy_rain_true, 1 - entropy_rain_false]
        ig_list.append(ig_rain_list)
        my_dict_ig = {k: v for k, v in zip([True, False], ig_rain_list)}
        ig_value_list.append(my_dict_ig)

        # 7 - res
        try:
            num_res = num_res_true + num_res_false
            p_res_true = num_res_true / num_res
            p_res_false = num_res_false / num_res

            # Calculate entropy H(res=true)
            t = num_res_t_true / num_res_true
            f = (num_res_true - num_res_t_true) / num_res_true
            try:
                entropy_res_true = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_res_true = 0

            # Calculate entropy H(res=false)
            t = num_res_t_false / num_res_false
            f = (num_res_false - num_res_t_false) / num_res_false
            try:
                entropy_res_false = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_res_false = 0

            entropy_res = entropy_res_true * p_res_true + entropy_res_false * p_res_false
        except:
            entropy_res = 0
        entropy_res_list = [entropy_res_true, entropy_res_false]
        entropy_list.append(entropy_res_list)
        my_dict = {k: v for k, v in zip([True, False], entropy_res_list)}

        entropy_value_list.append(my_dict)
        ig_res_list = [1 - entropy_res_true, 1 - entropy_res_false]
        ig_list.append(ig_res_list)
        my_dict_ig = {k: v for k, v in zip([True, False], ig_res_list)}
        ig_value_list.append(my_dict_ig)

        # 8 - Type
        num_type = num_type_italian + num_type_french + num_type_burger + num_type_thai
        p_type_french = num_type_french / num_type
        p_type_italian = num_type_italian / num_type
        p_type_thai = num_type_thai / num_type
        p_type_burger = num_type_burger / num_type

        try:
            # Calculate entropy H(type=thai)
            t = num_type_t_thai / num_type_thai
            f = (num_type_thai - num_type_t_thai) / num_type_thai

            try:
                entropy_type_thai = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_type_thai = 0
            t = num_type_t_burger / num_type_burger
            f = (num_type_burger - num_type_t_burger) / num_type_burger

            try:
                entropy_type_burger = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_type_burger = 0
            # Calculate entropy H(type=french)
            t = num_type_t_french / num_type_french
            f = (num_type_french - num_type_t_french) / num_type_french
            try:
                entropy_type_french = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_type_french = 0
            # Calculate entropy H(type=italian)
            t = num_type_t_italian / num_type_italian
            f = (num_type_italian - num_type_t_italian) / num_type_italian
            try:
                entropy_type_italian = -(t * math.log2(t) + f * math.log2(f))
            except:
                entropy_type_italian = 0
            # Calculate entropy H(type=burger)
            try:
                entropy_type = p_type_burger * entropy_type_burger + p_type_italian * entropy_type_italian + p_type_french * entropy_type_french + p_type_thai * entropy_type_thai
            except:
                entropy_type = 0
        except:
            entropy_type = 0
        entropy_type_list = [entropy_type_italian, entropy_type_french, entropy_type_burger, entropy_type_thai]
        entropy_list.append(entropy_type_list)
        my_dict = {k: v for k, v in zip(["Italian", "French", "Burger", "Thai"], entropy_type_list)}
        entropy_value_list.append(my_dict)
        ig_type_list = [1 - entropy_type_italian, 1 - entropy_type_french, 1 - entropy_type_burger,
                        1 - entropy_type_thai]
        ig_list.append(ig_type_list)
        my_dict_ig = {k: v for k, v in zip(["Italian", "French", "Burger", "Thai"], ig_type_list)}
        ig_value_list.append(my_dict_ig)

        # 9-Estimate i[9]
        # EXPLANATION: if numerator/denominator = 1, numerator = denominator -> no entropy
        # numerator/denominator = 0, numerator = 0 -> no entropy
        # we do dot hold these 2 situations into account

        try:
            num_est = num_1_est + num_2_est + num_3_est + num_4_est
            p_est_1 = num_1_est / num_est
            p_est_2 = num_2_est / num_est
            p_est_3 = num_3_est / num_est
            p_est_4 = num_4_est / num_est

            # Calculate entropy H(est = 1)
            t = num_t_1_est / num_1_est
            f = (num_1_est - num_t_1_est) / num_1_est

            first = 0 if t == 0.0 or t == 1.0 else t * math.log2(t)
            second = 0 if f == 0.0 or t == 1.0 else f * math.log2(f)
            entropy_est_1 = -(first + second)

            # Calculate entropy H(est = 2)
            t = num_t_2_est / num_2_est
            f = (num_2_est - num_t_2_est) / num_2_est

            first = 0 if t == 0.0 or t == 1.0 else t * math.log2(t)
            second = 0 if f == 0.0 or t == 1.0 else f * math.log2(f)
            entropy_est_2 = -(first + second)
            # Calculate entropy H(est = 3)
            t = num_t_3_est / num_3_est
            f = (num_3_est - num_t_3_est) / num_3_est

            first = 0 if t == 0.0 or t == 1.0 else t * math.log2(t)
            second = 0 if f == 0.0 or t == 1.0 else f * math.log2(f)

            entropy_est_3 = -(first + second)
            # Calculate entropy H(est = 4)

            t = num_t_4_est / num_4_est
            f = (num_4_est - num_t_4_est) / num_4_est

            first = 0 if t == 0.0 or t == 1.0 else t * math.log2(t)
            second = 0 if f == 0.0 or t == 1.0 else f * math.log2(f)

            entropy_est_4 = -(first + second)

            entropy_est = p_est_1 * entropy_est_1 + p_est_2 * entropy_est_2 + p_est_3 * entropy_est_3 + p_est_4 * entropy_est_4

        except:
            print()

        entropy_est_list = [entropy_est_1, entropy_est_2, entropy_est_3, entropy_est_4]
        entropy_list.append(entropy_est_list)
        my_dict = {k: v for k, v in zip(["0-10", "10-30", "30-60", ">60"], entropy_est_list)}
        entropy_value_list.append(my_dict)
        ig_est_list = [1 - entropy_est_1, 1 - entropy_est_2, 1 - entropy_est_3, 1 - entropy_est_4]
        ig_list.append(ig_est_list)
        my_dict_ig = {k: v for k, v in zip(["0-10", "10-30", "30-60", ">60"], ig_est_list)}
        ig_value_list.append(my_dict_ig)

        ####################

        # Output the entropy values of each attribute:

        # print("Alt Entropy(0): " + str(entropy_alt))
        # print("bar Entropy(1): " + str(entropy_bar))
        # print("fri Entropy(2): " + str(entropy_fri))
        # print("hun Entropy(3): " + str(entropy_hun))
        # print("Patron Entropy(4): " + str(entropy_patrons))
        # print("Price Entropy(5): " + str(entropy_price))
        # print("rain Entropy(6): " + str(entropy_rain))
        # print("res Entropy(7): " + str(entropy_res))
        # print("Type Entropy(8): " + str(entropy_type))
        # print("Est Entropy(9): " + str(entropy_est))

        attribute_list = ["alt", "bar", "fri", "hun", "patrons", "price", "rain", "res", "type", "est"]

        total_entropy_list = [entropy_alt, entropy_bar, entropy_fri, entropy_hun, entropy_patrons, entropy_price,
                              entropy_rain, entropy_res, entropy_type, entropy_est]

        entropy_attr_dict = {k: v for k, v in zip(attribute_list, total_entropy_list)}
        entropy_value_dict = {k: v for k, v in zip(attribute_list, entropy_value_list)}
        ig_value_dict = {k: v for k, v in zip(attribute_list, ig_value_list)}

        ig_attr_list = []

        count = 0
        for i in entropy_attr_dict.values():
            ig_attr_list.append(1 - i)
            count += 1
        ig_attr_dict = {k: v for k, v in zip(attribute_list, ig_attr_list)}

        EntropyCalculation.entropy_attr_dict = entropy_attr_dict
        EntropyCalculation.entropy_value_dict = entropy_value_dict
        EntropyCalculation.ig_attr_dict = ig_attr_dict
        EntropyCalculation.ig_value_dict = ig_value_dict

        return [entropy_attr_dict, entropy_value_dict, ig_attr_dict, ig_value_dict]


obj = EntropyCalculation()

data = pd.read_excel('../Dataset/data.xlsx')

# windows
# data = pd.read_excel('..\Dataset\data.xlsx')
dataset = data.values.tolist()
obj.entropy_calculation(dataset)

# Output the entropy values of each attribute
