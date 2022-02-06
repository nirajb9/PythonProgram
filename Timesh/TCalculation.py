from cgi import test
from multiprocessing.managers import BaseManager
from optparse import Values
import tkinter as tk
from tkinter import ttk
import pyodbc
import math
import statistics
from PIL import ImageTk,Image  

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MUM-NIRAJB1;'
                      'Database=DemoDB3;'
                      'Trusted_Connection=True'
                      )

data1 = [1, 3, 4, 5, 7, 9, 2]
def Multiply(value1,value2):
    return round((value1*value2),2)

def CalculatetTest(m1,m2,sd1,sd2,length):
    up = (m2-m1)-15
    dsqrt = math.sqrt(((sd1*sd1)/length) + ((sd2*sd2)/length))
    ttest = up/dsqrt
    return ttest

    

def show1():
   lst1 = []
   lst2 = []
   cursor = conn.cursor()
   cursor.execute('select * from Table_1')
   for index, row in enumerate(cursor):
       lst1.append(row[1])
       lst2.append(row[2])
   GMean = statistics.mean(lst1)
   BMean = statistics.mean(lst2)
   GSD = statistics.stdev(lst1)
   BSD =statistics.stdev(lst2)
   
   x=1
   for i in lst1:
       x=x+1
   listBox2.insert("", "end", values=(1, "The population mean(Girls)",GMean))
   listBox2.insert("", "end", values=(2, "Population standard deviation(Girls)",GSD))
   listBox2.insert("", "end", values=(3, "The population mean(Boys)",BMean))
   listBox2.insert("", "end", values=(4, "Population standard deviation(Boys)",BSD))
   listBox2.insert("", "end", values=(5, "The size of the population",len(lst1)))
   listBox2.insert("", "end", values=(6, "t Calculation",CalculatetTest(GMean,BMean,GSD,BSD,len(lst1))))
   
scores = tk.Tk()
scores['bg']='#e303fc'

label2 = tk.Label(scores, text="t-Calculating", font=("Arial bold",10)).grid(row=2, columnspan=1)
cols1 = ('SNo', 'Type', 'Value')
listBox2 = ttk.Treeview(scores, columns=cols1, show='headings',height=8)
for col in cols1:
    listBox2.heading(col, text=col)
listBox2.grid(row=3, column=0,columnspan=1)

x = 'I1.png'
img = Image.open(x)
img = img.resize((350, 350), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = tk.Label(scores, image=img).grid(row=9, columnspan=1)

show1()

scores.mainloop()