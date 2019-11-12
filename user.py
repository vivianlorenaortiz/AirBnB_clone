#!/usr/bin/python3
"""
User class that inherits from BaseModel."""

from models.base_model import BaseModel


class User(BaseModel):
    """Users of the app."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """New user init method."""
        super().__init__(self, *args, **kwargs)
