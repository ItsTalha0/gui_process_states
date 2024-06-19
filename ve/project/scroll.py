
#! ../bin/python3
import cord
import os

arr = [1,3,1,5,6,7]

pid=input()

f = "start"
f1 = "end"

file1 = open(f,"r")
file2 = open(f1,"r")
start= file1.readlines()
end = file2.readlines()

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
		for i in :
				
			if flg==0:
				draw_rectangle(y,(i*10)+x1,100,100,PINK)
				flg=1
			else:
				draw_rectangle(y,(i*10)+x1,100,100,BLACK)
				flg=0
			x=x+100

		#sleep(1)


		end_drawing()

show_output(arr)


