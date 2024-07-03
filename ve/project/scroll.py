
#! ../bin/python3
import cord
import os
from pyray import *
arr = [1,3,1,5,6,7]

pid=input()

f = "start"

file = open(f,"r")
start= file.readlines()
a=[]
for i in start:
	a.append(int(i,16))	

a=[x-a[0] for x in a]
a_sum = sum(a)
#a = [ (x/a_sum)*1000 for x in a]
a2=[]
for i in range(0,len(a)-1):
	a2.append(a[i+1]-a[i])

#a2 = [ (x/a_sum)*1000 for x in a2]
a2 = [ int(x/1024) if x/1024 < 1000 else 1000  for x in a2]

a3 = [ x if x < 1000 else 1000 for x in a2]
print(a2)

def show_output(arr):	
	win=init_window(800,1000,"hello")
	x1=0
	y1=0
	while not window_should_close():
		begin_drawing()
		clear_background(WHITE)
		a=get_key_pressed()
		strr=str(a)
		x=400
		y=500
		if is_key_down(265):
			x1=x1-2
		if is_key_down(264):
			x1=x1+2
		draw_text("hello",y,x,20,BLACK)
		flg=1
		
		for i in arr:
				
			if flg==0:
				draw_rectangle(y,(x+i*100)+x1,100,100+i*100,PINK)
				flg=1
			else:
				draw_rectangle(y,(x+i*100)+x1,100,100+i*100,BLACK)
				flg=0
			x=x+i*10

		#sleep(1)


		end_drawing()

show_output(a3)


