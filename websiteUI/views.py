from django.shortcuts import render
from django.http import HttpResponse
import requests
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
    return render(request, 'result.html', {
        "val": url.json()*1000
        # "val":inp1
    })