import flask

from infrastructure.view_modifiers import response
from viewmodels.videos.category_viewmodel import CategoryViewModel
from viewmodels.videos.play_viewmodel import PlayViewModel

blueprint = flask.Blueprint('videos', __name__, template_folder='templates')


@blueprint.get('/videos/category/<cat_name>')
@response(template_file='videos/category.html')
def category(cat_name: str):
    vm = CategoryViewModel(cat_name)
    return vm.to_dict()


@blueprint.get('/videos/play/<video_id>')
@response(template_file='videos/play.html')
def play(video_id: str):
    vm = PlayViewModel(video_id)
    return vm.to_dict()
