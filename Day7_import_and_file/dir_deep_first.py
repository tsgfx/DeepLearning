import os
def scan_dir(file_path,width):
    file_list = os.listdir(file_path)
    for file in file_list:
        print(' ' * width, file)
        new_path = file_path + '/' + file # 拼接路径
        if os.path.isdir(new_path):
            scan_dir(new_path,width+4)

def use_stat(file_path):
    file_info = os.stat(file_path)
    print('size{}, uid{}, mode{:x}, mtime{}'.format(file_info.st_size, file_info.st_uid, file_info.st_mode, file_info.st_mtime))

    from time import strftime
    from time import gmtime
    gmtime = gmtime(file_info.st_mtime)
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime))

if __name__ == '__main__':
    # scan_dir(".", 0)
    use_stat('file1.txt')