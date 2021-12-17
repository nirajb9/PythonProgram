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

def openCalculation1():
    os.system('LogitCalculation.py')

def openCalculation2():
    os.system('OddsCalculation.py')

root = Tk()
root.geometry('1400x600')
root.title('Logistic Regression Assumptions')
root['bg']='#436fba'

Button(root, width=20,font=("Arial bold",10), text='Data Set', command=openAllDataSet).grid(row=1, column=2)

Button(root, width=20,font=("Arial bold",10), text='Mean Calculation', command=openCalculation).grid(row=1, column=3)

Button(root, width=20,font=("Arial bold",10), text='Logit Calculation', command=openCalculation1).grid(row=1, column=4)

Button(root, width=20,font=("Arial bold",10), text='Odds Calculation', command=openCalculation2).grid(row=1, column=5)

Label(root, text="Logistic Regression Assumptions",font=("Arial bold",30)).grid(row=2, column=8)

root.mainloop()
