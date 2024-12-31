# 作者: 郭瑞超
# 2024年12月31日00时00分53秒
# grcsxb269@163.com
import error_file
def use_exception1():
    while True:
        try:
            num = int(input("请输入一个整数"))
            print(num)
            break
        except:
            print("必须输入整型数字")
def use_exception2():
    try:
        num = int(input("请输入一个整数"))
        res = 8 // num
        print(res)
    except ValueError:
        print("必须输入整型数字")
        return
    # except ZeroDivisionError:
        # print("除0错误")
    except Exception as e:
        print(e)
    else:
        print("正常执行")
    finally:
        print("执行完成，但是不保证正确") # 不受return影响

def use_exception3():
    """
    捕获异常发生的文件
    :return:
    """
    try:
        error_file.test()
    except Exception as e:
        print(e)
        print("捕获到异常", e.__traceback__.tb_frame.f_code.co_filename)
        print("捕获到异常", e.__traceback__.tb_lineno)
def use_exception4():
    """
    异常的传递
    :return:
    """
    def demo1():
        return int(input("请输入一个整数"))
    def demo2():
        num2 = demo1()
        print("I am demo2")
        return num2

    try:
        print(demo2())
    except Exception as e:
        print(e)

def use_exception5():
    """
    自定义异常
    :return:
    """
    pwd = input("请输入密码：")
    if len(pwd) >= 8:
        return pwd
    print("主动抛出异常")
    raise Exception("密码长度必须大于等于8")

def use_exception6():
    """
    断言异常
    :return:
    """
    try:
        assert 1 == 2, "程序发生了xxx错误" #可以不用写判断条件，直接抛出异常
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # use_exception1()
    # use_exception2()
    # use_exception3()
    # use_exception4()
    try:
        use_exception5()
    except Exception as e:
        print(e)
    # while True:
        # pass