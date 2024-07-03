#! ../bin/python3
import os
from pyray import *
import psutil
import sys

print(len(sys.argv))
pid_list=[ psutil.Process(int(x)) for x in  sys.argv[1:]]
print([ (x.status(),x.name()) for x in pid_list])

state_map = {
		"running" : 0,
		"dead"	: 1,
		"disk-sleep" : 2,
		"idle" 	: 3,
		"locked"  : 4,
		"parked"  : 5,
		"sleeping": 6,
		"stopped" : 7,
		"tracing-stop": 8,
		"waitin" : 9,
		"waking" : 10,
		"zombie" : 11
	}

def show_output():	
	win=init_window(1200,800,"hello")
	while not window_should_close():
		begin_drawing()
		i=0
		draw_text("pid",10,30,20,BLACK)
		draw_line(80,10,80,100+40*len(pid_list),BLACK)
		for x in state_map:
			draw_text(x[:4],100	+i,30,20,BLACK)
			draw_line(160+i,10,160+i,100+40*len(pid_list),BLUE)
			i=i+70
		ladder = 0
		for pr in pid_list:
			draw_text(pr.name(),10,ladder+80,20,BLACK)
			draw_rectangle(state_map[pr.status()]*70+100,ladder+80,20,20,BLACK)
			ladder=ladder+40

		clear_background(WHITE)
		end_drawing()

show_output()

