from flask import Flask,render_template,request
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

app = Flask(__name__)

@app.route("/")
def iris():
    if request.method=="POST":
        sepal_length = float(request.form["sepalLength"])
        sepal_width  = float(request.form["sepalWidth"])
        petal_length = float(request.form["petalLength"])
        petal_width  = float(request.form["petalWidth"])

        iris = load_iris()
        X, y = iris.data, iris.target

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, target_names=iris.target_names)

        features = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = model.predict(features)[0]
        predicted_class = iris.target_names[prediction]

        return render_template("index.html", prediction=predicted_class, accuracy=accuracy, report=report)
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)