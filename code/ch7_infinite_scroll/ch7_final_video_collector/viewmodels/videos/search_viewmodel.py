from typing import List

from models.video_model import Video
from services import video_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class SearchViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()

        self.search_text: str = self.request_dict.get('search_text')
        self.videos: List[Video] = []

        if self.search_text and self.search_text.strip():
            self.videos = video_service.search_videos(self.search_text)
