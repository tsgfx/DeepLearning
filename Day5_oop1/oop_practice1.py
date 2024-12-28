# 作者: 郭瑞超
# 2024年12月28日18时22分14秒
# grcsxb269@163.com

class Person(object): # 默认继承object父类
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def run(self):
        print(f"{self.name} is running.")
    def eat(self):
        print(f"{self.name} is eating.")

if __name__ == '__main__':
    elephent = Person('elephant', 25, 1.75)
    print(elephent.name, elephent.age, elephent.height)
    tiger = Person('tiger', 18, 1.78)
    tiger.eat()