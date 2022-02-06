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
    os.system('MeanCalculation.py')

def openCalculation2():
    os.system('MeanCalculationBoys.py')

def openCalculation1():
    os.system('TCalculation.py')

root = Tk()
root.geometry('1400x600')
root.title('T- Test')
root['bg']='#e303fc'


Button(root, width=20,font=("Arial bold",10), text='Data Set', command=openAllDataSet).grid(row=1, column=2)

Button(root, width=30,font=("Arial bold",10), text='Mean & SD Calculation(Girls)', command=openCalculation).grid(row=1, column=3)

Button(root, width=30,font=("Arial bold",10), text='Mean & SD Calculation(Boys)', command=openCalculation2).grid(row=1, column=4)

Button(root, width=20,font=("Arial bold",10), text='t Calculation', command=openCalculation1).grid(row=1, column=5)


Label(root, text="T- Test",font=("Arial bold",30)).grid(row=2, column=2, columnspan=6)

root.mainloop()
