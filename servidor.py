#importando o flask
from flask import *

usuarios = [['rene','1234','rene sousa'],
            ['maria','6543', 'maria do carmo'],
            ['evellyn','teste','Evellyn Melo']]

#criando o servidor flask (back-end)
app = Flask(__name__)

@app.route('/')
def pageprincipal():
    return render_template('homeifpb.html')

@app.route('/a')
def aaa():
    return '<h1>teste ok</h1>'

@app.route('/inseriraluno', methods=['POST'])
def inserir_user():
    login = request.form.get('login')
    senha = request.form.get('senha1')
    nome = request.form.get('nome')

    usuarios.append([login, senha, nome])
    msg = 'Usuário cadastrado com sucesso'
    return render_template('homeifpb.html', mensagem=msg)


@app.route('/login', methods=['POST'])
def login():
    login = request.form.get('login')
    senha = request.form.get('senha')
    logado = False

    for user in usuarios:
        if login == user[0] and senha == user[1]:
            logado = True
            break

    if logado:
        return render_template('homepagealuno.html', user=login)
    else:
        msg='Senha ou login incorretos'
        return render_template('homeifpb.html', msglogin=msg)

#iniciando/rodando o servidor
app.run(debug=True)