#coding:utf-8
import cv2
import os

VIDEO_PATH = '/Users/daiyanxu/Desktop/project/GraduationDesign/imageweuse'

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

def frameByFrame(path, folder, index):
	print path
	print folder
	vc = cv2.VideoCapture(path) #读入视频文件
	c=1
	if vc.isOpened(): #判断是否正常打开
	    rval , frame = vc.read()
	else:
	    rval = False
	timeF = 1  #视频帧计数间隔频率
	while rval:   #循环读取视频帧
	    rval, frame = vc.read()
	    if(c%timeF == 0): #每隔timeF帧进行存储操作
	        cv2.imwrite('./image/' + folder + '/' + str(index) + '&' +str(c) + '.jpg',frame) #存储为图像
	    c = c + 1
	vc.release()

walk(VIDEO_PATH) #递归删除.DS_Store

roots = []#所有文件夹名
dirs = []#视频文件
files = []#视频文件地址
for root, dir_, file in os.walk(VIDEO_PATH):
	roots.append(root)
	dirs.append(dir_)
	files.append(file)

for i in range(6):
	for index, file in enumerate(files[i+1]):
		print index
		frameByFrame(roots[i+1] + '/' + file, dirs[0][i], index)
