# 作者: 郭瑞超
# 2024年12月28日23时22分13秒
# grcsxb269@163.com
def function(*args):
    for i in args:
        print(i)

def function2(**kwargs):
    print({v:k for k,v in kwargs.items()})

if __name__ == '__main__':
    function(1, 2, 3, [4, 5, 6], (7, 8), {9:10})
    """
    1
    2
    3
    [4, 5, 6]
    (7, 8)
    {9: 10}
    """
    function2(name="Bob", age=18, gender="Male")
    """
    {'Bob': 'name', 18: 'age', 'Male': 'gender'}
    """