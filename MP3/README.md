Histogram Equalization and Lighting Correction
===============================================

Algorithm Descriptions
----------------------

*Histogram Equalization:*

+  Input image is read as a grayscale 2D array and its dimensions are determined
+  An empty array of the same size as input is initialized
+  Taking the cumulative sum at each element of the normalized histogram array, the cumulative distribution function (cdf) is calculated
+  A nested for loop is run to iterate over every pixel of the image, and the value at each pixel of the output is calculated as 255 times the cdf (which is b/w 0 and 1) at the corresponding input image pixel
+  The output image is saved as a file and returned


*Lighting Correction:*
Reference - [Tutorial: Illumination Correction](https://clouard.users.greyc.fr/Pantheon/experiments/illumination-correction/index-en.html#retrospective "Reference")

+  First two steps same as the above algorithm
+  The background is estimated using regression
+  For **linear** fitting method, the input features are row r, column c of input image (y_fit = b+w1*r+w2*c); for **quadratic** method, the input features are r, c, r<sup>2</sup>, c<sup>2</sup>, r*c (since y_fit = b+w1*r+w2*c+w3*r<sup>2</sup>+w4*c<sup>2</sup>+w5*r*c), where y is the intensity level (0-255)
+  Setting the gradient of the least squares cost function to 0, and solving the Ax=B type linear regression equation using pseudo-inverse (inverse also worked in the test image), we arrive at the optimal set of coefficients *w*
+  Now the output image *out* is filled with y_fit values; this is the estimated background - the plane-fit (linear) or 2<sup>nd</sup>-order surface-fit (quadratic) image
+  Additionally an image *out_mean_img* is created in which all pixels have the mean value of the out (background) image
+  Finally, the lighting corrected image = input image - estimated background + mean(estimated background)
+  The lighting corrected image is saved as a file and returned


Results Analysis
----------------
Because of histogram equalization, the contrast of the input image is greatly enhanced, making the important features of the image visible. Whereas the entire input image had more or less the same intensity, the output has intensities spread out from very dark to very bright.

Both linear and quadratic lighting correction improved the histogram equalized image by transforming the uneven background lighting to more uniform lighting. Linear method corrected the dark lower left region of the input image, and quadratic method (providing a more accurate fit) went a step ahead and also corrected for the dark middle region in the image.