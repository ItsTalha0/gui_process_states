#! ../bin/python3
from pyray import *
from time import sleep
import cord
import os

coord = dict(
	running = ((280,340),(250,330)),
	dead 	= ((120,250),(100,240)),
	parked	= ((300,150),(270,140)),
	uniter	= ((430,200),(400,190)),
	stoped	= ((120,400),(90,390)),
	sleep	= ((460,410),(430,400)),
	frozen	= ((290,550),(270,540)),
	zombie	= ((120,560),(100,550)),
	err		= ((60,60),(40,50))
	)

state_map = {
	0x00000001 : "sleep",
	0x00000000 : "running",
	0x00000002 : "uniter",
	0x00000004 : "stoped",
	0x00000080 : "dead",
	0x00000040 : "parked",
	0x00008000 : "frozen",
	0x00000020 : "zombie"
	}
#path=os.environ["path"]
mode = int(input("please enter 1 for debug and 2 for run\n"))

f_to_open = "/proc/sample"
if mode==1:
	f_to_open = "sample"

def show_output(file):
	i=0
	win=init_window(cord.window_aspect[0],cord.window_aspect[1],"Hello")
	x=100
	y=200
	while not window_should_close():	
		f = open(file,"r")
		strr = (f.read())
		str1 = strr
		str2 = ""
		for thing in str1:
			if thing not in "0123456789":
				break
			else:
				str2 = str2+thing
		strr = str2
		if strr != '':
			state = int(strr)
		else:
			state = -1		
		begin_drawing()
		clear_background(WHITE)
		#draw_rectangle_lines(100,200,50,50,BLACK)#running
		draw_text(strr,10,10,20,BLACK)
		#for running
		draw_line(coord["running"][0][0],coord["running"][0][1],coord["dead"][0][0],coord["dead"][0][1],BLACK)
		draw_line(coord["running"][0][0],coord["running"][0][1],coord["sleep"][0][0],coord["sleep"][0][1],BLACK)
		draw_line(coord["running"][0][0],coord["running"][0][1],coord["stoped"][0][0],coord["stoped"][0][1],BLACK)
		draw_line(coord["running"][0][0],coord["running"][0][1],coord["zombie"][0][0],coord["zombie"][0][1],BLACK)
		draw_line(coord["running"][0][0],coord["running"][0][1],coord["uniter"][0][0],coord["uniter"][0][1],BLACK)
		draw_line(coord["running"][0][0],coord["running"][0][1],coord["parked"][0][0],coord["parked"][0][1],BLACK)
		draw_line(coord["running"][0][0],coord["running"][0][1],coord["frozen"][0][0],coord["frozen"][0][1],BLACK)
		
		draw_line(coord["dead"][0][0],coord["dead"][0][1],coord["sleep"][0][0],coord["sleep"][0][1],BLACK)
		

		for i in cord.state_map:
			draw_circle(cord.coord[cord.state_map[i]][0][0],cord.coord[cord.state_map[i]][0][1],50,WHITE)
		if state != -1:
			if state != 0:
				for i in cord.state_map:
					if (i & state) == i and i!=0:
						draw_circle(cord.coord[cord.state_map[i]][0][0],cord.coord[cord.state_map[i]][0][1],50,PINK)
			else:
				draw_circle(cord.coord["running"][0][0],cord.coord["running"][0][1],50,PINK)
		else:
			draw_circle(cord.coord["err"][0][0],cord.coord["err"][0][1],50,PINK)
		for i in cord.coord:
			draw_circle_lines(cord.coord[i][0][0],cord.coord[i][0][1],50,BLACK)
			draw_text(i,cord.coord[i][1][0],cord.coord[i][1][1],20,BLACK)

		'''
		draw_circle_lines(280,340,50,BLACK)
		draw_text("running",250,330,20,BLACK)
		#from running to dead
		#for dead
		draw_circle_lines(120,250,50,BLACK)#interrpt
		draw_text("dead",100,240,20,BLACK)
		draw_circle_lines(300,150,50,BLACK)#interrpt
		draw_text("parked",270,140,20,BLACK)
		draw_circle_lines(430,200,50,BLACK)#uniterr
		draw_text("uniter",400,190,20,BLACK)
		draw_circle_lines(120,400,50,BLACK)#stoped
		draw_text("stoped",90,390,20,BLACK)
		draw_circle_lines(450,430,50,BLACK)
		draw_text("interp",420,420,20,BLACK)
		draw_circle_lines(290,550,50,BLACK)#uniterr
		draw_text("something",270,540,20,BLACK)
		draw_circle_lines(120,560,50,BLACK)
		draw_text("zombie",100,550,20,BLACK)
		#draw_circle_lines(230,500,50,BLACK)#stoped
		#draw_text("rtlock_wait",840,220,20,BLACK)
		#draw_text("freezable",120,220,20,BLACK)
		#draw_text("frozen",120,220,20,BLACK)
		#draw_text("state_max",120,220,20,BLACK)
		'''
		end_drawing()
		f.close()
		sleep(0.1)
	close_window()


print(f_to_open)
show_output(f_to_open)
