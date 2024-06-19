/^Size:/ {size+=$2}
/^Swap:/ {swap+=$2}
END{
	printf("%d is size , %d is swap %d is number of pages\n",size,swap,size/4);
}

