
#include <sys/sendfile.h>
#include <sys/types.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <assert.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>
#include <stdint.h>
#include <stdio.h>
#include <fcntl.h>

void win(int);
int vuln(int, char**, char**);

int asdf()
{
    __asm__ __volatile__ (
        ".intel_syntax noprefix;"
		"push rdi;"
		"pop rdi;"
		"ret;"
        ".att_syntax;"
		:
		:
		:
	);
	exit(0);
}

int main(int argc, char **argv, char **envp)
{
	puts("===================================================");
	printf("\tWelcome to %s!\n", argv[0]);
	puts("===================================================");
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 1);

	return vuln(argc, argv, envp);
}

int vuln(int argc, char **argv, char **envp)
{

	struct { char input[232]; uint64_t n; volatile struct {unsigned char p0[1]; unsigned char b0; unsigned char p1[3]; unsigned char b1; unsigned char p2[3]; unsigned char b2; unsigned char p3[3]; unsigned char b3; unsigned char p4[2]; unsigned char b4; unsigned char p5[3]; unsigned char b5; unsigned char p6[2]; unsigned char b6; unsigned char p7[2]; unsigned char b7;} __attribute__((packed)) wincheck; } frame;
	uint64_t *n = &frame.n;
	char *input = (char *)&frame.input;
	volatile struct {unsigned char p0[1]; unsigned char b0; unsigned char p1[3]; unsigned char b1; unsigned char p2[3]; unsigned char b2; unsigned char p3[3]; unsigned char b3; unsigned char p4[2]; unsigned char b4; unsigned char p5[3]; unsigned char b5; unsigned char p6[2]; unsigned char b6; unsigned char p7[2]; unsigned char b7;} __attribute__((packed)) *win_check = &frame.wincheck;

	short size;
	printf("Payload size? ");
	scanf("%hi", &size);
	assert(size <= 240);
	printf("Send your payload (up to %d bytes)!\n", size);
	read(0, input, (unsigned short)size);
puts(win_check);	if (win_check->b0 == 94 && win_check->b1 == 80 && win_check->b2 == 245 && win_check->b3 == 74 && win_check->b4 == 146 && win_check->b5 == 138 && win_check->b6 == 23 && win_check->b7 == 185) win(0x1337);
	else puts("You lose!");

	puts("Goodbye!");
	return 0;
}

void win(int win_token)
{

	puts("You win! Here is your flag:");
	register int flag_fd = open("/flag", 0);
	sendfile(1, flag_fd, 0, 1024);
}
