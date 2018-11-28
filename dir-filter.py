#--------------------------------------------------#
# 程序功能：  过滤重复目录(如果在过滤目录中已经
#             存在，则在处理目录中删除之
# target_dir：要处理的目录
# filter_dir  要过滤的目录
#--------------------------------------------------#
import os
import shutil

target_dir = "headImg-11-去除09月数据"
filter_dir = "headImg-09"

#target_dir = "test"
#filter_dir = "test_filter"

def get_dir_list(path):
    dir_set = set([])
    files = os.listdir(path)
    for file in files:
        dir_path = path + "\\" + file
        if os.path.isdir(dir_path):
            dir_set.add(file)
    return dir_set

if __name__ == "__main__":
    print("处理目录:" + target_dir)
    print("过滤目录:" + filter_dir)
    answer = input("确定要进行目录去重？(yes/no)")
    if answer.lower() != "yes":
        exit()                  
                        
    target_dir_set = get_dir_list(target_dir)
    filter_dir_set = get_dir_list(filter_dir)

    repeat_dir = set([])
    no_repeat_dir = set([])
    for dir in target_dir_set:
        if dir in filter_dir_set:
            repeat_dir.add(dir)
        else:
            no_repeat_dir.add(dir)

    print("处理目录处理前目录数:%d" % len(target_dir_set))
    print("重复目录个数：%d" % len(repeat_dir))
    print("处理后目录数:%d" % len(target_dir_set.difference(filter_dir_set)))
    for dir in repeat_dir:
        path = target_dir + "\\" + dir
        shutil.rmtree(path)

    print("恭喜，目录过滤处理已经完成！")
    os.system("pause")
