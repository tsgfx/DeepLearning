# 作者: 郭瑞超
# 2025年01月05日00时44分31秒
# grcsxb269@163.com
import re


def advance_regular_expression():
    # search()方法用于查找字符串的第一次出现的位置，如果没有找到匹配的字符串，则返回None。
    res = re.search(r"\d+", "点击次数为9999")
    print(res.group())

def find_second_match(pattern, text):
    maches = re.finditer(pattern, text)
    try:
        next(maches) # 跳过第一个匹配
        next(maches) # 跳过第二个匹配
        # next(maches) # 跳过第三个匹配
        second_match = next(maches) # 获取第三个匹配
        return second_match.group()
    except StopIteration:
        return None

def find_all_matches():
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
    print(ret)

def number_generator(start=0):
    while start < 10:
        yield start # 程序在这里暂停，start值被return回来
        start += 1
    return

def use_number_generator():
    gen = number_generator()
    print(type(gen))  # <class 'generator'>
    print(next(gen))  # 0
    print(next(gen))  # 1
    for i in gen: # for循环会自动调用next()方法
        print(i)

def add(x):
    result = x.group()
    return str(int(result) + 1)
def use_sub():
    res = re.sub(r"\d+", '998', "python = 997") # 将所有数字替换为998
    print(res)
    res = re.sub(r"\d+", lambda m: str(int(m.group()) + 1), "python = 997") # 将所有数字加1
    print(res)
    res = re.sub(r"\d+", add, "python = 997") # 将所有数字加1
    print(res)
    text = "apple apple apple apple"
    pattern = r"apple"
    replacement = "orange"
    new_text = re.sub(pattern, replacement, text, count=2)
    print(new_text)

def use_findall():
    s = 'hello world, now is 2020/7/20 18:48, 现在是 2020 年 7 月 20 日 18 时 48 分。'
    ret_s = re.sub(r'年|月', r'/', s)
    ret_s = re.sub(r'日', r' ', ret_s)
    ret_s = re.sub(r'时|分', r':', ret_s)
    print(ret_s)

    pattern1 = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    ret = pattern1.findall(ret_s)
    print(ret)

    pattern2 = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    res = pattern2.search(ret_s)
    print(res.group())

    long_text = """' " ' " """
    print(long_text)

if __name__ == '__main__':
    # advance_regular_expression()
    # text = "abc123def456ghi789"
    # pattern = r"\d+"
    # second_match = find_second_match(pattern, text)
    # print(second_match)
    # find_all_matches()
    # use_number_generator()
    # vuse_sub()
    use_findall()
