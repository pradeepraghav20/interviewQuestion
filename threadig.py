# # # from threading import Thread,currentThread
# # #
# # # def disp():
# # #     # for i in range(4):
# # #     #     print('Child thred')
# # #
# # #     print(currentThread().name)
# # #
# # #
# # # t=Thread(target=disp())
# # # t.start()
# # # print(t.setName("childthread"))
# # # print(t.getName())
# # # for i in range(4):
# # #     print("Main thread")
# # # print(currentThread().name)
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# #
# # import time
# #
# # import  threading
# # from threading import  *
# # ct=time.time()
# #
# # def square(arr):
# #     for i in arr:
# #         print("Square-",i*i)
# #
# # def cube(arr):
# #     for i in arr:
# #         print("Cube-",i**3)
# #
# # ar = [4, 5, 6, 7, 2] # given array
# # th1=threading.Thread(target=square,args=(ar,))
# # th2=threading.Thread(target=cube,args=(ar,))
# # ct=time.time()
# # th1.start()
# # th2.start()
# # ct=time.time()
# #
# #
# # print("Total time",time.time()-ct)
#
#
# l=[4,4,4,3,33,4,4,4]
#
# res=list(map(lambda a:a**2,l))
# print(res)
#
#
# res=list(filter(lambda a:a%2==0,l))
# print(res)
#
# from functools import  reduce
#
# l=[4,4,4,3,33,4,4,4]
# res=reduce(lambda x,y:x+y,l)
# print(res)


a=[4,4,3,3,33,4,4,3,3,3]

d={}
for i in a:
    d[i]=a.count(i)

print(d)