# 作者: 郭瑞超
# 2024年12月26日17时18分06秒
# grcsxb269@163.com
# 有7个整数，其中有3个数出现了两次，1个数出现了一次， 找出出现了一次的那个数。
def find_num_once():
    num_list = [3, 2, 3, 4, 4, 7, 7]
    count_list = [0] * (max(num_list) + 1)
    for num in num_list:
        count_list[num] += 1
    for i in range(0, len(count_list)):
        if count_list[i] == 1:
            print(i)
def new_fun():
    list = [2, 3, 1, 6, 3, 2, 6]
    res = 0
    for i in list:
        res = res ^ i
    print(res)
# 写一个简单的for循环，从1打印到20，横着打为1排
def print_num_list():
    for i in range(1,21):
        print(i, end=' ')
# 写一个say_hello函数打印多次hello并给该函数加备注（具体打印几次依靠传递的参数），然后调用say_hello，同时学会快速查看函数备注，及如何跳转到函数实现快捷操作（与上课一致）
def say_hello(num):
    """
    the function of say hello
    :param num:
    :return:
    """
    for i in range (0,num):
        print('hello')
# 写一个模块（命名不要用中文），模块里写3个打印函数，然后另外一个py文件调用该模块，并调用对应模块的函数，同时用一下下面操作
# if __name__ == '__main__': wd5.print_line()  # 调用函数
def print_a_line():
    print("this is a new line")
def print_a_line2():
    print("this is a new line")
def print_a_line3():
    print("this is a new line")
# 练习列表基本使用，排序，生成式等各种操作（与上课的代码保持一致）
def list_practice():
    # 一维列表
    a = [i for i in range(1,11)]
    print(a)
    # 双循环一维列表
    b = [i*j for j in range(5) for i in range(5)]
    print(b)
    # 二维列表
    c = [[row * col for col in range(5)]for row in range(5)]
    print(c)
    # 二维转一维
    d = [col for row in c for col in row]
    print(d)
    # 只保留单数
    e = [i for i in d if i % 2 == 1]
    print(e)
    # if else
    f = [i if i % 2 == 0 else i**2 for i in d]
    print(f)

# 有8个整数，其中有3个数出现了两次，2个数出现了一次，找出出现了一次的那2个数。
def find_num_twice():
    num_list = [3, 2, 3, 4, 4, 7, 7, 1]
    count_list = [0] * (max(num_list) + 1)
    for num in num_list:
        count_list[num] += 1
    for i in range(0, len(count_list)):
        if count_list[i] == 1:
            print(i, end=' ')
# find_num_once()
# print_num_list()
# say_hello(5)
# list_practice()
# find_num_twice()
new_fun()