from pyray import *
init_window(800,450,"Hello")
i=0
while not window_should_close():
	strr = "i is %d" %(i)	
	begin_drawing()
	clear_background(WHITE)
	draw_text(strr,190,200,20,VIOLET)
	end_drawing()
	i=i+1
close_window()

