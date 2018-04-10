# -*- coding: utf-8 -*-
"""
Edited on Mon Apr  9 21:33:19 2018

@author: Bob
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 16:48:36 2017
@author: haowen
"""
import numpy as np
import matplotlib.pyplot as plt
w_plot = np.array([[0,0],[0,0],[0,0]], np.float)
plt.xlim(-2,2)
plt.ylim(-2,2)

def getDataSet(filename):
    dataSet = open(filename, 'r')
    dataSet = dataSet.readlines()
    num = len(dataSet)
    X = np.zeros((num,2))
    Y = np.zeros((num,1))
    for i in range(num):
        data = dataSet[i].strip().split()
        X[i,0] = np.float(data[0])
        X[i,1] = np.float(data[1])
        Y[i,0] = np.float(data[2])
        
        # Color would be defined by its Label
        if Y[i,0] == 1 :
            color = 'blue'
        else:
            color = 'red'
        plt.scatter(X[i,0], X[i,1],c=color)
        
    return X,Y

def sign(x,w):
    if np.dot(x,w) >= 0:
        return 1
    else:
        return -1
        
def PLA_Naive(X, Y, w, speed, updates):
    iterations = 0
    num = len(X)
    flag = True
    for i in range(updates):
        flag = True
        for j in range(num):            
            if sign(X[j],w) != Y[j,0]:
                flag = False                     
                w = w + speed*Y[j,0]*np.matrix(X[j]).T
                #plot the line after adjusted            
                w_plot.itemset((0,0),2)
                w_plot.itemset((0,1),(-1)*2*w[0]/w[1])
                w_plot.itemset((1,0),0)
                w_plot.itemset((1,1),0)
                w_plot.itemset((2,0),(-2))
                w_plot.itemset((2,1),(-1)*(-2)*w[0]/w[1])
                plt.plot(w_plot[:,0],w_plot[:,1],marker='x')
                
                break
            else:
                continue
        if flag == True:
            iterations = i
            break
    return w, flag, iterations
    
filename = r"C:\PyWorkPlace\Machine-Learning-Foundations-and-Techniques-master\dataset" + "\hw1_bob.dat"
X, Y = getDataSet(filename)
plt.show()

w0 = np.zeros((2,1)) 
speed = 1
updates = 80

w, flag, iterations = PLA_Naive(X, Y, w0, speed, updates)

print (flag)
print (iterations)
print (w)
