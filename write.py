from multiprocessing import Pool
import time
import os.path
import datetime 
import sys
from multiprocessing import Pool
import time
import os.path
import datetime 

CORES = 10
def func(num):
    a = num**2+10 - 3

a_pool = Pool(CORES)
start = time.time()
result = a_pool.map(func, range(10000000))
print("time taken: "+str(time.time()-start))

save_path = './'
name_of_file = 'test_document-'+str(sys.argv[1])
completeName = os.path.join(save_path, name_of_file+".txt")         

file1 = open(completeName, "w")

toFile =str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

file1.write(toFile)

file1.close()