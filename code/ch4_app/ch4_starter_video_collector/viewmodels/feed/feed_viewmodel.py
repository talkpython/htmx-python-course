from typing import List

from models.video_model import Video
from services import video_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class FeedViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()

        self.videos: List[Video] = video_service.all_videos()
