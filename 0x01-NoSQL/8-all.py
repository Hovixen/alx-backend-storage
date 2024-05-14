#!/usr/bin/env python3
""" Listing all documents in Python """


def list_all(mongo_collection):
    """ function lists all documents in a collection
    return an empty list if no document in a the collection
    """
    return mongo_collection.find()
