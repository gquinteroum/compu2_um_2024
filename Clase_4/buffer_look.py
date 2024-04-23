import os
os.pipe()
pid = os.fork()


if pid > 0:
    print('PADRE: ', os.getpid())
    input()
    os.wait()

else:
    print('HIJO: ', os.getpid())
    input()
