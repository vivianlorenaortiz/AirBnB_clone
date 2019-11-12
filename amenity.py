#!/usr/bin/python3
"""Amenity class that inherits from BaseModel."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """All the amenities from the app."""

    name = ""

    def __init__(self, *args, **kwargs):
        """new amenity"""
        super().__init__(self, *args, **kwargs)
