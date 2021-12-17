import tkinter as tk
from tkinter import ttk
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MUM-NIRAJB1;'
                      'Database=DemoDB1;'
                      'Trusted_Connection=True'
                      )
                      

cursor = conn.cursor()
cursor.execute('select * from Table_1')

def Percent(value,total):
    return round((value*100)/total)

def show():
    #for row in cursor:
  
   for index, row in enumerate(cursor):
        listBox1.insert("", "end", values=(row[0], row[1])) 
scores = tk.Tk()
scores['bg']='#436fba'
label1 = tk.Label(scores, text="Logistic Regression Assumptions DataSet", font=("Arial bold",10)).grid(row=0, columnspan=3)
cols = ('SNo', 'Year')
listBox1 = ttk.Treeview(scores, columns=cols, show='headings',height=20)
for col in cols:
    listBox1.heading(col, text=col) 
listBox1.grid(row=1, column=0,columnspan=4)

show()
scores.mainloop()