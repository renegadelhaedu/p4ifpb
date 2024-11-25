#importando o flask
from flask import *
import dao

usuarios = [['rene','1234','rene sousa'],
            ['maria','6543', 'maria do carmo'],
            ['evellyn','teste','Evellyn Melo']]

#criando o servidor flask (back-end)
app = Flask(__name__)

@app.route('/')
def pageprincipal():
    return render_template('homeifpb.html')

@app.route('/inserirnovadisciplina', methods=['POST'])
def cadastrar_disciplina():
    nome_disc = request.form.get('nomedisciplina')
    print('a disciplina foi: ', nome_disc)
    return '<h1>Disciplina inserida com Sucesso!</h1>'
    #tem que fazer uma página html para exibir o retorno


@app.route('/adicionardisciplina')
def aaa():
    return render_template('adicionardisciplina.html')

@app.route('/inseriraluno', methods=['POST'])
def inserir_user():
    login = request.form.get('login')
    senha = request.form.get('senha1')
    nome = request.form.get('nome')

    #variável na memória ram
    usuarios.append([login, senha, nome])

    msg = 'Usuário cadastrado com sucesso'
    return render_template('homeifpb.html', mensagem=msg)


@app.route('/login', methods=['POST'])
def login():
    login = request.form.get('login')
    senha = request.form.get('senha')

    resultado = dao.verificarlogin(login, senha, dao.conectardb())
    print(resultado)
    if len(resultado) > 0:
        return render_template('homepagealuno.html', user=resultado[0][1])
    else:
        msg = 'Senha ou login incorretos'
        return render_template('homeifpb.html', msglogin=msg)


#iniciando/rodando o servidor
app.run(debug=True)