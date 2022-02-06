from cgi import test
from multiprocessing.managers import BaseManager
from optparse import Values
import tkinter as tk
from tkinter import ttk
import pyodbc
import math
import statistics

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
    print(ttest)


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
   CalculatetTest(GMean,BMean,GSD,BSD,len(lst1))
   x=1
   for i in lst1:
       listBox1.insert("", "end", values=(x, i,i-GMean, (i-GMean)*(i-GMean)))
       x=x+1
   listBox2.insert("", "end", values=(1, "The population mean",GMean))
   listBox2.insert("", "end", values=(2, "population standard deviation",GSD))
   listBox2.insert("", "end", values=(3, "the size of the population",len(lst1)))
      
scores = tk.Tk()
scores['bg']='#e303fc'
label1 = tk.Label(scores, text="Calculating Mean Score for Girls", font=("Arial bold",10)).grid(row=0, columnspan=1)
cols = ('SNo', 'Girls(Xi)', '(Xi-Xmean)', 'Sqr(Xi-Xmean)')
listBox1 = ttk.Treeview(scores, columns=cols, show='headings',height=10)
for col in cols:
    listBox1.heading(col, text=col)
listBox1.grid(row=1, column=0,columnspan=1)

label2 = tk.Label(scores, text="Calculating Mean", font=("Arial bold",10)).grid(row=2, columnspan=1)
cols1 = ('SNo', 'Type', 'Value')
listBox2 = ttk.Treeview(scores, columns=cols1, show='headings',height=5)
for col in cols1:
    listBox2.heading(col, text=col)
listBox2.grid(row=3, column=0,columnspan=1)

show1()
scores.mainloop()