# 作者: 郭瑞超
# 2024年12月31日00时51分22秒
# grcsxb269@163.com
"""
通过try进行异常捕捉，确保输入的内容一定是一个整型数，
然后判断该整型数是否是对称数，12321就是对称数，
123321也是对称数，否则就打印不是，非整型抛异常，不是对称数抛异常
"""

if __name__ == '__main__':
    try:
        num = int(input("请输入一个整型数: "))
    except ValueError:
        print("请输入一个整型数！")
    else:
        # assert str(num) == str(num)[::-1], "不是对称数！"
        if str(num) != str(num)[::-1]:
            raise Exception("不是对称数！")
        else:
            print("是对称数！")