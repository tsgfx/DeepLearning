# 作者: 郭瑞超
# 2024年12月31日10时40分58秒
# grcsxb269@163.com
import os 
def use__rename():
    os.rename('file3.txt', 'file4.txt')

def use_dir():
    dir_list = os.listdir('.') # '.'是当前目录
    print(dir_list)
    # os.mkdir('test')
    # os.mkdir('test2')
    # os.rmdir('test') # 删除空目录
    print(os.getcwd()) # 获取当前工作目录
    os.chdir('..') # 切换到上一级目录
    print(os.getcwd())

if __name__ == '__main__':
    # use__rename()
    use_dir()