from time import sleep
n1 = 9
n2 = 59
print("10:00")
print("{}:{}".format(n1, n2))
while(n1 >=0 ):
    n2-= 1
    if(n2 < 0):
        n1-= 1
        n2 = 59
    if(n2 >= 0):
        print("{}:{}".format(n1, str(n2).zfill(2)))
    sleep(1)

