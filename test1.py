from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId

"""conda install pymongo"""
class TestMongo(object):
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['blog']

    def add_one(self):
        """ 新增数据 """
        post = {
            'title': '新的标题',
            'content': '博客的内容...',
            'created_at': datetime.now()
        }
        return self.db.blog.insert_one(post)

    def get_one(self):
        """ 查询一条数据 """
        return self.db.blog.find_one()

    def get_more(self):
        """ 查询多条数据 """
        return self.db.blog.find()

    def get_from_oid(self, oid):
        """ 根据记录的ID来获取数据 """
        return self.db.blog.find_one({'_id': ObjectId(oid)})


def main():
    obj = TestMongo()

    oid = '5b3e594abab5b5196ca6dc2c'
    rest = obj.get_from_oid(oid)
    print(type(rest))
    print(rest)

    # rest = obj.get_more()
    # for item in rest:
    #     print(type(item))
    #     print(item['_id'])

    # rest = obj.get_one()
    # print(type(rest))
    # print(rest['_id'])

    # rest = obj.add_one()
    # print(rest.inserted_id)


if __name__ == '__main__':
    main()
