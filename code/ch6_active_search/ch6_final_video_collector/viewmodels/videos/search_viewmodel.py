from viewmodels.shared.viewmodelbase import ViewModelBase


class SearchViewModel(ViewModelBase):
    def __init__(self, search_text: str):
        super().__init__()

        self.search_text = search_text
