# 作者: 郭瑞超
# 2025年01月05日02时40分38秒
# grcsxb269@163.com
import re
def use_greedy():
    s = "This is a number 234-235-22-423"
    r = re.match(r".+(\d+-\d+-\d+-\d+)", s)  # use greedy match
    print(r.group(1))

    s = "This is a number 234-235-22-423"
    r = re.match(r".+?(\d+-\d+-\d+-\d+)", s)  # use ungreedy match
    print(r.group(1))

def use_r():
    mm = "c:\\a\\b\\c"
    print(mm)
    print(re.match(r"c:\\", mm).group()) # match c:\

def use_option():
    print(re.match(r"\w*", "abc爱",flags=re.A).group()) #re.A 不让\w匹配汉字
    print(re.match(r"a*", "Abc爱",flags=re.I).group()) #re.I 忽略大小写
    print(re.match(r".*", "ab\ncde",flags=re.S).group()) #re.S 让.匹配换行符


if __name__ == '__main__':
    use_greedy()
    use_r()
    use_option()

