from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
import numpy as np

class Classification:

    def classification(self, X, Y, user_input):

        # Convert boolean values to integers
        X = [[int(val) if isinstance(val, bool) else val for val in row] for row in X]

        # Separate string features for ordinal encoding
        i = 0
        j = 0
        string_features = []
        while i < 12:
            while j < 12:
                try:
                    string_features = [[row[i], row[j]] for row in X]
                except:
                    print()
                j += 1
            i += 1

        # Ordinal encode string features
        ordinal_encoder = OrdinalEncoder()
        string_features_encoded = ordinal_encoder.fit_transform(string_features)

        # Convert categorical features to one-hot encoding
        categorical_indices = [4, 8]  # Indices of categorical columns in X
        onehot_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        X_categorical = onehot_encoder.fit_transform(string_features_encoded)

        # Combine encoded categorical features with remaining numerical features
        X_encoded = np.concatenate((np.delete(X, categorical_indices, axis=1), X_categorical), axis=1)

        X_train, X_test, Y_train, Y_test = train_test_split(X_encoded, Y, test_size=0.2, random_state=42)

        model = LogisticRegression()
        model.fit(X_train, Y_train)

        # Step 5: Make predictions
        # new_data = [[True, False, False, True, 'Full', 1, False, False, 'Thai', 3]]
        new_data = [user_input]
        new_data = [[int(val) if isinstance(val, bool) else val for val in row] for row in new_data]


        new_string_features = [[row[4], row[8]] for row in new_data]
        new_string_features_encoded = ordinal_encoder.transform(new_string_features)
        new_data_categorical = onehot_encoder.transform(new_string_features_encoded)

        new_data_encoded = np.concatenate((np.delete(new_data, categorical_indices, axis=1), new_data_categorical), axis=1)

        predicted_outcome = model.predict(new_data_encoded.astype(float))

        return predicted_outcome

# X = [[True, False, False, True, 'Some', 3, False, True, 'French', 1],
#     [True, False, False, True, 'Full', 1, False, False, 'Thai', 3],
#     [False, True, False, False, 'Some', 1, False, False, 'Burger', 1],
#     [True, False, True, True, 'Full', 1, True, False, 'Thai', 2],
#     [True, False, True, False, 'Full', 3, False, True, 'French', 4],
#     [False, True, False, True, 'Some', 2, True, True, 'Italian', 1],
#     [False, True, False, False, 'None', 1, True, False, 'Burger', 1],
#     [False, False, False, True, 'Some', 2, True, True, 'Thai', 1],
#     [False, True, True, False, 'Full', 1, True, False, 'Burger', 4],
#     [True, True, True, True, 'Full', 3, False, True, 'Italian', 2],
#     [False, False, False, False, 'None', 1, False, False, 'Thai', 1],
#     [True, True, True, True, 'Full', 1, False, False, 'Burger', 3]]
#
# Y = [True, False, True, True, False, True, False, True, False, False, False, True]
# obj = Classification()
# print(obj.classification(X, Y, [True, False, False, True, 'Full', 1, False, False, 'Thai', 3]))
# # True, False, False, True, Full, 1, False, False, Thai, 3