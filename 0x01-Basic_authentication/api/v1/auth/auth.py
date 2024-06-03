from flask import Flask
from typing import List, TypeVar


app = Flask(__name__)


class Auth:
    def __init__(self):
        self.users = {
            "admin": "admin",
            "user": "user",
        }

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str or None:
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar("User"):
        return None
