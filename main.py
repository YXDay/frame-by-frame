#coding:utf-8
import cv2
import os

VIDEO_PATH = '/Users/daiyanxu/Desktop/project/GraduationDesign/imageweuse'

# �ݹ�ɾ��.DS_Store
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
	vc = cv2.VideoCapture(path) #������Ƶ�ļ�
	c=1
	if vc.isOpened(): #�ж��Ƿ�������
	    rval , frame = vc.read()
	else:
	    rval = False
	timeF = 1  #��Ƶ֡�������Ƶ��
	while rval:   #ѭ����ȡ��Ƶ֡
	    rval, frame = vc.read()
	    if(c%timeF == 0): #ÿ��timeF֡���д洢����
	        cv2.imwrite('./image/' + folder + '/' + str(index) + 'a' +str(c) + '.jpg',frame) #�洢Ϊͼ��
	    c = c + 1
	vc.release()

walk(VIDEO_PATH) #�ݹ�ɾ��.DS_Store

roots = []#�����ļ�����
dirs = []#��Ƶ�ļ�
files = []#��Ƶ�ļ���ַ
for root, dir_, file in os.walk(VIDEO_PATH):
	roots.append(root)
	dirs.append(dir_)
	files.append(file)

for i in range(6):
	for index, file in enumerate(files[i+1]):
		print index
		frameByFrame(roots[i+1] + '/' + file, dirs[0][i], index)
