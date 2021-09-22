import time

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


@blueprint.get('/feed/more_videos/<int:page>')
@response(template_file='feed/partials/video_list.html')
def more_videos(page: int):
    time.sleep(.5)
    vm = FeedViewModel(page_size=VIDEOS_PER_PAGE, page=page)
    return vm.to_dict()
