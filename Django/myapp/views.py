from django.shortcuts import render
import os
import pickle

# Create your views here.
def index(request):
    if request.method=='POST':
        pt=float(request.POST['pt'])
        maxt=float(request.POST['maxt'])
        mint=float(request.POST['mint'])
        wind=float(request.POST['wind'])
        path=os.path.dirname(__file__)
        model=pickle.load(open(os.path.join(path,'rfp.pkl'),'rb'))
        res=model.predict([[pt,maxt,mint,wind]])[0]
        #print(res)
        return render(request,"index.html",{"res":res})
    return render(request,"index.html")