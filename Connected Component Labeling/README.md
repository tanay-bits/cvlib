Connected Component Labeling of Binary Images
=======================================
The images are considered binary between 0 and non-­0 pixel values in the mono­channel images obtained from the given images. When the user runs 
`lab_img, num_labels = CCL(‘filename.bmp’)` 
a color-­labeled image of the input file is saved in memory and the labeled image matrix and total number of labels returned and stored to their respective variables. 

+ Connected Component Labeling is performed by considering the 4-­neighbors of each pixel while scanning from left to right, top to bottom of the image.
+  At each nonzero pixel (=pixel of interest), the algorithm ascertains the label of one pixel above and one pixel to the left. 
+  If both neighbor labels are 0, the label count is incremented and its value added to a dictionary of labels (where initially each key­value pair is a distinct pair of identical labels). The label is also associated with the current pixel (in the ​ lab_img ​ array). 
+ If both neighbor labels are same and nonzero, associate either with the current pixel (upper label in my implementation). 
+ If one of the neighbor labels is nonzero and the other zero, associate the current pixel with the maximum of the two (=nonzero label). 
+ If both are nonzero and not the same, assign the lower-­value label to the current pixel. Also change the value pointed to by the higher key in the dictionary of labels (E\_table) to the lower-­value label. And if the key corresponding to that lower value label does not point to itself, change the value pointed to by the higher key in E_table again to the value pointed to by the lower value key. 
+ After 1st pass through all the pixels, go through them again, but only check the labelled regions and update the labels associated with the pixels to the ones corresponding to the new modified E_table. 
+ Now all the connected components are labelled properly

Note: ​ The extra label in the first two images might have appeared because of using the 4­-neighbor algorithm instead of the 8­-neighbor one. 

Results
---------
Color-labeled outputs:

![results](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Connected%20Component%20Labeling/cclresults.png)
