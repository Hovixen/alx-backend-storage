#!/usr/bin/env python3
""" list of the schools """


def schools_by_topic(mongo_collection, topic):
    """ function returns the list of school having a specific topic """
    # school = []
    return [school for school in mongo_collection.find({"topics": topic})]
