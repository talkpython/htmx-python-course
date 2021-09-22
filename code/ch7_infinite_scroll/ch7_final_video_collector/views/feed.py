import flask

from infrastructure.view_modifiers import response
from viewmodels.feed.feed_viewmodel import FeedViewModel

blueprint = flask.Blueprint('feed', __name__, template_folder='templates')

VIDEOS_PER_PAGE = 3


@blueprint.get('/feed')
@response(template_file='feed/index.html')
def index():
    vm = FeedViewModel(page_size=VIDEOS_PER_PAGE)
    return vm.to_dict()
