from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
class Classification:
    def classification(self):
        X = [[True, False, False, True, 'Some', 3, False, True, 'French', 1],
 [True, False, False, True, 'Full', 1, False, False, 'Thai', 3],
 [False, True, False, False, 'Some', 1, False, False, 'Burger', 1],
 [True, False, True, True, 'Full', 1, True, False, 'Thai', 2],
 [True, False, True, False, 'Full', 3, False, True, 'French', 4],
 [False, True, False, True, 'Some', 2, True, True, 'Italian', 1],
 [False, True, False, False, 'None', 1, True, False, 'Burger', 1],
 [False, False, False, True, 'Some', 2, True, True, 'Thai', 1],
 [False, True, True, False, 'Full', 1, True, False, 'Burger', 4],
 [True, True, True, True, 'Full', 3, False, True, 'Italian', 2],
 [False, False, False, False, 'None', 1, False, False, 'Thai', 1],
 [True, True, True, True, 'Full', 1, False, False, 'Burger', 3]]

        Y = [True, False, True, True, False, True, False, True, False, False, False, True]
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1, random_state=42)
        model = LogisticRegression()
        model.fit(X_train, Y_train)

        # Step 5: Make predictions
        new_data = [True, False, False, True, 'Some', 3, False, True, 'French', 1]
        predicted_outcome = model.predict(new_data)

        print(predicted_outcome)
obj = Classification()
obj.classification()