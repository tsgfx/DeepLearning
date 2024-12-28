# 作者: 郭瑞超
# 2024年12月28日15时20分25秒
# grcsxb269@163.com
def muti_return():
    return 10, 20, 30

def use_mutireturn():
    res = muti_return()
    print(res)
    res1, res2, res3 = muti_return()
    print(res1, res2, res3)

def muti_perameter(name, num = 1):
    print(name, num)

if __name__ == '__main__':
    muti_perameter("zhang", 10)