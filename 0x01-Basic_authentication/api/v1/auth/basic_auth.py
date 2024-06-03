#!/usr/bin/env python3
"""Basic authentication for the API."""

from flask import Flask, jsonify, request, abort
from api.v1.auth.auth import Auth

app = Flask(__name__)


class BasicAuth(Auth):
    """Basic authentication for the API."""

    def __init__(self):
        """Initialize the class."""
        self.users = {"api": "api_key"}

    def extract_base64_authorization_header(self, authorization: str) -> str or None:
        """Extract the base64 authorization header."""
        if authorization is None or type(authorization) is not str:
            return None
        if not authorization.startswith("Basic "):
            return None
        return authorization[6:]
