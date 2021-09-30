from typing import Optional

from viewmodels.shared.viewmodelbase import ViewModelBase


class AddVideoViewModel(ViewModelBase):
    def __init__(self, cat_name: str):
        super().__init__()

        self.cat_name = cat_name
        self.id: Optional[str] = None
        self.title: Optional[str] = None
        self.author: Optional[str] = None
        self.view_count: Optional[int] = None

    def restore_from_form(self):
        d = self.request_dict
        self.title = d.get('title')
        self.author = d.get('author')
        self.id = d.get('id')
        self.view_count = int(d.get('view_count', 0))
