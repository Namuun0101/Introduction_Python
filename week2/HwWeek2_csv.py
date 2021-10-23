# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 18:29:49 2021

@author: tumur
"""

# Homework Week 2: Task 1-2 "25 буюу түүнээс дээш настай эмэгтэйчүүдийн нэрсийг ялган авч “csv” файл үүсгэ "
import os
import pandas as pd
 

# working directory
wd = r'C:\Users\tumur\Documents\python\Introduction_Python\week2'
wd = wd.replace('\\','/')

os.chdir(wd)

df_ind =pd.read_excel('data.xlsx', usecols= 'A:I',header=0)

df_ind[df_ind["age"]>=25][["firstName","lastName","age"]]
df=df_ind[(df_ind["age"]>=25) & (df_ind["gender"]=="F")][["firstName","lastName","age"]]

df.to_csv(r'C:\Users\tumur\Documents\python\Introduction_Python\week2\HwWeek2.csv', index=None, header=True)



# Homework Week 2: Task 1-3 "23-аас доош настай эрэгтэйчүүдийн нэрсийг ялган авч “json” файл үүсгэ (loop ашиглахгүй)"
df_ind =pd.read_excel('data.xlsx', usecols= 'A:I',header=0)
df=df_ind[(df_ind["age"]<23) & (df_ind["gender"]=="M")][["firstName","lastName","age"]]

df.to_json(r'C:\Users\tumur\Documents\python\Introduction_Python\week2\HwWeek2.json')
