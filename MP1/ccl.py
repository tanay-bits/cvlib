import numpy as np 
import cv2
from matplotlib import pyplot as plt

def CCL(filename):
    img_gray = cv2.imread(filename, 0)
    img_rgb = cv2.imread(filename)
    
    E_table = {}                         # initialize an empty dict to hold the equivalence table

    lab_img = np.zeros(img_gray.shape)   # initialize the labeled image as zeros
    rlim = img_gray.shape[0]             # row dimension
    clim = img_gray.shape[1]             # column dimension
    Lcount = 0                           # initialize counter for labels

    # Scan through all pixels sequentially:
    for r in xrange(rlim):
        for c in xrange(clim):
            if img_gray[r,c] > 0:                          # if pixel of interest
                L_u = lab_img[r-1, c]                      # label of the upper pixel
                L_l = lab_img[r, c-1]                      # label of the left pixel
                
                if (L_u==L_l) and (L_u!=0):                # if both labels same and non-zero
                    lab_img[r,c] = L_u                     # assign either label
                elif (L_u!=L_l) and (L_u==0 or L_l==0):    # if one of the labels is zero
                    lab_img[r,c] = max(L_u, L_l)           # assign the higher-value label
                elif (L_u!=L_l) and (L_u>0 and L_l>0):     # if both labels are non-zero
                    lab_img[r,c] = min(L_u, L_l)           # assign the lower-value label
                    E_table[max(L_u, L_l)] = min(L_u, L_l) # change the value pointed to by the higher key
                    if E_table[min(L_u, L_l)] != min(L_u, L_l):
                        E_table[max(L_u, L_l)] = E_table[min(L_u, L_l)] # old higher label (key) now pointing to lower label (value)
                else:                                      # if both labels are zero
                    Lcount += 1
                    E_table[Lcount] = Lcount               # add a new key with same value to the E_table
                    lab_img[r,c] = Lcount                  # add a new label

    # Scan through all pixels again to readjust labels:
    for r in xrange(rlim):
        for c in xrange(clim):
            if lab_img[r,c] != 0:     # only check labelled regions
                lab_img[r,c] = E_table[lab_img[r,c]] # old higher label now ACTUALLY changed to base label
            
            img_rgb[r,c,:] = lab_img[r,c]  # populate the 3-channel image

    # # Size filter:
    # min_size = 200
    # count = 0
    # for r in xrange(rlim):
    #     for c in xrange(clim):
    #         if lab_img[r, c] != 0:
    #             current_label = lab_img[r, c]
    #             count += 1
    #             if count>200:
                    



    # To color the labels distinctly:
    img_rgb[:,:,0] = img_rgb[:,:,0]*50
    img_rgb[:,:,1] = img_rgb[:,:,1]*100 
    img_rgb[:,:,2] = img_rgb[:,:,2]*150 

    # Calculate number of distinct labels:
    num_labels = len(np.unique(lab_img)) - 1

    # Save the labeled (colored) image:
    cv2.imwrite('rgb_image.png', img_rgb)

    # Return the labeled image matrix and number of labels:
    return lab_img, num_labels






