#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.school
students = db.students


def find():



    try:
        cursor = students.find({})
    except Exception as e:
        print "Unexpected error:", type(e), e
    all_ids = []
    for doc in cursor:
        min = float('inf')
        idx = None
        hw = doc['scores']
        for jdx, each_hw in enumerate(hw):
            if each_hw['type'] == 'homework' and each_hw['score']<=min:
                min = each_hw['score']
                idx = jdx
        doc['scores'].pop(idx)
        students.replace_one({'_id':doc['_id']}, doc)








if __name__ == '__main__':
    find()
