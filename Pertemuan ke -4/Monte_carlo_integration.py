#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy import random
import numpy as np
import matplotlib.pyplot as plt


a = 0
b = np.pi
N = 1000

def func(x):
    return np.sin(x)

integral = 0.0

answer = (b - a) / float(N) * integral

areas = []

for i in range (N):
    xrand = np.zeros(N)
    
    for i in range(len(xrand)):
        xrand[i] = random.uniform(a,b)
        integral = 0.0
        
    for i in range(N):
        integral = integral + func(xrand[i])
    
    answer = (b-a)/float(N)*integral
    areas.append(answer)

plt.title("Distribution of Areas Calculated")
plt.hist(areas, bins = 30, ec = 'black')
plt.xlabel("Areas")

print(" The Answer of areas {}".format(areas))


# In[2]:


from scipy import random
import numpy as np
import matplotlib.pyplot as plt


a = 0
b = np.pi
N = 1000

def func(x):
    return x**2

integral = 0.0

answer = (b - a) / float(N) * integral

areas = []

for i in range (N):
    xrand = np.zeros(N)
    
    for i in range(len(xrand)):
        xrand[i] = random.uniform(a,b)
        integral = 0.0
        
    for i in range(N):
        integral = integral + func(xrand[i])
    
    answer = (b-a)/float(N)*integral
    areas.append(answer)

plt.title("Distribution of Areas Calculated")
plt.hist(areas, bins = 30, ec = 'black')
plt.xlabel("Areas")

print(" The Answer of areas {}".format(areas))


# In[4]:


from scipy import random
import numpy as np
import math
import matplotlib.pyplot as plt


a = 0
b = np.pi
N = 1000

def func(x):
    return x**2 + 4*x *math.sin(x)

integral = 0.0

answer = (b - a) / float(N) * integral

areas = []

for i in range (N):
    xrand = np.zeros(N)
    
    for i in range(len(xrand)):
        xrand[i] = random.uniform(a,b)
        integral = 0.0
        
    for i in range(N):
        integral = integral + func(xrand[i])
    
    answer = (b-a)/float(N)*integral
    areas.append(answer)

plt.title("Distribution of Areas Calculated")
plt.hist(areas, bins = 30, ec = 'black')
plt.xlabel("Areas")

print(" The Answer of areas {}".format(areas))


# In[5]:


from scipy import random
import numpy as np
import math
import matplotlib.pyplot as plt


a = 0
b = np.pi
N = 1000

def func(x):
    return ((15*x**3+21*x**2 + 41*x + 3)**0.25)*(2.718**-0.5*x)

integral = 0.0

answer = (b - a) / float(N) * integral

areas = []

for i in range (N):
    xrand = np.zeros(N)
    
    for i in range(len(xrand)):
        xrand[i] = random.uniform(a,b)
        integral = 0.0
        
    for i in range(N):
        integral = integral + func(xrand[i])
    
    answer = (b-a)/float(N)*integral
    areas.append(answer)

plt.title("Distribution of Areas Calculated")
plt.hist(areas, bins = 30, ec = 'black')
plt.xlabel("Areas")

print(" The Answer of areas {}".format(areas))


# In[3]:


import math
import random


def function(x):
    return x**2

area_box = (4*25)
n = 10000
in_area = 0.0
out_area = 0.0

for jumlah in range(n):
    x_coord = random.uniform(1,5)
    y_coord = random.uniform(0,25)
    
    if y_coord < function(x_coord):
        in_area = in_area +1
    else:
        out_area = out_area + 1
    
  
area_under_graph = ((in_area)/(in_area + out_area)) * area_box

print("Total point di dalam area = {:.2f}".format(in_area))
print("Total point di atas area = {:.2f}".format(out_area))
print("Luas area di bawah grafik =  {:.2f}".format(area_under_graph))


# In[7]:


import math
import random


def function(x):
    return x**2 + 4*x *math.sin(x)

count = 0.0
in_area = 0.0
out_area = 0.0

while count < 10000:
    x_coord = random.uniform(2,3)
    y_coord = random.uniform(0,12.5)
    
    if y_coord < function(x_coord):
        in_area = in_area +1
    else:
        out_area = out_area + 1
    
    count = count + 1
    
area_box = (1*12.5)
    
area_under_graph = ((in_area)/(in_area + out_area))  * area_box

print("Total point di dalam area = {:.2f}".format(in_area))
print("Total point di atas area = {:.2f}".format(out_area))
print("Luas area di bawah grafik =  {:.2f}".format(area_under_graph))


# In[6]:


import math
import random


def function(x):
    return ((15*x**3+21*x**2 + 41*x + 3)**0.25)*(2.718**-0.5*x)

count = 0.0
in_area = 0.0
out_area = 0.0

while count < 100000:
    x_coord = random.uniform(0,4)
    y_coord = random.uniform(0,15)
    
    if y_coord < function(x_coord):
        in_area = in_area +1
    else:
        out_area = out_area + 1
    
    count = count + 1
    
area_box = (15*4)
    
area_under_graph = ((in_area)/(in_area + out_area))  * area_box

print("Total point di dalam area = {:.2f}".format(in_area))
print("Total point di atas area = {:.2f}".format(out_area))
print("Luas area di bawah grafik =  {:.2f}".format(area_under_graph))


# In[ ]:




