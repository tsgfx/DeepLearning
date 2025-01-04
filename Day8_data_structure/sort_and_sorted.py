# 作者: 郭瑞超
# 2025年01月04日16时11分19秒
# grcsxb269@163.com
my_list = "This is a test string from Andrew".split()
print(my_list)

def change_lower(s):
    return s.lower()

# print(sorted(my_list, key=str.lower))
print(sorted(my_list, key=change_lower))

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
    ]
print(sorted(student_tuples, key=lambda x: x[0]))
print("-"*50)
class Student(object):
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        相对于__str__,更方便，可以返回非字符串类型
        :return:
        """
        return 'Student(name=%s, grade=%s, age=%s)' % (self.name, self.grade, self.age)

student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10)
    ]
print(sorted(student_objects, key=lambda x: x.name))
print("-"*50)
from operator import itemgetter, attrgetter # 导入itemgetter和attrgetter
print(sorted(student_tuples, key=itemgetter(0))) # 按第一个元素排序
print("-"*50)
print(sorted(student_objects, key=attrgetter('grade', 'age'))) # 先按grade排序，再按age排序
print(sorted(student_objects, key=attrgetter('grade', 'age'), reverse=True)) # 先按grade排序，再按age排序，降序
print(sorted(student_tuples, key=lambda x:(x[1], x[2]))) # 先按grade排序，再按age排序
print(sorted(student_tuples, key=lambda x:(x[1], -x[2]))) # 先按grade排序，再按age排序，降序
print("-"*50)
mydict = { 'Li' : ['M',7],
           'Zhang': ['E',2],
           'Wang' : ['P',3],
           'Du':['C',2],
           'Ma': ['C',9],
           'Zhe' : ['H',7] }
print(sorted(mydict.items(),key=lambda x:x[1]))
print("-"*50)
# 列表嵌套字典排序
gameresult = [
{ "name":"Bob", "wins":10, "losses":3, "rating":75.00 },
{ "name":"David", "wins":3, "losses":5, "rating":57.00 },
{ "name":"Carol", "wins":4, "losses":5, "rating":57.00 },
{ "name":"Patty", "wins":9, "losses":3, "rating":57.00}]
print(sorted(gameresult, key=lambda x:x['rating']))
