# 作者: 郭瑞超
# 2024年12月25日14时11分50秒
# grcsxb269@163.com
def All_variables_are_Pointers():
    a = 1
    b = 1
    print(id(a))
    print(id(b))
    a = 2
    print(id(a))


def complex_num():
    c = complex(1, 2)
    print("c is %d+%dj" % (c.real, c.imag))


def float_num():
    b = -5
    print(b)
    c = 1.2345678912345678912345  # 1.234567891234568 精度丢失
    print(c)


def Decimal_conversion():
    a = 200
    print(bin(a))  # 0b11001000 二进制
    print(oct(a))  # 0o310 八进制
    print(hex(a))  # 0xc8 十六进制


def Input_Standart_Cin():
    a = input('请输入内容:')
    print(a)
    print(type(a))
    # 大写转小写
    print(chr(ord(a) + 32))


def change_type():
    a = input('请输入内容:')
    print(type(a))


def format_output():
    score = 98.2
    print('名字是%s,成绩是%.2f,年龄是%03d' % ('小明', score, 19))


def use_sum():
    """
    学习算数运算符
    :return:
    """
    a = 5 / 2
    print(a)  # 2.5
    a = 5 // 2
    print(a)  # 2
    a = 0.99 * 365
    print(a)
    a = 0.99 ** 365
    print(a)


def use_logic():
    """
    使用逻辑运算符
    :return:
    """
    print(3 and 5)  # 都为真则返回后一个
    print(0 or 5)
    3 and print('Hello')  # 短路运算 输出Hello


0 and print('Hello')  # 短路运算 不输出 可以不写if实现判断

# All_variables_are_Pointers()
# complex_num()
# float_num()
# Decimal_conversion()
# Input_Standart_Cin()
# change_type()
# format_output()
# use_sum()
# use_logic()
