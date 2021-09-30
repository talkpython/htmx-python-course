import flask

from infrastructure.view_modifiers import response
from services import video_service
from viewmodels.videos.add_video_viewmodel import AddVideoViewModel
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


@blueprint.get('/videos/add/<cat_name>')
@response(template_file='videos/partials/add_video_form.html')
def add_get(cat_name: str):
    vm = AddVideoViewModel(cat_name)
    return vm.to_dict()


@blueprint.post('/videos/add/<cat_name>')
def add_post(cat_name: str):
    vm = AddVideoViewModel(cat_name)
    vm.restore_from_form()

    video_service.add_video(cat_name, vm.id, vm.title, vm.author, vm.view_count)

    return flask.redirect(f'/videos/category/{cat_name}')


@blueprint.get('/videos/cancel_add/<cat_name>')
@response(template_file='videos/partials/show_add_form.html')
def cancel_add(cat_name: str):
    vm = AddVideoViewModel(cat_name)
    return vm.to_dict()
