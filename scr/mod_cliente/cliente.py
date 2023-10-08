from flask import Blueprint, render_template
bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

@bp_cliente.route('/', methods=['GET', 'POST'])
def formListaCliente():
    return render_template('formListaCliente.html')

@bp_cliente.route('/form-cliente/', methods=['GET'])
def formCliente():
    return render_template('formCliente.html')