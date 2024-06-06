#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>

int main()
{
	int i=0;
	while(1)
	{
		sleep(2);
		while(i<1000000000)i++;
		sleep(3);
		i=0;
	}
}

