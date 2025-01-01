# 作者: 郭瑞超
# 2024年12月31日10时40分58秒
# grcsxb269@163.com
import os 


def read_file(file_path):
    """
    读取文件
    :param file_path:
    :return:
    """
    file = open(file_path, mode='r', encoding='utf-8')
    text = file.read()
    print(text)
    file.close()

def read_and_write_file(file_path):
    """
    读写文件
    :param file_path:
    :return:
    """
    file = open(file_path, mode='a', encoding='utf-8')
    file.write("Hello Pycharm")
    read_file(file_path)
    file.close()

def use_readline(file_path):
    file = open(file_path, mode='r', encoding='utf-8')
    while True:
        line = file.readline()
        if not line:
            break
        print(line, end="")
    file.close()

def use_seek(file_path):
    file = open(file_path, mode='r+', encoding='utf-8')
    file.seek(6, os.SEEK_SET) # 全局常量,汉字的偏移是3的整数倍
    text = file.read(5)
    print(text)
    file.close()

def use_binary_seek(file_path):
    file = open(file_path, mode='rb+')
    b = file.read()
    print(b)
    file.close()

def copy_file(file_path1, file_path2):
    file1 = open(file_path1, mode='rb+')
    file2 = open(file_path2, mode='wb')
    b = file1.read()
    file2.write(b)
    file1.close()
    file2.close()

if __name__ == '__main__':
    # read_file("./file1.txt")
    # read_and_write_file("./file1.txt")
    # use_readline("./file1.txt")
    # use_seek("./file1.txt")
    copy_file("./file1.txt","file2.txt")