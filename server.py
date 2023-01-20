from flask import Flask, request, Response

colaboradores = [
    {'nome': 'Fabrício', 'cargo': 'Developer', 'remuneracao': 4000},
    {'nome': 'Thiago', 'cargo': 'Developer', 'remuneracao': 5500},
    {'nome': 'Enzo', 'cargo': 'Developer', 'remuneracao': 8000},
    {'nome': 'Gabriel', 'cargo': 'Developer', 'remuneracao': 2500},
    {'nome': 'Patricia', 'cargo': 'SoftwareDev', 'remuneracao': 12000},
    {'nome': 'Ana', 'cargo': 'SoftwareDev', 'remuneracao': 15000},
    {'nome': 'Daiane', 'cargo': 'SwiftDev', 'remuneracao':6000},
    {'nome': 'Igor', 'cargo': 'KotlinDev', 'remuneracao': 10000},
    {'nome': 'Jaqueline', 'cargo': 'CloudDev', 'remuneracao': 6500},
    {'nome': 'Leonardo', 'cargo': 'JavaDev', 'remuneracao': 11000},
    {'nome': 'Pietro', 'cargo': 'FullSatackDev', 'remuneracao': 16500},
]

users = [
    {"username":"Gustavo", "secret":"@admin2023"}
]

def check_user(username, secret):
    for user in users:
        if(user["username"] == username) and (user["secret"] == secret):
            return True
    return False

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home Page<h1>"

@app.route("/colaboradores")
def get_colaboradores():
    return{'colaboradores': colaboradores}

@app.route("/colaboradores/<cargo>")
def get_colaboradores_cargo(cargo):
    out_colaboradores = []
    for colaborador in colaboradores:
        if cargo == colaborador['cargo'].lower():
            out_colaboradores.append(colaborador)
    return {'colabradores': out_colaboradores}

@app.route("/colaboradores/<info>/<value>")
def get_colaboradores_info(info, value):
    out_colaboradores = []
    for colaborador in colaboradores:
        if info in colaborador.keys():
            value_colaborador = colaborador[info]

            if type(value_colaborador) == str:
                if value == value_colaborador.lower():
                    out_colaboradores.append(colaborador)

            if type(value_colaborador) == int:
                if int(value) == value_colaborador:
                    out_colaboradores.append(colaborador)
    return {'colaboradores': out_colaboradores}

@app.route("/informations", methods=['POST'])
def get_colaboradores_post():

    username = request.form['username']
    secret = request.form['secret']

    if not check_user(username, secret):
        # 401 HTTP Unauthorized
        return Response("Unauthorized", status=401)

    info = request.form['info']
    value = request.form['value']

    out_colaboradores = []
    for colaborador in colaboradores:
        if info in colaborador.keys():
            value_colaborador = colaborador[info]

            if type(value_colaborador) == str:
                if value == value_colaborador.lower():
                    out_colaboradores.append(colaborador)

            if type(value_colaborador) == int:
                if int(value) == value_colaborador:
                    out_colaboradores.append(colaborador)
    return{'colaboradores': out_colaboradores}

if __name__=="__main__":
    app.run(debug=True)