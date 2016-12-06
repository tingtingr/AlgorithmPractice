# import threading
# from multiprocessing import Queue
# import time
# #perform multiple tasks at  one time
# #shared variables then issues
# #thread using the same variable
# #so you lock the variable. it locks that variable
# #when using lock it, when finished, unlock it 
# #when access, it will just wait
# #lock is like saying, wait for me 
# #a lock per thing
# print_lock = threading.Lock()
# #how many thread s we have what do they do
# def exampleJob(Worker):
# 	time.sleep(0.5)
# 	with print_lock:
# 		print(threading.current_thread().name, worker)

# def worker():
# 	while True:
# 		item = q.get()
# 		do_work(item)
# 		q.task_done()
# q = Queue()

# for i in range(20):
# 	t = threading.Thread(target=worker)
# 	t.daemon = True
# 	t.start()

# for item in source():
# 	q.put(item)
# q.join()

import threading
import time

for i in range(10):
	print(i)
	time.sleep(i)