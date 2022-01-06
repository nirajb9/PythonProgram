import tkinter as tk
from tkinter import ttk
import pyodbc


def show():
    #for row in cursor:
   list = ["M","W","M","W","M","M","M","W","M","W","M","M","M","W","W","M","M","M","M","W","W","M","W","M","M","M","W","M","M","M","W","W","W","M","W","M","M","M","W","M","W","M","M","M","M","W","W","M"]
  
   templist = [0,12,24,36]
   for j in templist:
    listBox1.insert("", "end", values=(list[j],list[j+1],list[j+2],list[j+3],list[j+4],list[j+5],list[j+6],list[j+7],list[j+8],list[j+9],list[j+10],list[j+11]))
    
   
scores = tk.Tk()
scores['bg']='#deb70b'
label1 = tk.Label(scores, text="Run Test DataSet", font=("Arial bold",10)).grid(row=0, columnspan=3)
cols = ('','','','','','','','','','','','')

listBox1 = ttk.Treeview(scores,columns=cols, show='headings',height=20)
i=0
for col in cols:
    listBox1.heading(col, text=col)
    listBox1.column('# '+str(i),width=70) 
    i=i+1
    
listBox1.grid(row=1, column=0,columnspan=4)

show()
scores.mainloop()