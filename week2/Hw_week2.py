# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 18:29:49 2021

@author: tumur
"""
import os
import pandas as pd
 

# working directory
wd = r'C:\Users\tumur\Documents\python\Introduction_Python\week2'
wd = wd.replace('\\','/')

os.chdir(wd)

df_ind =pd.read_excel('data.xlsx', usecols= 'A:I',header=0)

df_ind[df_ind["age"]>=25][["firstName","lastName","age"]]
df_ind[(df_ind["age"]>=25) & (df_ind["gender"]=="F")][["firstName","lastName","age"]]
