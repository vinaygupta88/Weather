from flask import Flask, render_template, request
import os
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'rfp.pkl')
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        # Get form data
        precipitation = float(request.form['precipitation'])
        maxTemp = float(request.form['maxTemp'])
        minTemp = float(request.form['minTemp'])
        wind = float(request.form['wind'])

        # Prepare input data for prediction
        input_data = np.array([[precipitation, maxTemp, minTemp, wind]])
        
        # Make prediction using the model
        result = model.predict(input_data)[0]
        
        # Pass the result to the submit page
        return render_template('submit.html', result=result)

    return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug=True)

"""
Project: Weather Prediction Prediction using ML
Developer: Vinay
Year: 2025
"""
