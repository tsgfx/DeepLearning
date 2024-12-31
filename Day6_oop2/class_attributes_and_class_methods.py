# 作者: 郭瑞超
# 2024年12月30日23时06分30秒
# grcsxb269@163.com
class CountTool:
    count = 0;  # 类属性, 类似于类的全局变量

    def __init__(self, name):
        self.name = name
        CountTool.count += 1

    def __del__(self):
        CountTool.count -= 1

    @classmethod  # 类方法
    def show_tool_count(cls):
        print(cls.count)

    @staticmethod # 静态方法
    def help():
        """
        不使用对象属性,也不使用类属性
        :return:
        """
        print("不使用对象属性也不使用类属性")


if __name__ == '__main__':
    tool1 = CountTool('John')
    print(CountTool.count)
    too2 = CountTool('John')
    print(CountTool.count)
    del tool1
    print(CountTool.count)
    CountTool.name = "工具类"
    # print(CountTool.name)
    CountTool.show_tool_count()
    CountTool.help()
