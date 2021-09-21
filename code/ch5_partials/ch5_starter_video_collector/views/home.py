import flask

from infrastructure.view_modifiers import response
from viewmodels.home.index_viewmodel import IndexViewModel

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.get('/')
@response(template_file='home/index.html')
def index():
    vm = IndexViewModel()
    return vm.to_dict()
