import multiprocessing, time

# square_result=[]
# def calc_square(n):
#     global square_result
#     for i in n:
#         time.sleep(1)
#         print(f"Square of {i}: {i * i}")
#         square_result.append(i*i)
#     print('Within the process the square_result is: ',square_result)
#
#
# def calc_cube(n):
#     for i in n:
#         time.sleep(1)
#         print(f"Cube of {i}: {i * i * i}")
#
#
# if __name__ == "__main__":
#     arr = [2, 3, 9]
#     p1 = multiprocessing.Process(target=calc_square, args=(arr,))
#     p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#     print('Outside of that process the square_result is: ', square_result)
#     print('Done')

'''
Every Process has its own address space (virtual memory). Thus the progran variable are not shared
between 2 processes. You need IPC (InterProcess Communication) technique if you want to share data b/w 2 process.

So, In above example, within function def calc_square(n), it created its own variable named square_result, which is different from the one which you
have outside the function. So this result will not flow back outside of the function.

But in multi-threading we would have gotten the square_result same in both cases, as they shared the memory allocated.
'''

#Sharing memory b/w two processes using shared memory variable.
#Process A
# def calc_square(number,square_result,v):
#     for idx, n in enumerate(number):
#         square_result[idx]=n*n
#     v.value=10
#     print('Value of variable v inside the process is',v.value )
#     print('Within the process the square_result is: ',list(square_result))  #we have to convert it into list type, as its giving memory address of the object
#
# #Process B
# if __name__ == "__main__":
#     arr = [2, 3, 9]
#     square_result=multiprocessing.Array('i',3)
#     v=multiprocessing.Value('i',0)
#     p1 = multiprocessing.Process(target=calc_square, args=(arr,square_result,v))
#
#     p1.start()
#     p1.join()
#
#     print('Value of variable v outside the process is', v.value)
#     print('Outside of that process the square_result is: ', list(square_result))
#     print('Done')
#

print('-'*80)
#using queue/q for sharing data b/w processes

#Process A
def calc_square(numbers,q):
    for n in numbers:
        q.put(n*n)

#Process B
if __name__ == "__main__":
    arr = [2, 3, 9]
    q= multiprocessing.Queue()
    p1 = multiprocessing.Process(target=calc_square, args=(arr,q))

    p1.start()
    p1.join()

    while q.empty() is False:
        print(q.get())
