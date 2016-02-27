Hough Transform
==============

Algorithm Description
----------------------
+  The function Hough() returns Hough lines overlaid on the input image. It also writes to disk the Hough lines as well as parameter space image, indicating significant intersections in the parameter space as bright points.
+  First the input image is loaded as a grayscale, and its Canny edge map is obtained.
+  The accumulator is initialized with all values 0 and dimensions according to the quantization arguments. d_theta=1 implies 1 vertical bin = 1 deg, d_theta=0.5 implies 1 vertical bin = 0.5 deg. Similarly d_rho=1 implies 1 horizontal bin is 1 pixel wide
+  Iterating over all edge pixels, and for each such pixel iterating over the range of discrete angles 0 to 180 deg (in steps determined by d_theta), rho values are calculated according to rho=x.cos(theta)+y.sin(theta), where x and y are horizontal and vertical distance from center of image, and rho and theta are the polar coordinates. The corresponding bin (theta, rho) in the accumulator is then incremented by 1.
+  The accumulator is now complete. It is normalized by dividing each element by the total sum of votes so that all values are between 0 and 1. This allows the algorithm to work with different sized images using similar range of thresholds.
+ Significant intersections in the parameter space are found by extracting those bins from the accumulator which have higher votes than the threshold provided as an argument.
+ Iterating over the input image pixels again, we map back from parameter space to image space. This is done by checking if the above equation holds (within a small rounding off tolerance) at the current pixel, with any rho-theta pair from the list of significant intersections. If it does hold, that pixel belongs to the line modeled by rho-theta and is set to 255.
+ Finally, we save to disk the Hough lines image (obtained after the previous step) as well as parameter space image with theta’s represented by rows and rho’s represented by columns of the image. The significant intersections (one per line detected) are indicated by the bright points in this (rather cool looking) image.

Results
---------

![sec](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Hough%20Transform/result_input.png)

![sec](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Hough%20Transform/result_tests.png)

*Hough lines overlaid on input images and their parameter space maps. The bright points (significant intersections) in the parameter space correspond to lines detected.*

The above results were obtained using *d_theta* and *d_rho* equal to 1, and *thresh* = (0.0003 for test.bmp and test1.bmp, 0.00025 for input.bmp). Increasing quantizations (e.g. to 2, 2) resulted in a lot of false positive lines, since the accumulator grid was coarse which means more bins had high votes. In such a case, the threshold needs to be increased to obtain good results.

![sec](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Hough%20Transform/Comparisons/t2_test.bmp)

On the other hand, if quantization is decreased (e.g. to 0.5, 0.5), fewer lines are detected since the accumulator is too fine. Reducing the threshold helps in this case.

![sec](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Hough%20Transform/Comparisons/hough_test_p0_5_t_3.bmp)