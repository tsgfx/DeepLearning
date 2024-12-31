# 作者: 郭瑞超
# 2024年12月30日09时24分18秒
# grcsxb269@163.com
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'姓名：{self.name} 年龄：{self.age}'

    def __del__(self):
        print(f"{self.name}已删除")


class HouseItem:
    def __init__(self, name, area):
        """
        初始化方法
        :param name:
        :param area:
        """
        self.name = name
        self.area = area

    def __str__(self):
        return f"家具名：{self.name}， 家具位置：{self.area}"


class House:
    def __init__(self, house_type, area):
        """
        房子初始化方法
        :param house_type:
        :param area:
        """
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return f"房子类型：{self.house_type}， 房子位置：{self.area}， 空闲面积：{self.free_area}, 家具列表：{self.item_list}"

    def add_item(self, item: HouseItem):  # 通过:加对象类型，加注解
        """
        添加家具方法
        :param item:
        :return:
        """
        if (item.area > self.free_area):
            print("空间不足")
            return
        self.free_area -= item.area
        self.item_list.append(item.name)


if __name__ == '__main__':
    # xiaoming = Person('xiaoming', 18)
    # print(xiaoming)
    bed = HouseItem("bed", 50)
    my_house = House("big_house", 100)
    my_house.add_item(bed)
    print(my_house.item_list)
