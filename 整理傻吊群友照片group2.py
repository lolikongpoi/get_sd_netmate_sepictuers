import os,shutil
from PIL import Image
from progressbar import *
path=input('请输入文件夹路径(结尾不用加上/)：')+'/'
imagelist = []
f=os.listdir(path)#获得group2下第一层目录列表
prtectlens=100*len(f)
reallens=0
widgets = ['读取进度：',Percentage(),' ',Bar('='),' ',Timer(),' ',ETA()]
pbar = ProgressBar(widgets=widgets, maxval=prtectlens).start()#显示读取进度条
print('大约%d个文件'%(prtectlens))
for f2 in f:
	f3=os.listdir(path+"/"+f2)#获得group2下第二层目录列表
	for f4 in f3:
		f5=os.listdir(path+'/'+f2+'/'+f4)#获得group2下第二层目录下图片列表
		for someimg in f5:
			imagelist.append([path+'/'+f2+'/'+f4+'/'+someimg,someimg])#将[路径,文件名]加入图片列表
			reallens += 1
			pbar.update(reallens)
pbar.finish()
a=0;b=0;c=0;d=0;p1080=0;h=0;k2=0#初始化变量
e=len(imagelist)#获得图片文件数目
print('共发现%d个文件'%(e))
widgets = ['进度：',Percentage(),' ',Bar('='),' ',Timer(),' ',ETA()]
pbar = ProgressBar(widgets=widgets, maxval=e).start()#显示进度条

for i in imagelist:
	if i == 'Thumbs.db':#删除所有的Thumbs.db
		os.unlink(i[0])
		h=h+1
		continue
	try:#筛选1080p和2k（潜在的截图）
		img = Image.open(i[0])
		ws = img.width       #图片的宽
		hs = img.height      #图片的高
		img.close()
		if (ws == 1080 and hs == 1920) or (ws == 1920 and hs == 1080):
			shutil.move(i[0],'D:/qqimage/19201080/'+i[1])
			p1080=p1080+1
			continue
		elif (ws == 1440 and hs == 2160) or (ws == 2160 and hs == 1440):
			shutil.move(i[0],'D:/qqimage/21601440/'+i[1])
			k2=k2+1
			continue
	except :
		pass
	d=d+1
	j=os.path.getsize(i[0])
	if j > 1024*1024:#按照尺寸分类
		shutil.move(i[0],'D:/qqimage/中转站大/'+i[1])
		a=a+1
	if 1024*1024 >= j > 100*1024:
		shutil.move(i[0],'D:/qqimage/中转站中/'+i[1])
		b=b+1
	if 100*1024 >= j > 10*1024:
		shutil.move(i[0],'D:/qqimage/中转站/'+i[1])
		c=c+1
	if 10*1024 >= j:
		os.unlink(i[0])
		h=h+1
	pbar.update(d)
pbar.finish()
for i in f:#删除文件夹
	os.unlink(path+i)
print('已经移动%d个文件至1080p，%d个文件至2k，%d个文件至中转站大，%d个文件至中转站中，%d个文件至中转站。删除文件%d个'%(p1080,k2,a,b,c,h))
