# coding:utf-8
# 遍历特定文件夹,通过shell调用yolo<真*魔改版>保存man♂image

import os
import time

IMAGE_PATH = '/Users/daiyanxu/Desktop/project/GraduationDesign/frame-by-frame/image'

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

walk(IMAGE_PATH) #递归删除.DS_Store

roots = []#所有文件夹名
dirs = []#视频文件
files = []#视频文件地址

# 遍历
for root, dir_, file in os.walk(IMAGE_PATH):
	roots.append(root)
	dirs.append(dir_)
	files.append(file)


# 写入
for index, file in enumerate(files[6]):
	order = '../../darknet/darknet detect ../../darknet/cfg/yolo.cfg ../../darknet/yolo.weights ' + roots[6] + '/' + file
	os.system(order)
	time.sleep(0.1)

os.system('say mission complete')
