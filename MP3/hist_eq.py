import numpy as np 
import cv2

def HistoEqualization(img_in):
    '''
    Returns histogram-equalized version of input image img_in. Example:
    adjusted_img = HistoEqualization('imgname.bmp')
    '''
    img = cv2.imread(img_in, 0)
    rows = img.shape[0]  #no. of rows in input image
    cols = img.shape[1]  #no. of columns in input image
    img_eq = np.array([[0]*cols]*rows)  #initialize array to store result
    histarray, binarray = np.histogram(img, bins=np.arange(257), density=True)  #normalized histogram
    cdf = np.cumsum(histarray)  #cumulative distribution function
    for r in xrange(rows):
        for c in xrange(cols):
            img_eq[r][c] = int(255*cdf[img[r][c]])  #cdf(im[r][c]) is cdf at the INTENSITY LEVEL of the pixel

    #store and return output:
    cv2.imwrite('histeq_'+img_in, img_eq)
    
    return img_eq


#MAIN SCRIPT:
equalized_img = HistoEqualization('moon.bmp')

