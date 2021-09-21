from typing import Optional

import flask
from flask import Request

from infrastructure import request_dict


class ViewModelBase:
    def __init__(self):
        self.request: Request = flask.request
        self.request_dict = request_dict.create('')

        self.error: Optional[str] = None
        self.view_model = self.to_dict()

    def to_dict(self):
        return self.__dict__
