# 作者: 郭瑞超
# 2024年12月27日10时32分09秒
# grcsxb269@163.com
def tuple_practice():
    info_tuple = (1, 1.23, 'a', "HELLO")
    print(info_tuple)
    print(type(info_tuple))
    print(len(info_tuple))
    print(info_tuple[0])
    # 单元素元组，要加逗号
    single_tuple = (1,)
    for item in single_tuple:
        print(item)

def tuple_to_list():
    a = (1, 2, 3, "a", "hello")
    l = list(a)
    print(l)

# 字典
def dictionary_practice():
    dic = {"name": "zhangsan"}
    print(dic)
    print(type(dic))
    print(dic["name"])
    dic['age'] = 18
    print(dic)
    re = dic.pop("age") #返回值是键对应的值
    print(dic)
    print(re)
    new_dic = {"name1": "Lisi", "age": 16, "name2": "zhangsan"}
    dic.update(new_dic)
    print(dic)
    new_dic.setdefault("name3", "zhangsan")
    new_dic.setdefault("name1", "zhangsan")
    print(new_dic)
    print('-'*50)
    for item in dic:
        print(f" {item}: {dic[item]}")
    for kv in dic.items():
        print(kv)
    # 键
    for k in dic.keys():
        print(k)
    # 值
    for v in dic.values():
        print(v)
    # 嵌套
    card_list = [{"name": "zhangsan", "age": 16},{"name": "lisi", "age": 17}]
    print(card_list)
    for card in card_list:
        print(card)

def str_operate():
    s1 = "sadfbsa djsadhj sjadaj"
    print(s1.split(' '))
    s2 = "sdsad\nsadasd\ndasasd\n"
    print(s2.splitlines())
    s3 = ['a','b','c','d']
    print(','.join(s3))
    print(s2.splitlines(keepends=True))

def study_r():
    """
    \r和\n的区别
    :return:
    """
    s = "abc\rd" # d
    print(s)
    a = "abc\nd"
    print(a)

def str_slice():
    num_str = "0123456789"
    print(num_str[:5])
    print(num_str[5:])
    print(num_str[:])
    print(num_str[::2]) # 开始 结束 步长
    print(num_str[1::2])
    print(num_str[2:-1])
    print(num_str[-2:])
    print(num_str[-2:-1])
    print(num_str[::-1]) # 逆序
    print(num_str[::-2])

def list_slice():
    my_list = list("0123456789")
    print(my_list)
    print(str(my_list))

def set_practice():
    """
    集合练习
    :return:
    """
    set1 = set()
    print(type(set1))
    fruit = {"apple", "banana", "cherry"}
    fruit.add("pear")
    print(fruit)
    x = fruit.copy()
    print(x)
    computer = {"apple", "google", "microsoft"}
    z = fruit.difference(computer)
    print(z)
    fruit.difference_update(computer)
    print(fruit)
    fruit.discard("cherry")
    print(fruit)
    x = {1, 2, 3}
    y = {1, 2, 3, 4, 5}
    z = {3, 4, 5, 6, 7}
    k = {6, 4, 3}
    res = x.intersection(y, z, k)
    print(res)
    x.intersection_update(y,z,k)
    print(x)
    print(y.isdisjoint(z))
    print(x.issubset(y))
    print(y.issuperset(x))
    print(1 in y)
    print(2 in x)
def use_set():
    x = {1, 2, 3, 4, 5}
    y = {4, 5, 6, 7, 8}
    print(x-y)
    print(x|y)
    print(x^y)
    print(x&y)

def use_generator():
    """
    生成式
    :return:
    """
    my_tuple = tuple(x for x in range(10))
    print(my_tuple)
    my_set = {x for x in "asdsadsasaf" if x not in "abc"}
    print(my_set)
    print(len(my_set))
    print(len(my_tuple))

def public_operate():
    # 切片插入
    test_list = [1, 2, 3, 4, 5, 6]
    test_list[3:3] = ['x', 'y', 'z']
    print(test_list)
    print(test_list+test_list)
    print(test_list*2)
    print([9] > test_list)

def list_compare():
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b)
    print(id(a) == id(b))

def use_method():
    """
    容器的方法
    :return:
    """
    a = (1, 2, 3)
    b = ('a', 'b', 'c')
    print(list(zip(a, b))) # [(1, 'a'), (2, 'b'), (3, 'c')]
    print(dict(zip(a, b))) # {1: 'a', 2: 'b', 3: 'c'}
    # 键值拆包
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list1 = list(enumerate(seasons))  # 编号
    print(list1)
    # 转为字典
    my_dic = dict(list1)
    print(my_dic)
    # 键值拆包，反转
    print({v:k for k,v in my_dic.items()})



if __name__ == '__main__':
    # dictionary_practice()
    # tuple_practice()
    # tuple_to_list()
    # str_operate()
    # study_r()
    # str_slice()
    # list_slice()
    # set_practice()
    # use_set()
    # use_generator()
    # public_operate()
    # list_compare()
    use_method()
