from flask import Blueprint, render_template
bp_index = Blueprint('/', __name__, url_prefix="/", template_folder='templates')

@bp_index.route('/')
def index():
    return render_template('index.html'), 200