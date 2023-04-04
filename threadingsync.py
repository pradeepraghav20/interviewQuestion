# import threading
# import time
# et = time.time()
# def cal_cube(n):
#     for i in range(1,n):
#         time.sleep(1)
#         print ("Cube->",i**3,end=" ")
#         print()
#
# def cal_square(n):
#     for i in range(1,n):
#         time.sleep(1)
#         print("Square-> ",i**2,end=" ")
#         print()
#
#
# st=time.time()
# cal_square(5)
# cal_cube(5)
# et=time.time()
#
# # t1=threading.Thread(target=cal_square,args=(5,))
# # t2=threading.Thread(target=cal_cube,args=(5,))
# # st=time.time()
# # t1.start()
# # t2.start()
# # et = time.time()
# print('Total time->',et-st)
#
# # time-> 8.079832077026367



import threading
x=0
def thred_task(lock):

    global x
    for i in range(1000000):
        lock.acquire()
        x+=1
        lock.release()

def main_task():
    lock=threading.Lock()
    t1=threading.Thread(target=thred_task,args=(lock,))
    t2=threading.Thread(target=thred_task,args=(lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
main_task()
print(x)