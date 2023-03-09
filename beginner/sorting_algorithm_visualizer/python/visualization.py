import tkinter as tk
from tkinter import ttk
import random
import time
from bubblesort import bubblesort
from insertionsort import insertionsort
from selectionsort import selectionsort
from mergesort import mergesort
from quicksort import quick_sort

root = tk.Tk()
root.title("sorter")
root.maxsize(900,600)
root.config(bg = "white")


n = tk.StringVar()
data = [] #hold the array

def drawdata(data,color):
    canvas.delete("all")
    c_height = 380
    c_width  = 600
    x_width = c_width / (len(data)+1)
    offset = 30
    spacing = 0
    normalization = [i/(max(data)) for i in data]
    for i , height in enumerate(normalization):
        x0=i*x_width+offset+spacing
        x1=(1+i)*x_width+offset
        y0=c_height - height * 340
        y1=c_height
        
        canvas.create_rectangle(x0,y0,x1,y1,fill=color[i])
        canvas.create_text(x0+3,y0,text=str(data[i]))
    root.update_idletasks()

def Generate():
    global data    
    minimum_value = int(min_entry.get())
    maximum_value = int(max_entry.get())
    sizer = int(size.get())
    data = [random.randrange(minimum_value,maximum_value) for i in range(sizer)]
    drawdata(data,["grey" for i in range(len(data))])        

def startalgorithm():
    global data
    if n.get()=="Bubble Sort":
        bubblesort(data,speedy.get(),drawdata)
    if n.get()=="Selection Sort":
        selectionsort(data,speedy.get(),drawdata)   
    if n.get()=="Insertion Sort":
        insertionsort(data,speedy.get(),drawdata)
    if n.get()=="Merge Sort":
        mergesort(data,speedy.get(),drawdata)
    if n.get() == "Quick Sort":
        quick_sort(data,drawdata,speedy.get())

# Frame 
UI = tk.Frame(root,width=600,height = 200,bg = "white")
UI.grid(row = 0,column = 0,padx=10,pady=5)

# Canvas
canvas = tk.Canvas(root,width = 600,height = 380,bg = "white")
canvas.grid(row =1 ,column = 0, padx = 10,pady = 5)

#First Row
# UserInterface Labels
ttk.Label(UI, text = "Select the Algorithm:").grid(column = 0,row = 0, padx = 5, pady = 5) 

speedy = tk.Scale(UI,from_=0.1,to= 2.0, length = 200, digits = 2,resolution=0.5,orient="horizontal",label = "Speed")
speedy.grid(row=0,column=2,padx=10,pady=10)

# UserInterface Combobox
algorithm_selection_menu = ttk.Combobox(UI,textvariable=n)
algorithm_selection_menu['values']=('Bubble Sort','Insertion Sort','Selection Sort','Merge Sort','Quick Sort')
algorithm_selection_menu.grid(row=0,column=1)
algorithm_selection_menu.current(0)
tk.Button(UI,text="Start",command=startalgorithm).grid(row = 0,column = 3,padx=5,pady=5)
tk.Button(UI,text="Generate",command=Generate).grid(row = 1,column = 3,padx=5,pady=5)

# Second Row
min_entry = tk.Scale(UI,from_=1,to= 100, length = 200, digits = 2,resolution=1,orient="horizontal",label = "min_entry")
min_entry.grid(row=1,column=0,padx=10,pady=10)
max_entry = tk.Scale(UI,from_=100,to= 200, length = 200, digits = 2,resolution=1,orient="horizontal",label = "max_entry")
max_entry.grid(row=1,column=1,padx=10,pady=10)
size = tk.Scale(UI,from_=0,to= 15, length = 100, digits = 2,resolution=1,orient="horizontal",label = "size")
size.grid(row = 1,column = 2,padx=10,pady=10)


root.mainloop()


