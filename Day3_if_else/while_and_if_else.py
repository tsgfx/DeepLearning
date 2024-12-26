# 作者: 郭瑞超
# 2024年12月26日09时37分01秒
# grcsxb269@163.com
def use_for():
    """
    练习使用循环
    :return:
    """
    mylist = ['a', 'b', 'c']
    for i in mylist:
        print(i, end=' ')


def test(num):
    print(f'num={num},num的地址{id(num)}')
    num = 5
    print(f'num={num},num的地址{id(num)}')


def unchangeable_type():
    """
    不可变类型
    :return:
    """
    a = 10
    print(f'调用函数前a的地址{id(a)}')
    test(a)
    print(f'调用函数后a的值{a}')
    print(f'调用函数后a的地址{id(a)}')


def changeable_type(new_list):
    """
    可变类型
    :return:
    """
    #new_list[0] = 10
    new_list = ['a', 'b', 'c'] # new_list 开始指向一个新的对象，而 my_list 仍然指向原来的列表 [1, 2, 3]


def test_changeable_type():
    my_list = [1, 2, 3]
    print(f'调用前{my_list}')
    print(f"调用前地址{id(my_list)}")
    changeable_type(my_list) # 对原有对象进行操作，地址不变
    print(f'调用后{my_list}')
    print(f"调用后地址{id(my_list)}")
    my_list = ['a', 'b', 'c'] # 创建了新对象，地址会变
    print(f"现在的地址{id(my_list)}")

def local_variable_and_global_variable():
    # print(num)
    pass


# use_for()
# unchangeable_type()
# test_changeable_type()
# num = 10
# local_variable_and_global_variable()
