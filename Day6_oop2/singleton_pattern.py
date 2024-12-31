# 作者: 郭瑞超
# 2024年12月30日23时21分14秒
# grcsxb269@163.com
class MusicPlayer:
    """
    单例模式
    """
    instance = None # 用来保存对象
    def __new__(cls, *args, **kwargs):
        # 创建对象分配空间
        if cls.instance is None:
            cls.instance = super().__new__(cls) #父类的new类似于C的malloc
        return cls.instance
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    player1 = MusicPlayer("music1")
    player2 = MusicPlayer("music2")
    print(id(player1))
    print(id(player2)) # id相同
    print(player1.name)
    print(player2.name) # music2
