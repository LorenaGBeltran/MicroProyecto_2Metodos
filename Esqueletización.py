# -*- coding: utf-8 -*-I
"""
Created on Mon Mar  1 08:59:32 2021

@author: EMenendez
"""

from scipy.signal import convolve, convolve2d, correlate, correlate2d
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
#from tensorflow.keras.dataset import mnist
from scipy.ndimage import gaussian_filter
import  skimage.morphology as morf
from skimage.filters import threshold_local, threshold_mean, threshold_niblack,threshold_sauvola
from rdp import rdp 
from collections import Counter 



I = plt.imread('MinR.png')
Igray= I.mean(axis=2)
plt.figure()
plt.imshow(Igray,cmap="gray" )
plt.show()
#SmoothI= gaussian_filter(Igray, 0.1)
SmoothI=Igray
plt.figure()
plt.imshow(SmoothI,cmap="gray" )
plt.show()

TH = threshold_sauvola(SmoothI, window_size=13)
binaI= SmoothI> TH
binaI= morf.remove_small_objects(binaI, 2)

plt.figure()
plt.imshow(binaI,cmap="gray" )
plt.show()

skel= morf.skeletonize(~binaI)
#skel= morf.remove_small_objects(skel, 50, connectivity=2)

plt.figure()
plt.imshow(skel,cmap="gray" )
plt.savefig("MinRSkel.png", bbox_inches="tight")
plt.show()


X1= np.array([[-1,-1,-1],[-1,1,1],[-1,-1,-1]])
X2= np.array([[-1,-1,1],[-1,1,-1],[-1,-1,-1]])
X3= np.array([[-1,1,-1],[-1,1,-1],[-1,-1,-1]])
X4= np.array([[1,-1,-1],[-1,1,-1],[-1,-1,-1]])
X5= np.array([[-1,-1,-1],[1,1,-1],[-1,-1,-1]])
X6= np.array([[-1,-1,-1],[-1,1,-1],[1,-1,-1]])
X7= np.array([[-1,-1,-1],[-1,1,-1],[-1,1,-1]])
X8= np.array([[-1,-1,-1],[-1,1,-1],[-1,-1,1]])

F1= convolve(skel, X1)
F2= convolve(skel, X2)
F3= convolve(skel, X3)
F4= convolve(skel, X4)
F5= convolve(skel, X5)
F6= convolve(skel, X6)
F7= convolve(skel, X7)
F8= convolve(skel, X8)

filters = [F1, F2, F3, F4, F5, F6, F7, F8]
leaves=[]
for i in range(0, 8):
    pts= np.argwhere(filters[i]==2)
    if len(pts)>0:
        for j in range (0, pts.shape[0]):
            leaves.append(pts[j])
        
plt.figure(figsize=(12, 6))
for i in range (0,8):
    plt.subplot(2, 4, 1+i)
    plt.imshow(filters[i]==2,cmap="gray" )
    plt.xlabel("F"+str(i+1))
plt.show    
    
y1 = np.array([[-1,1,-1],[1,1,1],[-1,-1,-1]])
y2=  np.array([[-1,-1,1],[1,1,-1],[-1,1,-1]])
y3=  np.array([[-1,1,-1],[-1,1,1],[-1,1,-1]])
y4 = np.array([[-1,1,-1],[1,1,-1],[-1,-1,1]])
y5=  np.array([[-1,-1,-1],[1,1,1],[-1,1,-1]])
y6=  np.array([[-1,1,-1],[1,1,-1],[1,-1,-1]])
y7 = np.array([[-1,1,-1],[1,1,-1],[-1,1,-1]])
y8=  np.array([[1,-1,-1],[-1,1,1],[-1,1,-1]])
y9=  np.array([[1,-1,-1],[-1,1,1],[1,-1,-1]])
y10= np.array([[1,-1,1],[-1,1,-1],[-1,1,-1]])
y11= np.array([[-1,-1,1],[1,1,-1],[-1,-1,1]])
y12= np.array([[-1,1,-1],[-1,1,-1],[1,-1,1]])
y13= np.array([[1,-1,1],[-1,1,-1],[1,-1,-1]])
y14= np.array([[1,-1,1],[-1,1,-1],[-1,-1,1]])
y15= np.array([[-1,-1,1],[-1,1,-1],[1,-1,1]])
y16= np.array([[1,-1,-1],[-1,1,-1],[1,-1,1]])


b1= convolve(skel, y1)
b2= convolve(skel, y2)
b3= convolve(skel, y3)
b4= convolve(skel, y4)
b5= convolve(skel, y5)
b6= convolve(skel, y6)
b7= convolve(skel, y7)
b8= convolve(skel, y8)
b9= convolve(skel, y1)
b10= convolve(skel, y2)
b11= convolve(skel, y3)
b12= convolve(skel, y4)
b13= convolve(skel, y5)
b14= convolve(skel, y6)
b15= convolve(skel, y7)
b16= convolve(skel, y8)

filtersb = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16]

bif=[]

for i in range(0, 16):
    pts= np.argwhere(filtersb[i]==4)
    if len(pts)>0:
        for j in range (0, pts.shape[0]):
            bif.append(pts[j])
bif= np.array(bif)

plt.figure(figsize=(12, 12))
for i in range (0,16):
    plt.subplot(4, 4, 1+i)
    plt.imshow(filtersb[i]==4,cmap="gray" )
    plt.xlabel("B"+str(i+1).zfill(2))
plt.show    
    

z1 = np.array([[-1,1,-1],[1,1,1],[-1,1,-1]])
z2=  np.array([[1,-1,1],[-1,1,-1],[1,-1,1]])

t1= convolve(skel, z1)
t2= convolve(skel, z2)
filtert= [t1, t2]

trif=[]

for i in range(0, 2):
    pts= np.argwhere(filtert[i]==5)
    if len(pts)>0:
        for j in range (0, pts.shape[0]):
            trif.append(pts[j])

trif= np.array(trif)
plt.figure(figsize=(6, 6))
for i in range (0,2):
    plt.subplot(1, 2, 1+i)
    plt.imshow(filtert[i]==5,cmap="gray" )
    plt.xlabel("T"+str(i+1).zfill(2))
plt.show  

skel2= skel.copy()

for i in range (0, bif.shape[0]):
    x, y= bif[i]
    skel2[x-1:x+2, y-1: y+2]=0

for i in range (0, trif.shape[0]):
    x, y= trif[i]
    skel2[x-1:x+2, y-1: y+2]=0

plt.figure()
plt.imshow(skel2,cmap="gray" )
plt.show()

components= morf.label(skel2, connectivity=2)

plt.figure()
plt.imshow(components )
plt.show()

#esta en la cual cada entrada tendrá una lista
#de parejas ordenas que seran los componentes de la imagen 
superList=[]
for i in range(1, len(np.unique(components))):
    lista=[]
    for j in range (0, components.shape[0]):
        for k in range (0, components.shape[1]):
            if components[j,k]==i:
                lista.append([j,k])
    superList.append(lista)
superListrdp=[]
for i in range(0, len(superList)):
    if len(superList[i])<=2:
        superListrdp.append(superList[i])
    if len(superList[i])>2: 
        x= superList[i]
        arr1=rdp(x, epsilon=0.6)
        superListrdp.append(arr1)
        

