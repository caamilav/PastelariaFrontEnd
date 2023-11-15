from functools import wraps
from flask import Blueprint, jsonify, redirect, render_template, request, url_for, session
from shared.funcoes import Funcoes

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')

@bp_login.route('/', methods=['GET', 'POST'])
def login():
    return render_template("formLogin.html")


@bp_login.route('/login', methods=['POST'])
def validaLogin():
    try:
        cpf = request.form['usuario']
        senha = Funcoes.cifraSenha(request.form['senha'])
        
        if(cpf == 'abc' and senha == Funcoes.cifraSenha('Bolinhas')):
            session['login'] = cpf
            return redirect(url_for('index.formIndex'))
        else:
            raise Exception("Falha no login! Verifique seus dados e tente novamente!")
            
    except Exception as e:
        return jsonify(erro=True, msgErro=e.args[0])

@bp_login.route("/logoff", methods=['GET'])
def logoff():
    session.pop('login', None)
    session.clear()
    return redirect(url_for('login.login'))


def validaSessao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'login' not in session:
         # descarta os dados copiados da função original e retorna a tela de login
         return redirect(url_for('login.login', msgErro='Usuário não logado!'))
        else:
         # retorna os dados copiados da função original
         return f(*args, **kwargs)
    # retorna o resultado do if acima
    return decorated_function