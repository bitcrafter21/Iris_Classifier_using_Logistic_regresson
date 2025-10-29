# iris_logistic_regression_input.py

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load dataset and train model
iris = load_iris()
X, y = iris.data, iris.target

model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Prompt user for input
print("Enter the following flower features:")
sepal_length = float(input("Sepal length (cm): "))
sepal_width  = float(input("Sepal width (cm): "))
petal_length = float(input("Petal length (cm): "))
petal_width  = float(input("Petal width (cm): "))

# Predict
features = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(features)[0]
predicted_class = iris.target_names[prediction]

print(f"\nPredicted Iris species: {predicted_class}")