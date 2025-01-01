import sys
# print(type(sys.argv))
# print(sys.argv)
"""
(practice_enviroment) (base) root@Ubuntu20:~/DeepLearning/Day7_import_and_file# python send_perameter.py 123, abc
<class 'list'>
['send_perameter.py', '123,', 'abc']
"""

def write_hello(file_path):
    file = open(file_path, 'w+', encoding='utf-8')
    file.write('hello\\n')
    file.close()

if __name__ == '__main__':
    write_hello(sys.argv[1]) # sys.argv[0] = 'send_perameter.py'