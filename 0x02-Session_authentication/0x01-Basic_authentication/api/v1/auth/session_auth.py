#!/usr/bin/env python3
"""This module contains the session authentication logic"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
from flask import request
from os import getenv()
