import psycopg2

#para acessar o banco de dados, eu preciso de uma conexao.
#provê conexao com o banco de dados
def conectardb():
    con = psycopg2.connect(
        host='localhost',
        database='ifpbsubp4',
        user='postgres',
        password='12345'
    )
    return con

#verifica no banco de dados se existe um usuário com matrícula e a senha
#informadas por parâmetro
def verificarlogin(matricula, senha, conexao):

    cur = conexao.cursor()
    cur.execute(f"SELECT * FROM usuarios WHERE matricula = '{matricula}' AND senha = '{senha}'")
    recset = cur.fetchall()
    cur.close()
    conexao.close()

    return recset


def insert_comentario(login, comentario, conexao):

    cur = conexao.cursor()
    exito = False
    try:
        #mudar nome da tabela
        sql = (f"UPDATE usuario SET comentario = '{comentario}' where login = '{login}'")
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    cur.close()
    conexao.close()
    return exito

def inserirusuario(login, senha):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO usuario (login, senha) VALUES ('{login}', '{senha}')"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

def listarpessoas(opcao):
    conexao = conectardb()

    cur = conexao.cursor()
    cur.execute(f"SELECT * FROM usuario")
    recset = cur.fetchall()
    conexao.close()

    return recset
