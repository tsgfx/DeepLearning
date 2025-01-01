import os
def read_config():
    file=open('user_info.txt', 'r+', encoding='utf-8')
    text_info = file.read()
    print(eval(text_info)) #eval()函数将字符串当成python表达式来执行
    file.close()

if __name__ == '__main__':
    read_config()
    os.system('ls')