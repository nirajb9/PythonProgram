import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import pyodbc
import math
from functools import partial
import decimal

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-L16CCO6\SA;'
                      'Database=RegressionDB;'
                      'user id=sa;'
                      'password = 123')


def Multiply(value1,value2):
    return round((value1*value2),2)

def show1():
   SX1 = 0
   SX2=0
   SY=0
   SSX1 =0
   SSX2=0
   SSX1Y=0
   SSX2Y=0
   SSX1Y1=0
  
   
   cursor = conn.cursor()
   cursor.execute('select * from Table_1')
   for index, row in enumerate(cursor):
       SX1 = SX1+row[3]
       SX2= SX2+row[4]
       SY= SY+row[5]
       SSX1= SSX1+Multiply(row[3],row[3])
       SSX2=SSX2+Multiply(row[4],row[4])
       SSX1Y = SSX1Y+Multiply(row[3],row[5])
       SSX2Y= SSX2Y+Multiply(row[4],row[5])
       SSX1Y1= SSX1Y1+Multiply(row[3],row[4])
    
   listBox2.insert("", "end", values=('Sum(X1)', SX1))
   listBox2.insert("", "end", values=('Sum(X2)', SX2))
   listBox2.insert("", "end", values=('Sum(Y)', SY))
   listBox2.insert("", "end", values=('Sum(Sqrt X1)', SSX1))
   listBox2.insert("", "end", values=('Sum(Sqrt X2)', SSX2))
   listBox2.insert("", "end", values=('Sum(X1*Y)', SSX1Y))
   listBox2.insert("", "end", values=('Sum(X2*Y)', SSX2Y))
   listBox2.insert("", "end", values=('Sum(X1*Y1)', SSX1Y1))

   SSX1C  = SSX1 - ((SX1*SX1)/24)
   SSX2C  = SSX2 - ((SX2*SX2)/24)
   listBox2.insert("", "end", values=('Sum(X1 Calculation)', round(SSX1C,2)))
   listBox2.insert("", "end", values=('Sum(X2 Calculation)', round(SSX2C,2)))
   SSX1YC =  SSX1Y - ((SX1*SY)/24)
   SSX2YC =  SSX2Y - ((SX2*SY)/24) 
   listBox2.insert("", "end", values=('Sum(X1Y Calculation)', round(SSX1YC,2)))
   listBox2.insert("", "end", values=('Sum(X2Y Calculation)', round(SSX2YC,2)))
   SSX1Y1C= SSX1Y1 - ((SX1*SX2)/24)
   listBox2.insert("", "end", values=('Sum(X1X2 Calculation)', round(SSX1Y1C,2)))
#    b1 = ((SSX2C*SSX1YC)-(SSX1Y1C*SSX2YC))/ ((SSX1C*SSX2C)-(SSX1Y1C*SSX1Y1C))
#    listBox2.insert("", "end", values=('b1', round(b1,2)))
   
#    b2 = ((SSX1C*SSX2YC)-(SSX1Y1C*SSX1YC))/ ((SSX1C*SSX2C)-(SSX1Y1C*SSX1Y1C))
#    listBox2.insert("", "end", values=('b2', round(b2,2)))

#    b0 = 1070.88-(float(b1)*2.07)-(float(b2)*5.77)
#    listBox2.insert("", "end", values=('b0', round(b0,2)))

def show2():
   SX1 = 0
   SX2=0
   SY=0
   SSX1 =0
   SSX2=0
   SSX1Y=0
   SSX2Y=0
   SSX1Y1=0
   label3 = tk.Label(scores, text="b1 Calculation", font=("Arial bold",10)).grid(row=3, column=0)
   cols2 = ('Value','Result')
   listBox3 = ttk.Treeview(scores, columns=cols2, show='headings',height=2)
   for col in cols2:
     listBox3.heading(col, text=col) 
     listBox3.grid(row=4, column=0,columnspan=3)
  
   cursor = conn.cursor()
   cursor.execute('select * from Table_1')
   for index, row in enumerate(cursor):
       SX1 = SX1+row[3]
       SX2= SX2+row[4]
       SY= SY+row[5]
       SSX1= SSX1+Multiply(row[3],row[3])
       SSX2=SSX2+Multiply(row[4],row[4])
       SSX1Y = SSX1Y+Multiply(row[3],row[5])
       SSX2Y= SSX2Y+Multiply(row[4],row[5])
       SSX1Y1= SSX1Y1+Multiply(row[3],row[4])


   SSX1C  = SSX1 - ((SX1*SX1)/24)
   SSX2C  = SSX2 - ((SX2*SX2)/24)

   SSX1YC =  SSX1Y - ((SX1*SY)/24)
   SSX2YC =  SSX2Y - ((SX2*SY)/24) 

   SSX1Y1C= SSX1Y1 - ((SX1*SX2)/24)

   b1 = ((SSX2C*SSX1YC)-(SSX1Y1C*SSX2YC))/ ((SSX1C*SSX2C)-(SSX1Y1C*SSX1Y1C))
   listBox3.insert("", "end", values=('b1', round(b1,2)))
   
#    b2 = ((SSX1C*SSX2YC)-(SSX1Y1C*SSX1YC))/ ((SSX1C*SSX2C)-(SSX1Y1C*SSX1Y1C))
#    listBox3.insert("", "end", values=('b2', round(b2,2)))

#    b0 = 1070.88-(float(b1)*2.07)-(float(b2)*5.77)
#    listBox3.insert("", "end", values=('b0', round(b0,2)))

def show3():
   SX1 = 0
   SX2=0
   SY=0
   SSX1 =0
   SSX2=0
   SSX1Y=0
   SSX2Y=0
   SSX1Y1=0
   label4 = tk.Label(scores, text="b2 Calculation", font=("Arial bold",10)).grid(row=5, column=0)
   cols2 = ('Value','Result')
   listBox4 = ttk.Treeview(scores, columns=cols2, show='headings',height=2)
   for col in cols2:
     listBox4.heading(col, text=col) 
     listBox4.grid(row=6, column=0,columnspan=3)
  
   cursor = conn.cursor()
   cursor.execute('select * from Table_1')
   for index, row in enumerate(cursor):
       SX1 = SX1+row[3]
       SX2= SX2+row[4]
       SY= SY+row[5]
       SSX1= SSX1+Multiply(row[3],row[3])
       SSX2=SSX2+Multiply(row[4],row[4])
       SSX1Y = SSX1Y+Multiply(row[3],row[5])
       SSX2Y= SSX2Y+Multiply(row[4],row[5])
       SSX1Y1= SSX1Y1+Multiply(row[3],row[4])


   SSX1C  = SSX1 - ((SX1*SX1)/24)
   SSX2C  = SSX2 - ((SX2*SX2)/24)

   SSX1YC =  SSX1Y - ((SX1*SY)/24)
   SSX2YC =  SSX2Y - ((SX2*SY)/24) 

   SSX1Y1C= SSX1Y1 - ((SX1*SX2)/24)

   b1 = ((SSX2C*SSX1YC)-(SSX1Y1C*SSX2YC))/ ((SSX1C*SSX2C)-(SSX1Y1C*SSX1Y1C))
#    listBox3.insert("", "end", values=('b1', round(b1,2)))
   
   b2 = ((SSX1C*SSX2YC)-(SSX1Y1C*SSX1YC))/ ((SSX1C*SSX2C)-(SSX1Y1C*SSX1Y1C))
   listBox4.insert("", "end", values=('b2', round(b2,2)))

#    b0 = 1070.88-(float(b1)*2.07)-(float(b2)*5.77)
#    listBox3.insert("", "end", values=('b0', round(b0,2)))

def show4():
   SX1 = 0
   SX2=0
   SY=0
   SSX1 =0
   SSX2=0
   SSX1Y=0
   SSX2Y=0
   SSX1Y1=0
   label5 = tk.Label(scores, text="b0 Calculation", font=("Arial bold",10)).grid(row=7, column=0)
   cols2 = ('Value','Result')
   listBox5 = ttk.Treeview(scores, columns=cols2, show='headings',height=2)
   for col in cols2:
     listBox5.heading(col, text=col) 
     listBox5.grid(row=8, column=0,columnspan=3)
  
   cursor = conn.cursor()
   cursor.execute('select * from Table_1')
   for index, row in enumerate(cursor):
       SX1 = SX1+row[3]
       SX2= SX2+row[4]
       SY= SY+row[5]
       SSX1= SSX1+Multiply(row[3],row[3])
       SSX2=SSX2+Multiply(row[4],row[4])
       SSX1Y = SSX1Y+Multiply(row[3],row[5])
       SSX2Y= SSX2Y+Multiply(row[4],row[5])
       SSX1Y1= SSX1Y1+Multiply(row[3],row[4])


   SSX1C  = SSX1 - ((SX1*SX1)/24)
   SSX2C  = SSX2 - ((SX2*SX2)/24)

   SSX1YC =  SSX1Y - ((SX1*SY)/24)
   SSX2YC =  SSX2Y - ((SX2*SY)/24) 

   SSX1Y1C= SSX1Y1 - ((SX1*SX2)/24)

   b1 = ((SSX2C*SSX1YC)-(SSX1Y1C*SSX2YC))/ ((SSX1C*SSX2C)-(SSX1Y1C*SSX1Y1C))
#    listBox3.insert("", "end", values=('b1', round(b1,2)))
   
   b2 = ((SSX1C*SSX2YC)-(SSX1Y1C*SSX1YC))/ ((SSX1C*SSX2C)-(SSX1Y1C*SSX1Y1C))
   #listBox4.insert("", "end", values=('b2', round(b2,2)))

   b0 = 1070.88-(float(b1)*2.07)-(float(b2)*5.77)
   listBox5.insert("", "end", values=('b0', round(b0,2)))
   e1 = Entry(scores, width=20)
   e1.grid(row=9,column=0)

   e2 = Entry(scores, width=20)
   e2.grid(row=9, column=1)
   
   button4 = tk.Button(scores, text="Calculate Y",font=("Arial bold",10), background='yellow', width=20, command=partial(calculateY,b0,b1,b2,e1,e2)).grid(row=9, column=2)

def calculateY(b0,b1,b2,e1,e2):
    X1R= decimal.Decimal(e1.get())
    X2R= decimal.Decimal(e2.get())
    b0d = decimal.Decimal(b0)
    b1d = decimal.Decimal(b1)
    b2d = decimal.Decimal(b2)
    YCalculation = b0d+(b1d*X1R)+(b2d*X2R)
    label7 = tk.Label(scores, text="Y Calculation", font=("Arial bold",10)).grid(row=10, column=0)
    label6 = tk.Label(scores, text= round(YCalculation,3), font=("Arial bold",10)).grid(row=10, column=1)


       
      
scores = tk.Tk()
scores['bg']='#808000'
label2 = tk.Label(scores, text="Regrassion Calculation", font=("Arial bold",10)).grid(row=0, column=0)
button1 = tk.Button(scores, text="Calculate b1",font=("Arial bold",10), background='yellow', width=20, command=show2).grid(row=0, column=1)
button2 = tk.Button(scores, text="Calculate b2",font=("Arial bold",10), background='yellow', width=20, command=show3).grid(row=0, column=2)
button3 = tk.Button(scores, text="Calculate b0",font=("Arial bold",10), background='yellow', width=20, command=show4).grid(row=0, column=3)




cols1 = ('Value','Result')
listBox2 = ttk.Treeview(scores, columns=cols1, show='headings',height=12)
for col in cols1:
    listBox2.heading(col, text=col) 
    listBox2.grid(row=2, column=0,columnspan=3)


show1()

scores.mainloop()