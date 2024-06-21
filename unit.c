#include<stdio.h>
#include<stdlib.h>
#include<poll.h>


#include <unistd.h>

__attribute__((noinline)) static void run_child(void)
{
    pause();
    _exit(0);
}

int main(void)
{
	sleep(20);
    pid_t pid = vfork();

    if (pid == 0) {
        run_child();
    } else if (pid < 0) {
        return 1;
    }

    return 0;
}
