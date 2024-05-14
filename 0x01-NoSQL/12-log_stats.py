#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient


if __name__ == '__main__':
    """ script provides some stats about Nginx logs stored in MongoDB """

    client = MongoClient('mongodb://localhost:27017')
    d_base = client.logs.nginx
    count = d_base.count_documents({})
    print("{} logs".format(count))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        all_method = d_base.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, all_method))
    path = d_base.count_documents({"path": "/status"})
    print("{} status check".format(path))
