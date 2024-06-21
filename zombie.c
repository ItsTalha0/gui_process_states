#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>


int main()
{
	int p = fork();
	if( p==0 )
	{
		int i=0;
		while( i<10000 )
		{
			i++;
		}
		exit(0);
	}
	else
	{
		while(1);
	}
}

