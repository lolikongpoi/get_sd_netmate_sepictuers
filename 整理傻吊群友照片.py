import os,shutil
path=input('请输入文件路径(结尾不用加上/)：')+'/'
f=os.listdir(path)
a=0;b=0;c=0;d=0;h=0
e=len(f)
print('共发现%d个文件'%(e))
for i in f:
	j=os.path.getsize(path+i)
	d=d+1
	if j > 1024*1024:
		shutil.move(path+i,'T:/中转站大/'+i)
		a=a+1
	if 1024*1024 >= j > 100*1024:
		shutil.move(path+i,'T:/中转站中/'+i)
		b=b+1
	if 100*1024 >= j > 10*1024:
		shutil.move(path+i,'T:/中转站/'+i)
		c=c+1
	if 10*1024 >= j:
		os.unlink(path+i)
		h=h+1
	if d==e:
		print('已完成100%')
	elif d==(e*9//10):
		print('已完成90%')
	elif d==(e*8//10):
		print('已完成80%')
	elif d==(e*7//10):
		print('已完成70%')
	elif d==(e*6//10):
		print('已完成60%')
	elif d==(e*5//10):
		print('已完成50%')
	elif d==(e*4//10):
		print('已完成40%')
	elif d==(e*3//10):
		print('已完成30%')
	elif d==(e*2//10):
		print('已完成20%')
	elif d==(e//10):
		print('已完成10%')
	elif d==1:
		print('已完成0%')
print('已经移动%d个文件至中转站大，%d个文件至中转站中，%d个文件至中转站。删除文件%d个'%(a,b,c,h))