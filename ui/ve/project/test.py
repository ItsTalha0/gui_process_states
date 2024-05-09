#! ../bin/python3
from pyray import *
from time import sleep

mode = int(input("please enter 1 for debug and 2 for run\n"))

f_to_open = "/proc/sample"
if mode==1:
	f_to_open = "sample"


def show_output(file):
	i=0
	win=init_window(1000,800,"Hello")
	x=100
	y=200
	while not window_should_close():
		f = open(file,"r")
		strr = (f.read())
		begin_drawing()
		clear_background(WHITE)
		#draw_rectangle_lines(100,200,50,50,BLACK)#running
		draw_text(strr,10,10,20,BLACK)
		draw_circle_lines(100,200,50,BLACK)
		draw_text("running",70,250,20,BLACK)

		draw_circle_lines(230,200,50,BLACK)#interrpt
		draw_text("interruptible",180,250,20,BLACK)
		
		draw_circle_lines(350,200,50,BLACK)#uniterr
		draw_text("uniterruptible",280,250,20,BLACK)
		
		draw_circle_lines(100,350,50,BLACK)#stoped
		draw_text("stoped",70,300,20,BLACK)

		draw_circle_lines(230,350,50,BLACK)
		draw_text("parked",525,220,20,BLACK)

		draw_circle_lines(350,350,50,BLACK)#interrpt
		draw_text("dead",630,220,20,BLACK)

		draw_circle_lines(100,350,50,BLACK)#uniterr
		draw_text("created",735,220,20,BLACK)

		draw_circle_lines(230,500,50,BLACK)#stoped
		draw_text("rtlock_wait",840,220,20,BLACK)
		#draw_text("freezable",120,220,20,BLACK)
		#draw_text("frozen",120,220,20,BLACK)
		#draw_text("state_max",120,220,20,BLACK)
		end_drawing()
		f.close()
		sleep(0.1)
	close_window()


print(f_to_open)
show_output(f_to_open)
