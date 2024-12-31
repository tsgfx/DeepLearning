# 作者: 郭瑞超
# 2024年12月30日10时58分00秒
# grcsxb269@163.com
"""
菱形继承
"""
class Parent:
    def __init__(self, height):
        self.height = height
        print("Parent:", end='')
        print(self.height)

class Son1(Parent):
    def __init__(self, age, *args):
        self.age = age
        print("Son1:" ,end='')
        print(self.age)
        super().__init__(*args)

class Son2(Parent):
    def __init__(self, score, *args):
        self.score = score
        print("Son2:" ,end='')
        print(self.score)
        super().__init__(*args)

class Grandson(Son1, Son2):
    def __init__(self, name, *args):
        self.name = name
        print("Grandson:" ,end='')
        print(self.name)
        super().__init__(*args)

if __name__ == '__main__':
    xiao_ming = Grandson('xiao_ming', 18, 98.5, 175)
    print(Grandson.__mro__)