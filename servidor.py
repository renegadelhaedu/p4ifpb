#importando o flask
from flask import *

#criando o servidor flask (back-end)
app = Flask(__name__)

@app.route('/')
def pageprincipal():
    return render_template('homepage.html')

#iniciando/rodando o servidor
app.run()