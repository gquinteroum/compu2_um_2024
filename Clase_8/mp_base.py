from multiprocessing import Process
import os

def f(name):
    print('hijo en f: ', os.getpid())
    print('padre en f: ', os.getppid())
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    print('hijo: ', p.pid)
    print('padre: ', os.getpid())
    p.join()
