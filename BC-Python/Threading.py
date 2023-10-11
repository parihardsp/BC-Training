"""
Threading Basics:
Single-Threading, Multi-threading.
-- Synchronization mechanisms like locks or semaphores are used to control the order of execution between threads
 """
import time,threading
#
# class Hello(threading.Thread): #inheriting threading.Thread
#     def run(self):
#         for i in range(5):
#             print('Hello')
#             time.sleep(.5)
#
# class Hi(threading.Thread):
#     def run(self):
#         for i in range(5):
#             print('Hi')
#             time.sleep(.5)
#
# '''
# Now creating 2 threads apart from main thread, thread t1 & t2.
# run is a inbuilt function used for threading.
# '''
#
# t1=Hello()
# t2=Hi()
#
# t1.start()
# time.sleep(0.05)
# t2.start()
#
# t1.join()     #waiting for thread t1 to finish
# t2.join()     #waiting for thread t2 to finish
#
# print('Program Executed!')  #executed by main thread

print('-'*80)
#using Function for threading

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

#noraml code takes  seconds to execute
time1=time.perf_counter()
func(4)
func(2)
func(1)
time2=time.perf_counter()
print(f"Time taken by Noramal execution: {time2-time1}")

#using threads:

time1=time.perf_counter()
t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2=time.perf_counter()
print(f"Time taken by Threding method: {time2-time1}")

#Concurrent Futures, ThreadPool executer