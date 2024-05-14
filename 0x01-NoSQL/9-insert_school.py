#!/usr/bin/env python3
""" Insert a mongo document in python """


def insert_school(mongo_collection, **kwargs):
    """ function inserts a new document in a collection
    based on kwargs
    return the new _id
    """
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id

