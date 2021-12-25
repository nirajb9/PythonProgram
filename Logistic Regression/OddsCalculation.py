import decimal
import tkinter as tk
from tkinter import ttk
import pyodbc
import math

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MUM-NIRAJB1;'
                      'Database=DemoDB1;'
                      'Trusted_Connection=True')
def Multiply(value1,value2):
    return round((value1*value2),2)

def Difference(value1,value2):
    return value1-value2

def show1():
   cursor = conn.cursor()
   cursor.execute('select * from Table_1')
   count=0
   countY=0
   for index, row in enumerate(cursor):
        count=count + row[0]
        countY=countY + row[1]
   cursor1 = conn.cursor()
   cursor1.execute('select * from Table_1')
   d3Sum=0
   d4Sum=0
   m=0
   b=0
   for index, row in enumerate(cursor1):
        Xbar= round(count/20,2)
        Ybar= round(countY/20,2)
        d1 =Difference(row[0],Xbar)
        d2 =Difference(row[1],Ybar)
        d3 =decimal.Decimal(d1)* decimal.Decimal(d2)
        d4 = d1*d1
        d3Sum = d3Sum+d3
        d4Sum = d4Sum+d4
        m= round(d3Sum/d4Sum,4)
        #listBox1.insert("", "end", values=(row[0], row[1],d1,d2,d3,d4))
        b=decimal.Decimal(Ybar)- decimal.Decimal((m*Xbar))
        #listBox1.insert("", "end", values=(d3Sum,d4Sum,m,Xbar,Ybar,b))
   cursor2 = conn.cursor()
   cursor2.execute('select * from Table_1')
   for index, row in enumerate(cursor2):
       y= (m*row[0])+b
       listBox1.insert("", "end", values=(row[0],row[1],y,math.exp(y)))
        
   
scores = tk.Tk()
scores['bg']='#436fba'
label1 = tk.Label(scores, text="Odds Catculation", font=("Arial bold",10)).grid(row=0, columnspan=1)
cols = ('Hours(x)', 'Pass(y)', 'Logit','Odds')
listBox1 = ttk.Treeview(scores, columns=cols, show='headings',height=20)
for col in cols:
    listBox1.heading(col, text=col)
listBox1.grid(row=1, column=0,columnspan=1)

show1()

scores.mainloop()