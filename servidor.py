#importando o flask
from flask import *

usuarios = []

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

@app.route('/verificarconvite', methods =['POST'])
def verificar_convite():
    #receber um dado vindo de um formulário
    nome = request.form.get('nomeuser')
    idade = int(request.form.get('idadeuser'))
    if nome in convidados and idade >= 18:
        return render_template('sim.html')
    else:
        return render_template('nao.html')


#iniciando/rodando o servidor
app.run(debug=True)