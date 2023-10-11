import multiprocessing
import time

# def f(n):
#     total=0
#     for x in range(n):
#         total += total
#     return total
#
#
# if __name__ == "__main__":
#     time1= time.perf_counter()
#     n=1000
#     p=multiprocessing.Pool()
#     result=p.map(f,range(n))
#     p.close()
#     p.join()
#     time2 = time.perf_counter()
#
#     print(f"It took {time2-time1} seconds, to give the result: {total}")
#

import multiprocessing
import time

def f(n):
    total = 0
    for x in range(n):
        total += x
    return total

if __name__ == "__main__":
    time1 = time.perf_counter()
    n = 10000
    p = multiprocessing.Pool( processes=8)   #it will create 4 processes., deault processes is the max available cores in your system
    result = p.map(f, range(n))
    p.close()
    p.join()
    time2 = time.perf_counter()

    print(f"Using Pool ,it took {time2 - time1} seconds to complete.")
    print(f"The sum of digits form 0 to {n} is: {sum(result)}")

    print()
    time3=time.perf_counter()
    result=[]
    for x in range(10000):
        result.append(f(x))

    time4=time.perf_counter()
    print(f"Using Serial Processing ,it took {time4 - time3} seconds to complete.")
    print(f"The sum of digits form 0 to {n} is: {sum(result)}")


