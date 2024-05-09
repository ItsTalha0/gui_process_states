#include<stdio.h>
#include<unistd.h>

int main()
{
	getchar();
	sleep(2);
	while(1)
	{
		printf("jput\n");
		getchar();
		int i=0;
		while(i<10000000)i++;
	}
}

		
