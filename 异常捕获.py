# try:
#     a = int(input())
#     b=int(input())
#     c=a/b
# except BaseException as e:
#     print(e)
# else:
#     print(c)
# finally:   #无论是否出现异常都执行
#     print("卧槽")


# import traceback   #traceback打印异常信息
# try:
#     print(10/0)
# except:
#     traceback.print_exc()