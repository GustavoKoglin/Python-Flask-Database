import requests

data = {"username":"Gustavo", "secret":"@admin2023", "info":"remuneracao", "value":"developer"}
response = requests.post("http://127.0.0.1:5000/informations", data=data)

if response.status_code == 200:
    message = response.json()
    print(message['colaboradores'])
else:
    print(response.status_code)