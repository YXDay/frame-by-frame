# coding:utf-8
# 用于生成给yolo的图片路径文件
import os

# 递归删除.DS_Store
def walk(path):
	for item in os.listdir(path):
		try:
			if(item == ".DS_Store"):
				os.remove(path+"/"+item)
			else:
				if(os.path.isdir(path+"/"+item)):
					walk(path+"/"+item)
		except OSError,e:
			print e

walk(VIDEO_PATH) #递归删除.DS_Store

roots = []#所有文件夹名
dirs = []#视频文件
files = []#视频文件地址

# 遍历
for root, dir_, file in os.walk(VIDEO_PATH):
	roots.append(root)
	dirs.append(dir_)
	files.append(file)

# 写入
for i in range(6):
	for index, file in enumerate(files[i+1]):
		print index
		frameByFrame(roots[i+1] + '/' + file, dirs[0][i], index)
