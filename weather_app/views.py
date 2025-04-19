from django.shortcuts import render
import os
import pickle
import numpy as np


model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'rfp.pkl')
model = pickle.load(open(model_path, 'rb'))

def index(request):
    return render(request, 'weather_app/index.html')

def about(request):
    return render(request, 'weather_app/about.html')

def predict(request):
    return render(request, 'weather_app/predict.html')

def submit(request):
    if request.method == "POST":
        precipitation=float(request.POST['precipitation'])
        maxTemp=float(request.POST['maxTemp'])
        minTemp=float(request.POST['minTemp'])
        wind=float(request.POST['wind'])
        input_data = np.array([[precipitation, maxTemp, minTemp, wind]])
        result = model.predict(input_data)[0]  
        return render(request, 'weather_app/submit.html', {'result': result})
    return render(request, 'weather_app/predict.html')