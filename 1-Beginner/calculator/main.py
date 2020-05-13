import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title = ("Calculator")
root.geometry = (500,500)
root.config(bg = "black")

# font for the Entry
large_font = ('Verdana',15)
# font for Buttons
small_font = ('Verdana',10)

# Frame
frame = tk.Frame(root, width = 500,height = 400 )
frame.grid(row = 1,column = 0)
top_frame = tk.Frame(root,width = 500,height = 100)
top_frame.grid(row = 0,column = 0)



# validation

#vcmd = (top_frame.register(validate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')


# Entry box 
result = tk.StringVar()
entry = tk.Entry(top_frame,textvariable = result,width=30,bg = "black",fg = "white",font = large_font)
entry.grid(row = 0,column = 0,ipady=15)

# validation function
'''
def validate(action, index, value_if_allowed,prior_value, text, validation_type, trigger_type, widget_name):
	if value_if_allowed:
		try:
			float(value_if_allowed)
			return True
		except ValueError:
                	return False
		else:
			return False

'''

def button_click(number):
	current_number = result.get()
	entry.delete(0,"end")
	entry.insert(0,current_number+number)

def button_clear():
	entry.delete(0,"end")

def addition():
	global current_number
	current_number = int(result.get())
	entry.delete(0,"end")
	global selection
	selection = "add"

def multiplication():
	global current_number
	current_number = int(result.get())
	entry.delete(0,"end")

	global selection
	selection = "multiplication"

def substraction():
	global current_number
	current_number = int(result.get())
	entry.delete(0,"end")
	global selection
	selection = "substraction"

def division():
	global current_number
	current_number = int(result.get())
	entry.delete(0,"end")
	global selection
	selection = "division"

def equal():	
	second_number = int(result.get())
	entry.delete(0,"end")

	global current_number
	global selection
	if selection =="add":
		entry.insert(0,int(second_number)+current_number)
	if selection == "multiplication":
		entry.insert(0,current_number*int(second_number))
	if selection == "substraction":
		entry.insert(0,current_number-int(second_number))
	if selection == "division":
		entry.insert(0,current_number/int(second_number))
	

# Defining Buttons and configuring

button_clear = tk.Button(frame,text="C",padx=40,pady=20,command = button_clear,font=small_font)
button_clear.grid(row = 1,column = 0)
button_add_sub = tk.Button(frame,text="+/-",padx=39,pady=20)
button_add_sub.grid(row = 1,column = 1)
button_percentage = tk.Button(frame,text="%",padx=40,pady=20)
button_percentage.grid(row = 1,column = 2)
button_division = tk.Button(frame,text="/",padx=40,pady=20,command=division,bg = "orange",font=small_font)
button_division.grid(row = 1,column = 3)

button_7 = tk.Button(frame,text="7",padx=40,pady=20,command= lambda: button_click("7"))
button_7.grid(row = 2,column = 0)
button_8 = tk.Button(frame,text="8",padx=40,pady=20,command= lambda: button_click("8"))
button_8.grid(row = 2,column = 1)
button_9 = tk.Button(frame,text="9",padx=40,pady=20,command= lambda: button_click("9"))
button_9.grid(row = 2,column = 2)
button_mult = tk.Button(frame,text="*",padx=40,pady=20,command = multiplication,bg = "orange",font=small_font)
button_mult.grid(row = 2,column = 3)


button_4 = tk.Button(frame,text="4",padx=40,pady=20,command= lambda: button_click("6"))
button_4.grid(row = 3,column = 0)
button_5 = tk.Button(frame,text="5",padx=40,pady=20,command= lambda: button_click("5"))
button_5.grid(row = 3,column = 1)
button_6 = tk.Button(frame,text="6",padx=40,pady=20,command= lambda: button_click("4"))
button_6.grid(row = 3,column = 2)
button_substraction = tk.Button(frame,text="-",padx=40,pady=20,command = substraction,bg = "orange",font=small_font)
button_substraction.grid(row = 3,column = 3)

button_1 = tk.Button(frame,text="1",padx=40,pady=20,command= lambda: button_click("1"))
button_1.grid(row = 4,column = 0)
button_2 = tk.Button(frame,text="2",padx=40,pady=20,command= lambda: button_click("2"))
button_2.grid(row = 4,column = 1)
button_3 = tk.Button(frame,text="3",padx=40,pady=20,command= lambda: button_click("3"))
button_3.grid(row = 4,column = 2)
button_addition = tk.Button(frame,text="+",padx=40,pady=20,command = addition,bg = "orange",font=small_font)
button_addition.grid(row = 4,column = 3)

button_0 = tk.Button(frame,text="0",command= lambda: button_click("0"),padx = 40,pady = 20)
button_0.grid(row = 5,column = 0,columnspan = 3)
button_decimal= tk.Button(frame,text=".",padx=40,pady=20)
button_decimal.grid(row = 5,column = 2)
button_equal = tk.Button(frame,text="=",padx=40,pady=20,command = equal,bg = "orange",font=small_font)
button_equal.grid(row = 5,column = 3)

root.mainloop()
