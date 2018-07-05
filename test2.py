""" pip install mongoengine """

# from mongoengine import connect, Document, EmbeddedDocument, \
#     StringField, IntField, FloatField, ListField, EmbeddedDocumentField

from mongoengine import *

connect('students')

SEX_CHOICES = (
    ('male', '男',)
    ('female', '女')
)


class Grade(EmbeddedDocument):
    ''' 成功 '''
    name = StringField(required=True)
    score = FloatField(required=True)


class Student(Document):
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    sex = StringField(required=True,choices=SEX_CHOICES)
    address = StringField()
    grade = ListField(StringField())
    comments = ListField(EmbeddedDocumentField(Grade))

    meta = {
        'collection': 'students',
        # 'ordering':['-age'], # 倒叙排序
    }


class TestMongoEngine(object):

    def add_one(self):
        """ 添加一条数据到数据库 """
        yunwen = Grade(
            name='语文',
            score=90
        )
        shuxue = Grade(
            name='数学',
            score=100
        )
        stu_obj = Student(
            name='张三5',
            age=15,
            sex='male',
            grades=[yunwen, shuxue]
        )
        stu_obj.remark = 'remark'
        stu_obj.save()
        return stu_obj

    def get_one(self):
        return Student.objects.first()


def main():
    obj = TestMongoEngine()

    # rest = obj.get_one()
    # print(rest.id)
    # print(rest.name)

    # rest = obj.add_one()
    # print(rest.pk)
    # print(rest.id)


if __name__ == '__main__':
    main()
