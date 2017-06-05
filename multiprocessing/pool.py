# -*- coding=utf-8 -*-
from multiprocessing import Pool
import os,time,random
def long_time_task(name):
    print('start %s'%os.getpid())
    start=time.time()
    time.sleep(random.random()*10)
    end=time.time()
    print('spend %s'%(end-start))
if __name__=='__main__':
    print('parent process %s'%os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')