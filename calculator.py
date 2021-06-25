from tkinter import *

root =Tk()
root.geometry("300x354")
root.resizable(False,False)
root.title("Calculator")

expression=""
input_text = StringVar(root)

def btn_click(item):
    global expression
    expression = expression +str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    input_text.set("")

def bt_equal():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=""        



input_field=Entry(root,bd=2,textvariable=input_text,justify=RIGHT)
input_field.place(x=25,y=40,height=40,width=250)


clear = Button(root, text = "Clear", fg = "black", width = 32, height = 5, bd = 2, bg = "#eee",border=4,  command = lambda: bt_clear())
clear.place(x=25,y=10,height=20,width=50)


seven = Button(root, text = "7", fg = "black", width = 7, height = 3, bd = 2, bg = "#fff", command = lambda: btn_click(7))
seven.place(x=37,y=90)
eight = Button(root, text = "8", fg = "black", width = 7, height = 3, bd = 2, bg = "#fff", command = lambda: btn_click(8))
eight.place(x=97,y=90)
nine = Button(root, text = "9", fg = "black", width = 7, height = 3, bd = 2, bg = "#fff", command = lambda: btn_click(9))
nine.place(x=157,y=90)
multiply = Button(root, text = "*", fg = "black", width = 7, height = 3, bd = 2, bg = "#eee", command = lambda: btn_click("*"))
multiply.place(x=217,y=90)

four = Button(root, text = "4", fg = "black", width = 7, height = 3, bd = 2, bg = "#fff", command = lambda: btn_click(4))
four.place(x=37,y=150)
five = Button(root, text = "5", fg = "black", width = 7, height = 3, bd = 2, bg = "#fff", command = lambda: btn_click(5))
five.place(x=97,y=150)
six = Button(root, text = "6", fg = "black", width = 7, height = 3, bd = 2, bg = "#fff", command = lambda: btn_click(6))
six.place(x=157,y=150)
minus = Button(root, text = "-", fg = "black", width = 7, height = 3, bd = 2, bg = "#eee", command = lambda: btn_click("-"))
minus.place(x=217,y=150)

one = Button(root, text = "1", fg = "black", width = 7, height = 3, bd = 2, bg = "#fff", command = lambda: btn_click(1))
one.place(x=37,y=210)
two = Button(root, text = "2", fg = "black", width = 7, height = 3, bd = 2, bg = "#fff", command = lambda: btn_click(2))
two.place(x=97,y=210)
three = Button(root, text = "3", fg = "black", width = 7, height = 3, bd = 2, bg = "#fff", command = lambda: btn_click(3))
three.place(x=157,y=210)
plus = Button(root, text = "+", fg = "black", width = 7, height = 3, bd = 2, bg = "#eee", command = lambda: btn_click("+"))
plus.place(x=217,y=210)

point = Button(root, text = ".", fg = "black", width = 7, height = 3, bd = 2, bg = "#eee", command = lambda: btn_click("."))
point.place(x=37,y=270)
zero = Button(root, text = "0", fg = "black", width = 7, height = 3, bd = 2, bg = "#fff", command = lambda: btn_click(0))
zero.place(x=97,y=270)
equals = Button(root, text = "=", fg = "black", width = 7, height = 3, bd = 2, bg = "#eee", command = lambda: bt_equal())
equals.place(x=157,y=270)
divide = Button(root, text = "/", fg = "black", width = 7, height = 3, bd = 2, bg = "#eee",  command = lambda: btn_click("/"))
divide.place(x=217,y=270)

root.mainloop()