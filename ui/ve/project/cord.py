window_aspect = (1200,800)
coord = dict(
	running = ((280,340),(250,330)),
	dead 	= ((120,250),(100,240)),
	parked	= ((300,150),(270,140)),
	uniter	= ((430,200),(400,190)),
	stoped	= ((120,400),(90,390)),
	interp	= ((450,430),(420,420)),
	frozen	= ((290,550),(270,540)),
	zombie	= ((120,560),(100,550)),
	err		= ((60,60),(40,50))
	)

state_map = {
	0x00000001 : "interp",
	0x00000000 : "running",
	0x00000002 : "uniter",
	0x00000004 : "stoped",
	0x00000080 : "dead",
	0x00000040 : "parked",
	0x00008000 : "frozen"
	}


