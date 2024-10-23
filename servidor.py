#importando o flask
from flask import *

convidados = ['jose','maria','pedro','ana','thais','carla','joaquim']

#criando o servidor flask (back-end)
app = Flask(__name__)

@app.route('/')
def pageprincipal():
    return render_template('thaynaraifpb.html')

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