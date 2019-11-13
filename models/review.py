#!/usr/bin/python3
"""Review class that inherits from BaseModel."""

from models.base_model import BaseModel


class Review(BaseModel):
    """All the reviews in the app."""

    place_id = ""
    user_id = ""
    text = ""
