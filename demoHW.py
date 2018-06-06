#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.students
stories = db.grades


def find():



    try:
        cursor = stories.find({}, {'student_id':1, '_id':0}).sort('student_id',1)
    except Exception as e:
        print "Unexpected error:", type(e), e
    all_ids = []
    for doc in cursor:
        for key in doc:
            all_ids.append(doc[key])
    all_ids_uniq =  list(set(all_ids))

    for student in all_ids_uniq:
        try:
            cursor = stories.find({'student_id':student, 'type':'homework'}).sort('score', 1).limit(1)

        except Exception as e:
            print "Unexpected error:", type(e), e
        for doc in cursor:
            print(doc)
            # print(doc['_id'])
            obj_id = doc['_id']
            try:
                cursor = stories.delete_one({'_id':obj_id})
            except Exception as e:
                print "Unexpected error:", type(e), e


if __name__ == '__main__':
    find()
