from {{cookiecutter.project_slug}}.http import HTTP


class {{cookiecutter.project_facade}}:
    def __init__(self, token: str):
        self.http = HTTP(token=token)
