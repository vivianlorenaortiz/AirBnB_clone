#!/usr/bin/python3
"""Review class that inherits from BaseModel."""

from models.base_model import BaseModel


class Review(BaseModel):
    """All the reviews in the app."""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """New reviews."""
    super().__init__(self, *args, **kwargs)
