#! /bin/bash

#flags
verbose="-v";
help="-h";
tst="-t";
run="-r";
#setting up the paths creating temp files sample files
pyt="ve/bin/python3"
path=$(pwd);
rpyt=$path/$pyt;
export path=$path;
echo "checking for local sample file";
if test -f "sample";then
	echo "sample present skipping creation";
else 
	echo "sample not found creating sample file";
	touch "sample";
fi

echo "emptying sample";
echo -n "" > "sample";
echo "removing previos module if initiated";
#sudo rmmod procfs;
#if test $1;then
if test $# != 2;then
	echo "Please provide 2 argument first run flag and second pid";
	exit;
else
	if [[ "$1" =~ -[a-z]* && $2 > 0 ]] ;then
		if test  "$1" = "$verbose"  ;then
			#rm "sample";
			echo "verbose selected;skipping verbose not implemented";
		else
			if test "$1" = "$help" ;then
				cat help_file;
			else
				if test "$1" = "$tst" ;then
					echo "starting test program"
				else
					if test "$1" = "$run";then
						echo "starting program in normal mode";
						echo "sudo insmod module/procfs.ko myint=$2" | bash;
						sleep 1;
						echo "starting frontedn";
						ve/bin/python3 ve/project/test.py;
					fi
				fi

			fi
		fi
	fi
fi
sudo rmmod procfs
#fi

#running the python part for ui.
#$($rpyt "ve/project/test.py");
