# 作者: 郭瑞超
# 2024年12月26日15时24分26秒
# grcsxb269@163.com
import my_first_module
my_first_module.print_line('-', 50)
# print(my_first_module.a) python中模块的顶层代码在被导入时就会立即运行
print(my_first_module.__name__)