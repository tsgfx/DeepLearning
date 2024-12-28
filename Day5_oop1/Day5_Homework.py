# 作者: 郭瑞超
# 2024年12月28日23时03分38秒
# grcsxb269@163.com
def function1(*args, **kwargs):
    print(f"function1:{args}")
    print(f"function2:{kwargs}")

def function2(*args, **kwargs):
    function1(*args, **kwargs)

def function3(age, name = "zhangsan", *args, **kwargs):
    print(f"function3:{age}")
    print(f"function3:{name}")
    print(f"function3:{args}")
    print(f"function3:{kwargs}")

if __name__ == '__main__':
    function2(1, 2, 3, [4, 5, 6], "name", {"name":"zhangsan"}, age = 18, dic = {"position":"manager"})
    """
    function1:(1, 2, 3, [4, 5, 6], 'name', {'name': 'zhangsan'})
    function2:{'age': 18, 'dic': {'position': 'manager'}}
    """
    function3(18)
    """
    function3:18
    function3:zhangsan
    function3:()
    function3:{}
    """