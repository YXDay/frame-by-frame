# Delete everything reachable from the directory named in 'top',
# assuming there are no symbolic links.
# CAUTION:  This is dangerous!  For example, if top == '/', it
# could delete all your disk files.
import os
flag = 0
for root, dirs, files in os.walk('/Users/daiyanxu/Desktop/project/me/HumanActionRecognition/classification_core/static/images/train/sit', topdown=False):
    for name in files:
		if flag%2 == 1:
			os.remove(os.path.join(root, name))
		flag += 1