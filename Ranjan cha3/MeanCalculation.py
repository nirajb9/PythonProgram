import decimal
import tkinter as tk
from tkinter import ttk
import pyodbc
import math


def show1():
    lists = ["M","W","M","W","M","M","M","W","M","W","M","M","M","W","W","M","M","M","M","W","W","M","W","M","M","M","W","M","M","M","W","W","W","M","W","M","M","M","W","M","W","M","M","M","M","W","W","M"]
    n1= 30
    n2=18
    R=27
    M = (2*(n1*n2)/(n1+n2))+1
    listBox1.insert("", "end", values=("Mean", M))
    nt = 2*n1*n2*(2*n1*n2-n1-n2)
    dt = (n1+n2)*(n1+n2)*(n1+n2-1)
    SD = nt/dt 
    listBox1.insert("", "end", values=("Standard Deviation", math.sqrt(SD)))
    Z= (R-M)/SD
    listBox1.insert("", "end", values=("z-Statistic", Z))
          
scores = tk.Tk()
scores['bg']='#deb70b'
label1 = tk.Label(scores, text="Run Test(Mean & Standard Daviation Calculation)", font=("Arial bold",10)).grid(row=0, columnspan=1)
cols = ('Label', 'Value')
listBox1 = ttk.Treeview(scores, columns=cols, show='headings',height=20)
for col in cols:
    listBox1.heading(col, text=col)
listBox1.grid(row=1, column=0,columnspan=1)

show1()
scores.mainloop()