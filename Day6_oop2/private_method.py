# 作者: 郭瑞超
# 2024年12月30日10时51分08秒
# grcsxb269@163.com
class Women:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __seceret(self):
        """
        私有方法, 不能被外部调用
        :return:
        """
        print(f"年龄: {self.age}")

if __name__ == '__main__':
    xiaohong = Women('xiaohong', 18)
    # xiaohong.__seceret()