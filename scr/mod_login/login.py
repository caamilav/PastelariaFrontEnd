from functools import wraps
from flask import Blueprint, jsonify, redirect, render_template, request, url_for, session
import requests
from settings import ENDPOINT_LOGIN, HEADERS_API
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
        
        payload = {'cpf': cpf, 'senha': senha}
        
        response = requests.post(ENDPOINT_LOGIN, headers=HEADERS_API, json=payload)
        result = response.json()
        print(result)
        
        if (response.status_code != 200):
            raise Exception("Falha no login! Verifique seus dados e tente novamente!")
        else:
          guardaDadosSessao(result)
          return redirect(url_for('index.formIndex'))
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


def guardaDadosSessao(result):
    session['login'] = result[0].get('cpf')
    session['nome'] = result[0].get('nome')
    session['grupo'] = result[0].get('grupo')

