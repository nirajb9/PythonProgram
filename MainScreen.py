import sys
import os
import tkinter as Tk
from tkinter import * 
import time
import sqlite3
import random
import tempfile


f = ''
flag = ''
flags = ''


def openAllDataSet():
    os.system('AllDataSet.py')

def openCalculation():
    os.system('TableCalculation.py')

def openCalculation1():
    os.system('RegrassionCalculation.py')




root = Tk()
root.geometry('1400x600')
root.title('Multiple Linear Regression')
root['bg']='#808000'


Button(root, width=20,font=("Arial bold",10), text='Data Set', command=openAllDataSet).grid(row=1, column=2)

Button(root, width=20,font=("Arial bold",10), text='Table Calculation', command=openCalculation).grid(row=1, column=3)

Button(root, width=20,font=("Arial bold",10), text='Calculation', command=openCalculation1).grid(row=1, column=4)


Label(root, text="Multiple Linear Regression",font=("Arial bold",30)).grid(row=2, column=8)

root.mainloop()
