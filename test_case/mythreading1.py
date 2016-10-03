# coding = utf-8

from time import sleep, ctime
import threading
loops = [1, 2]
class Threadfunc(object):
    def __init__(self, func, arge, name=''):
        self.name = name
        self.func = func
        self.arges = arge
    def __call__(self):
        self.func(self.arges[0], self.arges[1])
#         apply(loop,(i,loops[i]))
#         loop(nloop, nsec)
def loop(nloop, nsec):
    print('start loop', nloop, ' at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())
def main():
    print('start:', ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=Threadfunc(loop, (i,loops[i]), loop.__name__))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print('all end:', ctime())
if __name__ == '__main__':
    main()
