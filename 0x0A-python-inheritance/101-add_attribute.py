#!/usr/bin/python3
def add_attribute(cls, field, name):
    if not hasattr(cls, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(cls, field, name)
