Histogram-based Skin Color Detection
============

Main script
-----------------------------------------------------
+ The main script, *main.m* consists of two sections - training and testing
First, an empty 3D array (*hist_bag*) to store all the normalized training 2D histograms is initialized
+ Training images are read one by one, and the region of interest is cropped for each one by the user
+ For each training image, the 2D H-S histogram of the cropped part is calculated by the function *build_hist(training_image)*
+ Each such histogram is stored as an entry along the 3rd dimension of hist_bag 
+ After all the training images have been loaded, the mean of the normalized histograms in *hist_bag* is computed and stored as *hist_avg*
+ Now the test image is read and the skin color segmented image is obtained by the function *segmentskin(testing_image, hist_avg)* and stored in the variable *imtest_skin*.

Training image histogram generator function
--------------------------------------------------
+ *build\_hist(input_image)* returns the normalized 2D (H-S) histogram of input image
+ First it loads the input image, and allows the user to crop a region of interest (skin pixels)
+ The relevant color space channels to create the 2D histogram are extracted from the cropped image
+ The histogram is built by filling a 1000 x 1000 bin matrix with number of occurrences of each H-S pair by iterating over the pixels of the cropped image
+ Finally the 2D histogram is normalized by dividing its each element by the sum of the all elements

Segmented image generator function
--------------------------------------------------
+ *segmentskin(testing_image, hist_avg)* returns the test image segmented for skin color, i.e., all non-skin pixels are black
+ It first extracts the H and S channels of the test image
+ It sets the histogram threshold (presently it is set arbitrarily, but can also be determined by running the script *myKmeans.m*)
+ Iterating over all the pixels of the test image, each pixel’s H and S value is determined and used to index the *hist_avg* 2D histogram
+ If the value of hist_avg at that index is below the threshold, the corresponding pixel in the output image is set to 0 

Results and Comments
-------------------------------
![altxt](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Skin%20Color%20Segmentation/hist_avg_15.jpg)
![altxt](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Skin%20Color%20Segmentation/hist_1.jpg)

+ After trying R-G, H-S, and nR-nG histograms, the HSV color-space was chosen since it seemed to produce generally better results. 
+ Increasing the number of training images from 1 to 15 definitely improved the segmentation of test images, but 15 is still a low number to achieve impressive segmentation. If the output image is converted to binary and a morphological operation like dilation or closing is applied to it, the result can be used as a mask on the original input color image to segment out the skin regions in a cleaner fashion. 
+ For test images which have colors similar to the skin color in background (like ‘16.jpg’), much of the background is also segmented along with the human. This is one of the flaws of color-based image segmentation.
+ Although I could use the script myKmeans.m (which is my k=2 implementation of the k-means clustering algorithm), on multiple trials with it I realized the thresholds it suggested were quite similar to what I would set upon looking at the 2D histogram plot, and so both methods gave similar results. Since the latter is more practical and convenient (at least in this case) than the time and computation-expensive k-means clustering, I decided to go with that option.