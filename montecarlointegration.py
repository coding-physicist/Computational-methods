import math as mt
import random as rnd
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy

x1=float(input("Enter lower limit: "))
x2=float(input("Enter upper limit: "))
xx=np.arange(x1,x2,abs((x2-x1)/1000))
trial=int(input("Enter desired number of trials: "))
xdiff=(x2-x1)
arrxa=[]
arrya=[]
arrx=[]
arry=[]
def fnctn(x):
    y=mt.sin(1/(x*(2-x)))**2
    return y
def arrfn(x):
     y=-np.sin(1/(x*(2-x)))**2
     return y
y1=np.min(arrfn(xx))
y2=np.max(arrfn(xx))
ydiff=abs(y1-y2)
area=abs(xdiff*ydiff)
count=0
for i in range (0,trial):
    xa=x1+(xdiff*rnd.random())
    ya=y1+(ydiff*rnd.random())
    if (ya<=fnctn(xa)):
        count+=1
        arrxa.append(xa)
        arrya.append(ya)
    else:
        arrx.append(xa)
        arry.append(ya)
integral=area*count/trial
print('integral=',integral)
plt.scatter(arrx,arry,color='red',s=8)
plt.scatter(arrxa,arrya,color='yellow',s=8)
plt.show()