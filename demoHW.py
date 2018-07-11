#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.enron
messages = db.messages


def find():



    try:
        cursor = messages.find({"headers.From":"andrew.fastow@enron.com", "headers.To":"jeff.skilling@enron.com"})

    except Exception as e:
        print "Unexpected error:", type(e), e
    all_ids = []
    for doc in cursor:
        print(doc)
    print((cursor.count(True)))








if __name__ == '__main__':
    find()
