# 作者: 郭瑞超
# 2024年12月30日22时57分01秒
# grcsxb269@163.com
# 多态：同一条指令，不同对象，产生的行为是不同的
class Dog:
    def __init__(self, name):
        self.name = name
    def game(self):
        print('Dog game')

class XiaoTianDog(Dog):
    def game(self):
        print('XiaoTian game')

class Person:
    def __init__(self, name):
        self.name = name
    def game_with_dog(self, dog:Dog):
        print(f"{self.name} play with {dog.name}")
        dog.game()

if __name__ == '__main__':
    zhang_san =Person('zhangsan')
    wang_cai = Dog('wang_cai')
    zhang_san.game_with_dog(wang_cai)
    xiao_tian_quan = XiaoTianDog('xiao_tian_quan')
    zhang_san.game_with_dog(xiao_tian_quan)