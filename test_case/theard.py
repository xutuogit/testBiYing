from time import sleep,ctime
import time
import _thread
def loop0():
    print('start loop0 at:',time.ctime())
    sleep(2)
    print('loop0 done at:',ctime())
def loop1():
    print('start loop1 at:',ctime())
    sleep(1)
    print('loop1 done at:',ctime())
def main():
    print('start:',ctime())
    _thread.start_new_thread(loop0,())
    _thread.start_new_thread(loop1,())
    sleep(3)
    print('all end:',ctime())
if __name__ == '__main__':
    main()
