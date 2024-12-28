# 作者: 郭瑞超
# 2024年12月29日00时20分02秒
# grcsxb269@163.com
class Animal:
    def __init__(self, type, color, name):
        self.type = type
        self.color = color
        self.name = name

    def bark(self):
        print("汪汪汪")

    def wag_tail(self):
        print("摇尾巴")

if __name__ == '__main__':
    dog = Animal('Dog', 'yello', 'da_huang')
    print(dog.type)
    print(dog.color)
    print(dog.name)
    dog.bark()
    dog.wag_tail()