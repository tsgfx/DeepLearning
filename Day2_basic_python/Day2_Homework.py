# 作者: 郭瑞超
# 2024年12月25日17时26分24秒
# grcsxb269@163.com
# 自己定义变量赋值不同的数据类型并打印，并使用type
def print_data_type():
    a = 100
    b = 5.12
    c = True
    str = "Hello World"
    ch = 'A'
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(str))
    print(type(ch))


# 能够将整型转为不同进制，进行输出（与上课一致）
def decimal_conversion():
    a = 200
    print(bin(a))  # 0b11001000 二进制
    print(oct(a))  # 0o310 八进制
    print(hex(a))  # 0xc8 十六进制


# 实现从1到100之间的奇数求和
def sum_odd_num():
    sum = 0
    for i in range(1, 101):
        if i % 2 != 0: sum += i
    print(sum)


# 打印九九乘法表（直接百度乘法表图像，与其一致即可）
def chengfabiao():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("%d * %d = %d" % (i, j, i * j), end="\t")
        print()


# 统计一个整数对应的二进制数的1的个数。输入一个整数（可正可负，负数就按64位去遍历即可）， 输出该整数的二进制包含1的个数（使用位运算）
def count_num_of_one():
    num = int(input("请输入一个整数："))
    if (num < 0): num = (1 << 64) + num
    count = 0
    while num != 0:
        if (num & 1 == 1): count += 1
        num = num >> 1
    print(count)
# print_data_type()
# decimal_conversion()
# sum_odd_num
# chengfabiao()
# count_num_of_one()
