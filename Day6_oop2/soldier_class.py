# 作者: 郭瑞超
# 2024年12月30日10时39分15秒
# grcsxb269@163.com
class Gun:
    def __init__(self, model):
        self.model = model
        self.bullets_count = 0

    def add_bullet(self,count):
        self.bullets_count += count

    def shoot_bullets(self):
        if self.bullets_count <= 0:
            print("No bullets left")
            return

        self.bullets_count -= 1
        print(f"{self.model}发射子弹{self.bullets_count}")

class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print(f"{self.name}没有枪")
            return
        print(f"冲啊{self.name}")
        self.gun.add_bullet(50)
        self.gun.shoot_bullets()

if __name__ == '__main__':
    ak47 = Gun("AK-47")
    xiao_ming = Soldier("xiaoming")
    xiao_ming.gun = ak47
    xiao_ming.fire()
    print(xiao_ming.gun)