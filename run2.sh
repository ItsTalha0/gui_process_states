#! /bin/bash
source ve/bin/activate
echo $@
if [[ $# < 1 ]];then
	echo "atleast one pid";
else
	ve/bin/python3 ve/project/multi.py $@;
fi
