#!/usr/bin/env python3
"""Basic authentication for the API."""

from flask import Flask
from api.v1.auth.auth import Auth
from typing import TypeVar

app = Flask(__name__)


class BasicAuth(Auth):
    """Basic authentication for the API."""

    def __init__(self):
        """Initialize the class."""
        self.users = {"api": "api_key"}

    def extract_base64_authorization_header(self, authorization: str) -> str or None:
        """Extract the base64 authorization header."""
        if isinstance(authorization, str) is False:
            return None
        if not authorization.startswith("Basic "):
            return None
        return authorization[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Decode the base64 authorization header."""
        if isinstance(base64_authorization_header, str) is False:
            return None
        try:
            return base64_authorization_header.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> tuple:
        """Extract the user credentials."""
        if isinstance(decoded_base64_authorization_header, str) is False:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> str or None:
        """Get the user object from the credentials."""
        if user_email is None or user_pwd is None:
            return None
        if user_email not in self.users.keys():
            return None
        if self.users[user_email] != user_pwd:
            return None
        return user_email

    def current_user(self, request=None) -> TypeVar("User"):
        """Get the current user."""
        auth_header = self.authorization_header(request)
        base64_header = self.extract_base64_authorization_header(auth_header)
        decoded_header = self.decode_base64_authorization_header(base64_header)
        user_credentials = self.extract_user_credentials(decoded_header)
        return self.user_object_from_credentials(
            user_credentials[0], user_credentials[1]
        )
