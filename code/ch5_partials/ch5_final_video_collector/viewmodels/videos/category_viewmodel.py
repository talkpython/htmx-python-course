from typing import Optional

import more_itertools

from models.category_model import Category
from models.video_model import Video
from services import video_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class CategoryViewModel(ViewModelBase):
    def __init__(self, cat_name: str):
        super().__init__()

        self.cat_name = cat_name
        self.category: Optional[Category] = video_service.category_by_name(cat_name)
        self.rows = [list(row) for row in more_itertools.chunked(self.category.videos, 3)]
        self.Video = Video
