import requests

data = requests.get('http://127.0.0.1:8080/prediction_api?LSTAT=5.0&RM=6.5&PTRATIO=15.3')
data_print = data.json()
print(data_print)