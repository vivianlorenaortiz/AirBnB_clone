#!/usr/bin/python3
"""State class that inherits from BaseModel."""

from models.base_model import BaseModel


class State(BaseModel):
    """All the states available in the app."""

    name = ""
