# 作者: 郭瑞超
# 2025年01月03日09时49分36秒
# grcsxb269@163.com
import copy

def use_list_copy():
    a = [1, 2, 3]
    b = a.copy()
    b[0] = 10
    print(id(a), id(b))
    print(a)
    print(b)

def use_copy():
    c = [1, 2, 3]
    d = copy.copy(c)
    d[0] = 10
    print(id(c), id(d))
    print(c)
    print(d)

def use_copy2():
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d= copy.copy(c) # shallow copy
    print(id(a), id(b), id(c), id(d))
    a[0] = 10
    print(a, b, c, d)

def use_deep_copy():
    """
    递归copy,不管有多少层嵌套,都将所有元素都复制一遍
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(a), id(b), id(c), id(d))
    a[0] = 10
    print(a, b, c, d)

class Student:
    def __init__(self, name):
        self.name = name
        self.score = [ 80, 90, 95]

def use_own_object_copy():
    s1 = Student('Alice')
    s2 = copy.copy(s1)
    # 浅拷贝 不可变数据类型
    s2.name = 'Bob'
    # 浅拷贝 可变数据类型
    s1.score.append(85)
    print(s1.name, s2.name)
    print(s1.score, s2.score)
    # 深拷贝
    s3 = copy.deepcopy(s1)
    s3.score.append(90)
    print(s1.score,s3.score)

if __name__ == '__main__':
    # use_list_copy()
    # use_copy()
    # use_copy2()
    # use_deep_copy()
    use_own_object_copy()