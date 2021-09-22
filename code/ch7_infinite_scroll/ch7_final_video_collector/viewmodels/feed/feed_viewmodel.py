from typing import List

from models.video_model import Video
from services import video_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class FeedViewModel(ViewModelBase):
    def __init__(self, page_size: int, page: int = 1):
        super().__init__()

        self.page_size = page_size
        self.page = page

        all_videos = video_service.all_videos()
        start = (page - 1) * page_size
        end = start + page_size

        self.videos: List[Video] = all_videos[start:end]
        self.has_more_videos = len(all_videos) > end
