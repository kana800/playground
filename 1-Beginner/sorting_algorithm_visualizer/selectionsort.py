import time
def selectionsort(n,speed,drawdata):
    array_length = len(n)
    for i in range(0,len(n)):
        iMin = i
        for j in range(i+1,len(n)):
            if n[j] < n[iMin]:
                iMin = j
        k = ["pink" for i in range(len(n))]
        k[i],k[iMin]="yellow","yellow"
        n[i],n[iMin]=n[iMin],n[i]
        drawdata(n,k)
        time.sleep(speed)
    drawdata(n,["grey" for x in range(len(n))])

