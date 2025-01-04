# 作者: 郭瑞超
# 2025年01月03日10时56分53秒
# grcsxb269@163.com
import re

def use_match():
    # . 匹配任意单个字符
    res = re.match("wangdao", "wangdao.cn") # 匹配字符串开头
    print(res)
    print(res.group()) # 输出匹配到的字符串
    res = re.match(".", "w") # 匹配任意单个字符
    print(res)
    # [] 匹配字符集
    res = re.match("[aA]", "asdadsa") # 匹配a或A
    print(res)
    res = re.match("[aA]", "Asdadsa") # 匹配a或A，不区分大小写
    print(res)
    res = re.match("[1-9]", "1sdadsa") # 匹配1-9的数字
    print(res)
    res = re.match(r"[1-35-9]", "4fd") # 匹配1-3或5-9的数字
    print(res)
    res = re.match(r"[1-35-9]", "3fd")  # 匹配1-3或5-9的数字
    print(res)
    # \d 匹配数字
    res = re.match(r"a\db", "a7b")  # 匹配a后面跟着b
    print(res)

    print('-'*50)

    # * 匹配0个或多个字符
    res = re.match("[A-Z][a-z]*","AbcDef") # 匹配大写字母开头，小写字母0个或多个
    print(res.group())
    # + 匹配1个或多个字符
    # \w 匹配字母、数字、下划线
    # r 原始字符串
    names = ["name1", "_name", "1name", "__name__"]
    for name in names:
        res = re.match(r"[a-zA-Z_]+[\w]*", name) # 匹配字母、数字、下划线，至少1个字符
        if res:
            print("变量名 %s 符合要求" % res.group())
        else:
            print("变量名 %s 非法" % name)

    print('-' * 50)

    # ？ 匹配0-99之间的数字
    res = re.match("[1-9]?[0-9]", "0")
    print(res.group())
    res = re.match(r"[1-9]?\d", "33")
    print(res.group())
    res = re.match(r"[1-9]?\d", "3")
    print(res.group())

    print('-' * 50)

    # {m} 匹配m个字符
    res = re.match("[a-zA-Z0-9_]{6}", "12a3g4567") # 匹配6个字符的字符串
    print(res.group())
    res = re.match(r"[a-zA-Z0-9_]{8,20}", "12a3g456723434343423")
    print(res.group())

def email_match():
    """
    邮箱匹配
    ^ 匹配字符串开头
    $ 匹配字符串结尾
    :return:
    """
    email_list = ["grcsxb269@163.com", "1715207009@163.comqq", "674672hdy@163acom"]
    for email in email_list:
        res = re.match(r"\w{4,20}@163\.com$", email) # 出现正则符号要转义
        if res:
            print("邮箱 %s 符合要求" % email)
        else:
            print("邮箱 %s 非法" % email)

def split_group_match():
    """
    分组匹配
    :return:
    """
    # 匹配1-100
    # 写到前面的会先匹配
    res = re.match(r"[1-9][0-9]|[1-9]|100", "11")
    print(res.group())
    email_list = ["grcsxb269@163.com", "1715207009@126.com", "674672hdy@qq.com"]
    for email in email_list:
        res = re.match(r"\w{4,20}@(163|126|qq)\.com$", email)
        if res:
            print("邮箱 %s 符合要求" % email)
        else:
            print("邮箱 %s 非法" % email)
    print('-' * 50)
    res = re.match(r"([^-]+)-(\d+)","010-123456") #^-表示没有遇到-就一直匹配下去
    print(res.group())
    print(res.group(1))
    print(res.group(2))
    print('-' * 50)
    # 引用分组
    res = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<div>hello</div>")
    print(res.group())
    res = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<div><span>hello</span></div>")
    print(res.group())

if __name__ == '__main__':
    # use_match()
    # email_match()
    split_group_match()