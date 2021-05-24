#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math

# Fungi yang akan digunakan
def f(x):
    return x**2 - 3*x -2

# Penentuan metode bisection
def bisection(x0,x1,e):
    step = 1
    
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iterasi ke -%d, x2 = %0.6f dan f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
        condition = abs(f(x2)) > e

    print('\nAkar yang dibutuhkan : %0.8f' % x2)


# Baris untuk memasukkan nilai
x0 = input('Titik Awal: ')
x1 = input('Titik Kedua: ')
e = input('Batasan error: ')

# Merubah nilai input menjadi float
x0 = float(x0)
x1 = float(x1)
e = float(e)

# Pengecekan awal nilai bisection
if f(x0) * f(x1) > 0.0:
    print('Nilai yang dimasukkan tidak masuk dalam kurungan.')
    print('Coba dengan nilai baru.')
else:
    bisection(x0,x1,e)


# In[13]:


import math

# Fungi yang akan digunakan
def f(x):
    return x*x*x + x**2 - 3*x -2

# Penentuan metode bisection
def bisection(x0,x1,e):
    step = 1
    
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iterasi ke -%d, x2 = %0.6f dan f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
        condition = abs(f(x2)) > e

    print('\nAkar yang dibutuhkan : %0.8f' % x2)


# Baris untuk memasukkan nilai
x0 = input('Titik Awal: ')
x1 = input('Titik Kedua: ')
e = input('Batasan error: ')

# Merubah nilai input menjadi float
x0 = float(x0)
x1 = float(x1)
e = float(e)

# Pengecekan awal nilai bisection
if f(x0) * f(x1) > 0.0:
    print('Nilai yang dimasukkan tidak masuk dalam kurungan.')
    print('Coba dengan nilai baru.')
else:
    bisection(x0,x1,e)


# In[ ]:




