from tkinter import *

#initialization
root = Tk()
root.title("CONTROL")
root.geometry("200x200")
root.resizable(width=False, height=False)

#Display for button funtions
display = Label(root, text="CONTROL", bg='black', fg='green', width=10, height=2)
display.pack()

#button functions
def forward_press():
    display.config(text="FORWARD")
def back_press():
    display.config(text="BACK")
def right_press():
    display.config(text="RIGHT")
def left_press():
    display.config(text="LEFT")
def stop_press():
    display.config(text="STOP")
    
#bottons
forward = Button(root, text = "FORWARD", command = forward_press)
forward.place(x=100, y=70, anchor='c')

back = Button(root, text = "BACK", command = back_press)
back.place(x=100, y=130, anchor='c')

right = Button(root, text = "RIGHT", command = right_press)
right.place(x=165, y=100, anchor='c')

left = Button(root, text = "LEFT", command = left_press)
left.place(x=35, y=100, anchor='c')

stop = Button(root, text = "STOP", command = stop_press)
stop.place(x=100, y=100, anchor='c')


#run
root.mainloop()
