import numpy as np 
import cv2

img = cv2.imread('histeq_moon.bmp', 0)
rows = img.shape[0]  #no. of rows in input image
cols = img.shape[1]  #no. of columns in input image
out = np.array([[0]*cols]*rows)  #initialize array to store LR image

#REGRESSION FOR LINEAR FIT:
x = []
y = []
for r in xrange(rows):
        for c in xrange(cols):
            x.append([1, r, c])
            y.append(img[r][c])

X = np.asarray(x)
X = X.T
y = np.asarray(y)
y.shape = (np.size(y), 1)

A = X.dot(X.T)
B = X.dot(y)

w = (np.linalg.pinv(A)).dot(B)

ynew = (X.T).dot(w)

#CREATE PLANE-FIT IMAGE:
ind = 0  #y index counter
for r in xrange(rows):
    for c in xrange(cols):
        out[r][c] = ynew[ind][0]
        ind += 1

#CREATE MEAN OF PLANE-FIT IMAGE:
out_mean = np.mean(out)
out_mean_img = np.array([[out_mean]*cols]*rows)

#CREATE LIGHTING CORRECTED IMAGE:
lc_img = (img - out) + out_mean_img

cv2.imwrite('lc_lin_histeq_moon.bmp', lc_img)
