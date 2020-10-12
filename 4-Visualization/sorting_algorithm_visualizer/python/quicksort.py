#quick sort algorithm

import time

def quick_sort(data,drawdata,speedy):
    quicksort(data,0,len(data)-1,drawdata,speedy)

def quicksort(arr,start,end,drawdata,speedy):
    
    drawdata(arr,getcolor(len(arr),start,end,start,start))
    time.sleep(speedy)

    if start < end:
        partition_index = partition(arr,start,end,drawdata,speedy)
        
        quicksort(arr,start,partition_index-1,drawdata,speedy)
        quicksort(arr,partition_index+1,end,drawdata,speedy)
    return arr

def partition(arr,start,end,drawdata,speedy):
    pivot = arr[end]
    pIndex = start
    for i in range(start,end):
        if arr[i] < pivot:
            drawdata(arr,getcolor(len(arr),start,end,pIndex,i,True))
            time.sleep(speedy)
            arr[pIndex],arr[i] =arr[i],arr[pIndex]
            pIndex += 1
        drawdata(arr,getcolor(len(arr),start,end,pIndex,i,))
        time.sleep(speedy)
    
    
    drawdata(arr,getcolor(len(arr),start,end,pIndex,i,))
    time.sleep(speedy)    
    arr[pIndex],arr[end] = arr[end],arr[pIndex]
    return (pIndex)

# reference dennislovescoffee
def getcolor(length,start,end,pIndex,current_index,iswapping=False):
    colorarr=[]
    for i in range(length):
        if i >= start and i <=end:
            colorarr.append("yellow")
        else:
            colorarr.append("white")
        if i == end:
            colorarr[i] = "blue"
        if i == pIndex:
            colorarr[i] = "green"
        
        if iswapping:
            if i==pIndex or i==current_index:
                colorarr[i] == "grey"
    return colorarr
