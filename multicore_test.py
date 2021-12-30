from multiprocessing import Pool
import time

CORES = 4
def func(num):
    a = num**2+10 - 3

a_pool = Pool(CORES)
start = time.time()
result = a_pool.map(func, range(10))
print("time taken: "+str(time.time()-start))