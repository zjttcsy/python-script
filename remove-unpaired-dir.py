#--------------------------------------------------#
# 程序功能：  去除target_dir子目录中单个目录下文件数
#             目小于2张的目录(人脸数据不成对)
# target_dir：要处理的目标目录
#--------------------------------------------------#
import os
import shutil

target_dir = "test"
#target_dir = "test"

def get_dir_list(path):
    dir_set = set([])
    files = os.listdir(path)
    for file in files:
        dir_path = path + "\\" + file
        if os.path.isdir(dir_path):
            dir_set.add(file)
    return dir_set

def get_dir_file_count(path):
    file_count = 0
    files = os.listdir(path)
    for file in files:
        file_path = path + "\\" + file
        if os.path.isfile(file_path):
            file_count = file_count + 1
    return file_count

if __name__ == "__main__":
    print("程序功能:去除target_dir子目录中单个目录下文件数目小于2张的目录(人脸数据不成对)")
    print("目标目录:" + target_dir)
    answer = input("确定要移除无效目录？(yes/no)")
    if answer.lower() != "yes":
        exit()                  
                        
    target_dir_set = get_dir_list(target_dir)

    remove_dir = set([])
    dir_counter = 1
    for dir in target_dir_set:
        path = target_dir + "\\" + dir
        file_count = get_dir_file_count(path)
        if file_count < 2:
            remove_dir.add(dir)
        dir_counter = dir_counter + 1
        if dir_counter % 100 == 0:
            print(".", end='')

    print("\n目标目录处理前目录数:%d" % len(target_dir_set))
    print("待删除目录个数：%d" % len(remove_dir))
    answer = input("请再次确认是否要移除无效目录？(yes/no)")
    if answer.lower() != "yes":
        exit()

    for dir in remove_dir:
        path = target_dir + "\\" + dir
        shutil.rmtree(path)

    print("恭喜，去除未成对目录处理已经完成！")
    os.system("pause")
