from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import StoreData
# Create your views here.

def index(request):
    return render(request, "index.html")

def result(request):
    arr=[]
    inp1 = request.POST['float-input1']
    inp2 = request.POST['float-input2']
    inp3 = request.POST['float-input3']
    url = requests.get(f"http://127.0.0.1:8080/prediction_api?LSTAT={inp1}&RM={inp2}&PTRATIO={inp3}")
    print(url.json()*1000)
    print(inp1, inp2, inp3)
    arr.append(inp1)
    arr.append(inp2)
    arr.append(inp3)
    # return render(request, 'result.html', {
        
    # })
    d = StoreData(lstat=inp1, rm=inp2, ptratio=inp3, prediction=url.json()*1000)
    d.save()
    return render(request, 'resultsfinal.html', {
            "val": url.json()*1000
            # "val":inp1
        })

# def final(request):
#     return render(request, 'resultsfinal.html', {
#         "val":50
#     })