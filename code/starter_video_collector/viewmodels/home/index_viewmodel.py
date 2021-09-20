from typing import List

import more_itertools

from models.category_model import Category
from services import video_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()

        self.categories: List[Category] = video_service.all_categories()
        self.rows = [
            list(row)
            for row in more_itertools.chunked(self.categories, 3)
        ]
