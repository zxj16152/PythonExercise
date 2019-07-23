import os
filelist=[]
def getAllFiles(path):
    for file in os.listdir(path):  # 遍历当前目录下所有文件
        filePath = os.path.join(path, file)  # 生成当前目录下文件的绝对路径
        if os.path.isfile(filePath):  # 如果这个路径是文件而不是文件夹则找到一个文件
            if filePath.endswith("txt"):
               print(filePath)
               filelist.append(filePath)
        else:   # 如果这个路径是文件夹，则递归调用此函数
            getAllFiles(filePath)
    return sorted(filelist)

def readFiles(files):
    "注释是这样的"
    path="/Users/zhouxinjian/vedio/01.Elasticsearch顶尖高手系列课程/01_快速入门篇/知识点.txt"
    disFile = open(path, "ab")
    for file in files:
        readlines = open(file, "rb").readlines()
        disFile.writelines(readlines)


all_files = getAllFiles("/Users/zhouxinjian/vedio/01.Elasticsearch顶尖高手系列课程/01_快速入门篇")
all_files.remove("/Users/zhouxinjian/vedio/01.Elasticsearch顶尖高手系列课程/01_快速入门篇/知识点.txt")
readFiles(all_files)

