# 作者: 郭瑞超
# 2024年12月28日16时59分56秒
# grcsxb269@163.com
def print_info(name, title="", gender=True):
    print("Name:", name)
    print("Title:", title)
    print("Gender:", gender)

def demo2(*args, **kwargs):
    print(args)
    print(kwargs)

def demo(num, *args, **kwargs): # *args-位置参数 *kwargs-keyword参数
    print(num)
    print(args)
    print(kwargs)
    demo2(*args, **kwargs)

if __name__ == '__main__':
    # print_info("zhangsan")
    # print_info("lisi", gender=False)
    # print_info("wangu", "teacher")
    demo(101, 2, 3, 4, 5, name = 'xiaoming', age = 20, mylist = [1, 2, 3, 4])

