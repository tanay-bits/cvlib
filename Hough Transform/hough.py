import numpy as np
from math import sin, cos, pi, hypot, radians
import cv2

def Hough(img_in, d_theta=1, d_rho=1, thresh=0.0003):
    '''
    Returns Hough lines overlaid on input image. Also writes to disk the Hough lines
    as well as parameter space image.
    
    img_in -> input image file name as string
    d_theta -> quantization resolution of parameter theta;
               1 implies 1 bin = 1 deg, 0.5 implies 1 bin = 0.5 deg
    d_rho -> quantization resolution of parameter rho;
             1 implies 1 bin is 1 pixel wide
    thresh -> threshold for normalized votes in the accumulator
    
    Example:
    h = Hough('input.bmp',1,1,thresh=0.000255)
    '''
    # Initialization and preprocessing:
    img = cv2.imread(img_in, 0)
    rows = img.shape[0]  #no. of rows in input image
    cols = img.shape[1]  #no. of columns in input image
    img_canny = cv2.Canny(img,100,200,L2gradient=True)
    ctr_x = cols/2
    ctr_y = rows/2
    accum_w = int(hypot(rows,cols)/d_rho)
    accum_h = int(180./d_rho)
    accum = np.array([[0]*accum_w]*accum_h) #accumulator initialized as zeros 

    # Filling the accumulator with votes:
    for r in xrange(rows):
        for c in xrange(cols):
            if img_canny[r][c]>0:
                for bin_theta in xrange(accum_h):
                    theta = radians(bin_theta*d_theta)
                    rho = (c-ctr_x)*cos(theta) + (r-ctr_y)*sin(theta)
                    bin_rho = accum_w/2 + int(rho/d_rho)
                    accum[bin_theta][bin_rho] += 1
    accum_viz = accum*3         #enhanced for visualization
    accum = np.true_divide(accum, accum.sum())

    # Finding significant intersections in the parameter space:
    accum_ind = np.argwhere(accum>thresh)
    assert accum_ind.size > 0, "thresh too high, try lower value"
    accum_prev = accum_ind[0]
    accum_new = [accum_prev]
    for i in xrange(1, accum_ind.shape[0]): #this loop removes redundant intersection
                                            #points
        diff = abs(accum_ind[i] - accum_prev)
        if np.any(diff>5):
            accum_new.append(accum_ind[i])
        accum_prev = accum_ind[i]
    accum_new = np.asarray(accum_new)

    # Mapping back from parameter space to image space, and overlaying detected lines:
    for r in xrange(rows):
        for c in xrange(cols):
            for m,n in accum_new:
                # if ((c-ctr_x)*cos(radians(m*d_theta)) + (r-ctr_y)*sin(radians(m*d_theta)) - 1) <= ((n-accum_w/2)*d_rho) <= ((c-ctr_x)*cos(radians(m*d_theta)) + (r-ctr_y)*sin(radians(m*d_theta)) + 1):
                if round((n-accum_w/2)*d_rho) == round((c-ctr_x)*cos(radians(m*d_theta)) + (r-ctr_y)*sin(radians(m*d_theta))):
                    img[r][c] = 255
    
    cv2.imwrite('hough_'+img_in, img)
    cv2.imwrite('param_'+img_in, accum_viz)

    return img



