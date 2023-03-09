import time
def bubblesort(n,speed,drawdata):
    x = len(n)
    for p in range(x):
        for i in range(0,x-1):
            if n[i] > n[i+1]:
                n[i],n[i+1]=n[i+1],n[i]
                drawdata(n,["black" if x == i or x==i+1 else 'grey' for x in range(len(n))])
                time.sleep(speed)
    drawdata(n,["grey" for x in range(len(n))])
