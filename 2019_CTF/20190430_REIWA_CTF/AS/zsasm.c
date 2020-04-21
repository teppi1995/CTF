/* vim: set ai sw=4 ts=4 ai: */
#include <stdio.h>
#include <sys/mman.h>
#include "seccomp-bpf.h"

int restrict_syscalls()
{
    struct sock_filter filter[] = {
        VALIDATE_ARCHITECTURE,
        EXAMINE_SYSCALL,
        ALLOW_SYSCALL(open),
        ALLOW_SYSCALL(read),
        ALLOW_SYSCALL(write),
        ALLOW_SYSCALL(close),
        ALLOW_SYSCALL(exit),
        KILL_PROCESS,
    };
    struct sock_fprog fprog = {
        sizeof(filter) / sizeof(filter[0]),
        filter,
    };

    if(prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) < 0){
        return -1;
    }

    if(prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &fprog) < 0){
        return -1;
    }

    return 0;
}

int main()
{
	char *buf;
	int cnt, len, bufsize = getpagesize();

	buf = mmap(NULL, bufsize, PROT_READ|PROT_WRITE|PROT_EXEC,
			MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
	len = fread(buf, 1, bufsize, stdin);
	if(len <= 0 || len % 2 != 0){
		return -1;
	}
	for(cnt = 0; cnt < len / 2; cnt++){
		if((buf[2 * cnt] + buf[2 * cnt + 1]) != 0){
			return -1;
		}
	}
	if(restrict_syscalls() < 0) return -1;
	((void(*)())buf)();

	return 0;
}

