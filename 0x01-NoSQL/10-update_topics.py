#!/usr/bin/env python3
""" Update school topics
"""


def update_topics(mongo_collection, name, topics):
    """ function changes all topics of a school document
    based on the name """

    update = mongo_collection.update_many({"name": name},
            {"$set" : {"topics": topics}})
