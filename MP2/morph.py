import numpy as np 
import cv2

def Dilation(img, n, write=1, fullname=1, noisefilter=0):
    '''
    Dilate input image (img) with an n-by-n square structural element. 
    By default, the img is specified as 'imgfilename.format', and the output image is saved to the working 
    directory. Optional arguments:
    write=0 => Do not save output
    fullname=0 => Specify input as an array variable instead of full filename
    noisefilter=1 => Enable noise filtering 
    '''
    
    assert n != 1, 'Size of structural element cannot be 1 pixel'

    if fullname==1:
        img_gray = cv2.imread(img, 0)  # read input img as grayscale
    else:
        img_gray = img  # or, ensure input img is a 2-D array
    
    se = np.array([[255]*n]*n)  # define the structural element as a square
    rmax = img_gray.shape[0]  # lowest row index + 1
    cmax = img_gray.shape[1]  # right-most column index + 1
    img_out = np.zeros(img_gray.shape)  # output img initialized as blank
    
    # Iterate over all pixels of input image and perform the morphological operation:
    for r in range(rmax):
        for c in range(cmax):
            if img_gray[r,c]==255:  # if the pixel belongs to the foreground
                if (r-3>0 and r+3<rmax and c-3>0 and c+3<cmax and noisefilter==1):  # check for img size limits
                    count = 0  # counter for number of foreground pixels in neighborhood; for noise filtering
                    for ir in range(r-3, r+3):
                        for ic in range(c-3, c+3):
                            if img_gray[ir, ic]==255:
                                count += 1

                if noisefilter==1:  # perform dilation only if count > 10
                    if (r-(n/2)>0 and r+(n/2)<rmax and c-(n/2)>0 and c+(n/2)<cmax and noisefilter==1 and count>10):
                        if n%2==0:
                            img_out[r-(n/2) : r+(n/2), c-(n/2) : c+(n/2)] = se
                        else:  # if n is odd, the SE needs to be clipped by 1 row and column in order to match
                            img_out[r-(n/2) : r+(n/2), c-(n/2) : c+(n/2)] = se[0:n-1, 0:n-1]

                else:  # do not consider count
                    if (r-(n/2)>0 and r+(n/2)<rmax and c-(n/2)>0 and c+(n/2)<cmax):
                        if n%2==0:
                            img_out[r-(n/2) : r+(n/2), c-(n/2) : c+(n/2)] = se
                        else:
                            img_out[r-(n/2) : r+(n/2), c-(n/2) : c+(n/2)] = se[0:n-1, 0:n-1]


    if write==1 and fullname==1:
        cv2.imwrite('dil_'+img, img_out) # save the dilated image
    
    return img_out


def Erosion(img, n, write=1, fullname=1):
    '''
    Erode input image (img) with an n-by-n square structural element. 
    By default, the img is specified as 'imgfilename.format', and the output image is saved to the working 
    directory. Optional arguments:
    write=0 => Do not save output
    fullname=0 => Specify input as an array variable instead of full filename
    '''
    # This function structurally follows the same algorithm as Dilation, but here the roles of background and 
    # foreground are inverted (since Erosion is the geometric dual of Dilation).  
 
    assert n != 1, 'Size of structural element cannot be 1 pixel'

    if fullname==1:
        img_gray = cv2.imread(img, 0)  # read input img as grayscale
    else:
        img_gray = img  # or, ensure input img is a 2-D array

    se = np.zeros((n,n))  # define the structural element as a square
    rmax = img_gray.shape[0]  # lowest row index + 1
    cmax = img_gray.shape[1]  # right-most column index + 1
    img_out = np.ones(img_gray.shape)*255  # output img initialized as completely white
    
    # Iterate over all pixels of input img and perform the morphological operation:
    for r in range(rmax):
        for c in range(cmax):
            if r==0 or r==rmax-1 or c==0 or c==cmax-1:  # if pixel is at frame boundary, make it 0
                img_out[r,c] = 0                        # otherwise we get a white-framed output
            if img_gray[r,c]==0:  # if pixel belongs to background
                if (r-(n/2)>0 and r+(n/2)<rmax and c-(n/2)>0 and c+(n/2)<cmax):  # check for img size limits
                    if n%2==0:
                        img_out[r-(n/2) : r+(n/2), c-(n/2) : c+(n/2)] = se
                    else:  # if n is odd, the SE needs to be clipped by 1 row and column in order to match
                        img_out[r-(n/2) : r+(n/2), c-(n/2) : c+(n/2)] = se[0:n-1, 0:n-1]

    if write==1 and fullname==1:
        cv2.imwrite('ero_'+img, img_out)  # save the eroded image
    
    return img_out


def Opening(img, n, write=1, fullname=1):
    '''
    Open (erode, then dilate) the input image (img) with an n-by-n square structural element. 
    By default, the img is specified as 'imgfilename.format', and the output image is saved to the working 
    directory. Optional arguments:
    write=0 => Do not save output
    fullname=0 => Specify input as an array variable instead of full filename
    '''

    ero_img = Erosion(img, n, write=0, fullname=1)  # img -> full filename
    img_final = Dilation(ero_img, n, write=0, fullname=0)  # ero_img NOT the full filename, just an ndarray

    if write==1 and fullname==1:
        cv2.imwrite('opened_'+img, img_final)  # save the opened image
    
    return img_final


def Closing(img, n, write=1, fullname=1, noisefilter=0):
    '''
    Close (dilate, then erode) the input image (img) with an n-by-n square structural element. 
    By default, the img is specified as 'imgfilename.format', and the output image is saved to the working 
    directory. Optional arguments:
    write=0 => Do not save output
    fullname=0 => Specify input as an array variable instead of full filename
    noisefilter=1 => Enable noise filtering
    '''

    if noisefilter==1:
        dil_img = Dilation(img, n, write=0, fullname=1, noisefilter=1)  # img -> full filename
    else:
        dil_img = Dilation(img, n, write=0, fullname=1)

    img_final = Erosion(dil_img, n, write=0, fullname=0)  # dil_img NOT the full filename, just an ndarray

    if write==1 and fullname==1:
        cv2.imwrite('closed_'+img, img_final)  # save the opened image
    
    return img_final


def Boundary(img, n, write=1, fullname=1):
    '''
    Obtain the boundary of the input image (img) with an n-by-n square structural element. Greater the n,
    thicker the boundary. 
    By default, the img is specified as 'imgfilename.format', and the output image is saved to the working 
    directory. Optional arguments:
    write=0 => Do not save output
    fullname=0 => Specify input as an array variable instead of full filename
    noisefilter=1 => Enable noise filtering
    '''
    # Boundary of foreground is obtained by subtracting the eroded img from the original img.

    orig_img = cv2.imread(img, 0)  # img -> full filename
    ero_img = Erosion(orig_img, n, write=0, fullname=0)  # orig_img -> NOT the full filename
    bound_img = orig_img - ero_img  

    if write==1 and fullname==1:
        cv2.imwrite('bound_'+img, bound_img)  # save the boundary image
    
    return bound_img
