import tkinter as tk
from tkinter import ttk
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-L16CCO6\SA;'
                      'Database=RegressionDB;'
                      'user id=sa;'
                      'password = 123')

cursor = conn.cursor()
cursor.execute('select * from Table_1')

def Percent(value,total):
    return round((value*100)/total)

def show():
    #for row in cursor:
  
   for index, row in enumerate(cursor):
        listBox1.insert("", "end", values=(row[0], row[1],row[2], row[3], row[4],row[5])) 
scores = tk.Tk()
scores['bg']='#808000'
label1 = tk.Label(scores, text="Multiple Linear Regression DataSet", font=("Arial bold",10)).grid(row=0, columnspan=3)
cols = ('SNo', 'Year', 'Month', 'ROI(x1)', 'ROU(X2)', 'SIP(Y)')
listBox1 = ttk.Treeview(scores, columns=cols, show='headings',height=15)
for col in cols:
    listBox1.heading(col, text=col) 
listBox1.grid(row=1, column=0,columnspan=4)

show()
scores.mainloop()