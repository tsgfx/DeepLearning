# 作者: 郭瑞超
# 2024年12月26日15时38分24秒
# grcsxb269@163.com
def practice_list():
    """
    列表练习
    :return:
    """
    my_list = ['zhangsan', 'lisi', 'wangwu']
    # 取值
    print(my_list[0])
    # 查找元素
    print(my_list.index('lisi'))
    # 添加
    my_list.append('zhaoliu')
    print(my_list)
    # 插入
    my_list.insert(1, 'xiaoming')
    print(my_list)
    # 删除
    my_list.remove('lisi')
    print(my_list)
    my_list.pop(0)
    print(my_list)
    # 清空
    print(id(my_list))
    my_list.clear()
    print(my_list)
    print(id(my_list))
    # 删除
    print(id(my_list))
    del my_list
    # print(id(my_list) # error


def practice_list_operate():
    my_list = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
    # 长度
    print(len(my_list))
    # 升序
    my_list.sort()
    print(my_list)
    # 降序
    my_list.sort(reverse=True)
    print(my_list)
    # 反转
    my_list.reverse()
    print(my_list)
    # 遍历
    i = 0;
    while i < len(my_list):
        print(my_list[i])
        i += 1


def init_list():
    a = [x for x in range(10)]
    print(a)
    b = [j for i in range(10) for j in range(i)]
    print(b)
    # 二维列表
    c = [[col * row for col in range(5)] for row in range(5)]
    print(c)
    # 二维转一维
    d = [j for x in c for j in x]
    print(d)
    # if
    e = [x for x in range(10) if x % 2 == 0]
    print(e)
    e = [x for x in range(10) if x % 2 != 0]
    print(e)
    # if else
    d = [x if x % 2 == 0 else x ** 2 for x in range(10)]
    print(d)


def simplyfy_list():
    """
    列表的转化
    :return:
    """
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3]
    print(id(a))
    print(a * 2)
    print(a + b)
    print(a)
    print(id(a))  # 不变
    a.extend(b)
    print(a)
    print(id(a))  # 不变
    a += b
    print(a)
    print(id(a))  # 不变,相当于a.extend(b)的重载
    a = a + b
    print(a)
    print(id(a))  # 改变


if __name__ == '__main__':
    pass
# practice_list()
# practice_list_operate()
# init_list()
# simplyfy_list()
