#importando o flask
from flask import *


#criando o servidor flask (back-end)
app = Flask(__name__)

@app.route('/')
def pageprincipal():
    return render_template('thaynaraifpb.html')


@app.route('/inserir')
def inserir_user():
    login = request.form.get('')

@app.route('/login')
def login():
    login = request.form.get('senha')
    senha = request.form.get('login')


#iniciando/rodando o servidor
app.run(debug=True)