import requests
from settings import HEADERS_API, ENDPOINT_PRODUTO
from flask import Blueprint, render_template
bp_produto = Blueprint('produto', __name__, url_prefix="/produto", template_folder='templates')

@bp_produto.route('/', methods=['GET', 'POST'])
def formListaProduto():
    try: 
        response = requests.get(ENDPOINT_PRODUTO, headers=HEADERS_API)
        result = response.json()
        
        if(response.status_code != 200):
            raise Exception(result[0])
        
        return render_template('formListaProduto.html', result=result[0])
    except Exception as e:
        return render_template('formListaProduto.html', msgCode=e.args[0])
 

@bp_produto.route('/form-produto/', methods=['GET'])
def formProduto():
    return render_template('formProduto.html')