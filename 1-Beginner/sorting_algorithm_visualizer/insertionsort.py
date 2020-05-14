import time
def insertionsort(n,speed,drawdata):
    array_length = len(n)
    for i in range(1,array_length):
        k = ["grey" for i in range(len(n))]
        value = n[i]
        hole = i
        k[hole]="yellow"
        drawdata(n,k)
        while hole > 0 and n[hole-1]>value:
                n[hole] = n[hole-1]
                hole = hole -1
        n[hole]=value
        k[hole]="yellow"
        drawdata(n,k)
        time.sleep(speed)
    drawdata(n,["grey" for x in range(len(n))])
