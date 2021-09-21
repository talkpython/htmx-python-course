from viewmodels.shared.viewmodelbase import ViewModelBase


class SearchViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()

        self.search_text: str = self.request_dict.get('search_text')
