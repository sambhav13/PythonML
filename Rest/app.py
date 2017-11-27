import numpy as np
from flask import Flask, abort, jsonify, request, render_template
import _pickle as pickle

import sys
import json
#machine learning code
from sklearn import tree
features = [[140,1] , [130,1], [150,1], [170,1]]
labels = [0,0,1,1]

clf = tree.DecisionTreeClassifier()
clf.fit(features,labels)
print(clf.predict([[150,0]]))



pickle.dump(clf, open("D:\\img\\models\\clf.pkl","wb"))

random_forest_model = pickle.load(open("D:\\img\\models\\clf.pkl","rb"))

print(random_forest_model.predict([[150,0]]))


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/predict_api', methods=['POST'])
def predict():
    # Error checking
    data = request.get_json(force=True)

    print("data --> " +str(data))
    #predict_request1 = [data['dl']]
    #print(predict_request1)

    result = json.loads(str(data))
    print("result --> " + str(result) )
    predict_request = np.array(result)

    # Predict using the random forest model
    y = random_forest_model.predict([predict_request])

    # Return prediction
    output = "{"+str(y[0])+"}"
    print("prediction:"+str(output))
    return jsonify(results=output)


    sys.exit(0)
    # Convert JSON to numpy array
    predict_request = [data['sl'],data['sw'],data['pl'],data['pw']]
    predict_request = np.array(predict_request)

    # Predict using the random forest model
    y = random_forest_model.predict(predict_request)

    # Return prediction
    output = [y[0]]
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 9000, debug = True)