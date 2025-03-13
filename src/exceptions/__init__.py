from flask import abort


class Error(Exception):
    def __init__(self, message):
        self.message = message
        self.error()

    def error(self):
        abort(404, description=self.message)
