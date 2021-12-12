import tkinter as tk
from tkinter import ttk
import pyodbc
import math

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-L16CCO6\SA;'
                      'Database=RegressionDB;'
                      'user id=sa;'
                      'password = 123')



def Multiply(value1,value2):
    return round((value1*value2),2)

def show1():
   cursor = conn.cursor()
   cursor.execute('select * from Table_1')
   for index, row in enumerate(cursor):
        listBox1.insert("", "end", values=(row[0], row[1],row[2], row[3], row[4],row[5]))
        listBox2.insert("", "end", values=(row[0], row[1],row[2], row[3], row[4],row[5],Multiply(row[3],row[3]),Multiply(row[4],row[4]))) 
        listBox3.insert("", "end", values=(row[0], row[1],row[2], row[3], row[4],row[5],Multiply(row[3],row[5]),Multiply(row[4],row[5]))) 
        listBox4.insert("", "end", values=(row[0], row[1],row[2], row[3], row[4],row[5],Multiply(row[3],row[4]))) 

scores = tk.Tk()
scores['bg']='#808000'
label1 = tk.Label(scores, text="Multiple Linear Regression", font=("Arial bold",10)).grid(row=0, columnspan=1)
cols = ('SNo', 'Year', 'Month', 'ROI(x1)', 'ROU(X2)', 'SIP(Y)')
listBox1 = ttk.Treeview(scores, columns=cols, show='headings',height=5)
for col in cols:
    listBox1.heading(col, text=col)
listBox1.grid(row=1, column=0,columnspan=1)

label2 = tk.Label(scores, text="Multiple Linear Regression", font=("Arial bold",10)).grid(row=6, columnspan=1)
cols1 = ('SNo', 'Year', 'Month', 'ROI(x1)', 'ROU(X2)', 'SIP(Y)','X1(Sqrt)','X2(Sqrt)')

listBox2 = ttk.Treeview(scores, columns=cols1, show='headings',height=6)
for col in cols1:
    listBox2.heading(col, text=col)
    listBox2.column(col,width=100)
listBox2.grid(row=7, column=0,columnspan=1)

label3 = tk.Label(scores, text="Multiple Linear Regression", font=("Arial bold",10)).grid(row=10, columnspan=1)
cols2 = ('SNo', 'Year', 'Month', 'ROI(x1)', 'ROU(X2)', 'SIP(Y)','X1*Y','X2*Y')

listBox3 = ttk.Treeview(scores, columns=cols2, show='headings',height=6)
for col in cols2:
    listBox3.heading(col, text=col)
    listBox3.column(col,width=100)
listBox3.grid(row=11, column=0,columnspan=1)


label4 = tk.Label(scores, text="Multiple Linear Regression", font=("Arial bold",10)).grid(row=14, columnspan=1)
cols3 = ('SNo', 'Year', 'Month', 'ROI(x1)', 'ROU(X2)', 'SIP(Y)','X1*X2')

listBox4 = ttk.Treeview(scores, columns=cols3, show='headings',height=6)
for col in cols3:
    listBox4.heading(col, text=col)
    listBox4.column(col,width=100)
listBox4.grid(row=15, column=0,columnspan=1)


show1()

scores.mainloop()