#!/usr/bin/env python3
"""
Connect to MongoDB and retrieve statistics about Nginx logs
"""

from pymongo import MongoClient

def get_nginx_stats():
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Number of documents in the collection
    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")

    # Methods statistics
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Number of documents with method=GET and path=/status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    get_nginx_stats()

