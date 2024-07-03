awk '{print $1}' /proc/$c_pid/maps | sed "s/\([a-f0-9]*\)-.*/\1/" > start 
awk '{print $1}' /proc/$c_pid/maps | sed "s/[a-f0-9]*-\(.*\)/\1/" | tail -1 >> start
