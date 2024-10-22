#!/usr/bin/env python3
"""DB implementation"""


def list_all(mongo_collection):
    """List all documents"""
    return mongo_collection.find()
