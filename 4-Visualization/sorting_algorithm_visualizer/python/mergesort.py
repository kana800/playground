#merge sort algorithm for-loop ~kinda~
import time

# main algorithm
def mergesort(data,sleeper,drawdata):
    merge_sort_algorithm(data,0,len(data)-1,drawdata,sleeper)


def merge_sort_algorithm(data,left,right,drawdata,sleeper):
    if left < right:
        mid = (left+right)//2
        merge_sort_algorithm(data,left,mid,drawdata,sleeper)
        merge_sort_algorithm(data,mid+1,right,drawdata,sleeper)
        merge(data,left,mid,right,drawdata,sleeper)
        

def merge(data,left,mid,right,drawdata,sleeper):
    drawdata(data, colorarray(len(data),left,mid,right))
    time.sleep(sleeper)
    leftpart=data[left:mid+1]
    rightpart = data[mid+1:right+1]

    leftindex = rightindex = 0

    for dataindex  in range(left,right+1):
        if len(leftpart) > leftindex and len(rightpart) > rightindex:
            if leftpart[leftindex] >  rightpart[rightindex]:
                data[dataindex] = rightpart[rightindex]
                rightindex += 1
            else:
                data[dataindex] = leftpart[leftindex]
                leftindex += 1
        elif len(leftpart) > leftindex:
            data[dataindex] = leftpart[leftindex]
            leftindex += 1
        else:
            data[dataindex] = rightpart[rightindex]
            rightindex += 1

    drawdata(data,["pink" if x >= left and x <= right else "blue" for x in range(len(data))])
    time.sleep(sleeper)


def colorarray(n,left,mid,right):
    colorarr=[]
    for i in range(n):
        if i >= left and i <= right:
            if i>=left and i <= mid:
                colorarr.append("yellow")
            else:
                colorarr.append("green")
        else:
            colorarr.append("blue")
    return colorarr
