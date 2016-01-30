Morphological Operations on Binary Images
=======================================
Function usage notes are provided as comments on the source code. The images are considered binary between 0 and non­-0 pixel values in the mono­channel images obtained from the input images.
Algorithm Descriptions
----------------------
####Dilation:
+ Define the structural element (SE) as an array of size ​ n x n ​ , where ​ n ​ is provided by the user. Presently, all values of this array are set as 255 (=> square SE). 
+ Initiate the output image as a blank (zeros) image of same size as the input 
+ Iterate over all pixels of the input image 
+ At each nonzero pixel (=pixel of interest, or foreground), it is firstly checked if the ​ n x n neighboring pixels are all accessible (i.e., not outside the image’s size limits) 
+ If so, the output image array is sliced to extract the ​ n x n ​ window of pixels centered on the current pixel coordinates, and this slice is set equal to the SE 
+ If ​ n ​ is odd, there is no center pixel of the window, so the SE it is equated to is clipped by one row and one column (so that the dimensions of the window and SE match) 
+ If the user had provided the optional argument ​ noisefilter=1 , ​ the above three steps would only happen the pixel of interest is ascertained to not be a noise pixel + That is ascertained by scanning a small neighbor window around the pixel and counting the number of non­zero pixels. If this count is below a threshold, the current pixel is deemed as noise.
+ Finally, the output image is returned (and also saved in the working directory by default). 

####Erosion:
This function structurally follows the same algorithm as ​ Dilation , ​ but here the roles of background and foreground are inverted (since Erosion is the geometric dual of Dilation). Wherever 255 was used in ​ Dilation , ​ 0 is used in ​ Erosion (like the values in SE, criterion for pixel of interest).

####Opening:
​First apply ​ Erosion o ​ n the input image, then feed the eroded array to ​ Dilation. ​

####Closing:
First apply ​ Dilation o ​ n the input image, then feed the dilated array to ​ Erosion.

####Boundary:
​First apply ​ Erosion ​ on the input image, then subtract the eroded array from the input array

Results
---------

![res1](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Morphological%20Operations/Selection_013.png)
![res2](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Morphological%20Operations/Selection_014.png)
![res3](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Morphological%20Operations/Selection_015.png)

+ Since the SE’s chosen were quite small compared to the input image’s foreground, the ‘square­ness’ of the SE was not very apparent after any morphological operation ­ hence there was little incentive to go for more complicated shapes. 
+ Dilation produced best results with noise filtering enabled (since any noise would be magnified) and relatively larger SE sizes (6­8 for the given images), since they fill in the gaps smaller SE’s are not able to. 
+ However, ​ Erosion with similar SE sizes removed so many pixels that the image would lose characteristic features. Hence erosion was found to work best with SE of size 2. 
+ Opening performed well at limiting the output within the original bounds of the input while smoothing the contour and eliminating thin protrusions. Breaking of narrow isthmuses was most apparent (and potentially useful) on the ​ game.jpg i ​ mage. 
+ Closing gave best results (continuous filled region of interest) with relatively large SE sizes. It helped in smoothing the contour, fusing narrow breaks and long thin gulfs, filling in small holes. 
+ Boundary produced neat, continuous outer boundaries when used on closed images, but too fine internal boundaries on the original noisy images provided (could be useful, for instance to identify the finger boundaries on the ​ palm.bmp) ​