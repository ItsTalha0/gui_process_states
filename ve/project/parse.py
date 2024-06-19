pid=int(input())

print("/proc/"+str(pid)+"/smaps")

f = open("/proc/"+str(pid)+"/maps")

	
