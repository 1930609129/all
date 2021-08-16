ip = input()
ip1 = int(input())
i=0
while i<ip1:
    i+=1
    fp = open("B:/p.bat","a+")
    print("ping",ip+str(i),file=fp)
    fp.close()