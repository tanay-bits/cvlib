Canny Edge Detector
=======================================

Algorithm Description
----------------------
+  The main script, *main.m* performs canny edge detection on one input image and shows the input image, Gaussian smoothed image, the two thresholded non-maxima suppressed images (high and low), and the final binary canny edge image.
+  First, the input image is **smoothed** using a Gaussian filter of appropriate sigma and window size in order to eliminate some of the noise from the input. This helps produce a more accurate edge image later on. For example: *S = GaussSmoothing(img_gray,7,1.4);*
+  The intensity **gradient** of the smoothed image is calculated by convolving it with a Sobel filter, resulting in the magnitude and direction of the edge map. Example: *[mags, thetas] = ImageGradient(S);*
+  The high and low thresholds (for use in the **double thresholding** algorithm later) are determined based on a user defined percentage of non-edge area in the edge magnitude map. For example: *[T_l, T_h] = FindThreshold(mags, 80);* How does it work? From the histogram of edge magnitudes, we find the magnitude below which lie 80% of the pixels in the mags image. That magnitude is the higher threshold *T_h*. The lower threshold *T_l* is simply *T_h/2*.
+  The magnitude map has thick edges, which are thinned to single pixel wide edges by finding the local maximum at each pixel, preserving it while ignoring all the non-maximum pixels. This **non-maxima suppression** is achieved by quantizing the possible angles from the direction edge map into 8 sections (45 deg apart),  iterating over all (non-boundary) pixels and comparing the gradient magnitude at each pixel with the two pixels from its 8-neighbor which lie along the section corresponding to the gradient direction. Example: *magsNMS = NonmaximaSuppress(mags, thetas);*
![sec](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Canny%20Edge%20Detector/sections.png)
+ *createThresholded.m* simply thresholds the non-maxima suppressed (NMS) image based on the higher and lower thresholds previously obtained (only needed if one wants to view these thresholded edge maps)
+ Finally, the canny edge map is obtained by **linking the edges** from the NMS image. This is done by iterating over all (non-boundary) pixels in the NMS image, checking if the current pixel is greater than the higher threshold (strong edge), and if it is, then recursively checking if any of its adjacent pixels (in the 8-neighbor) is a weak edge (greater than the lower threshold), until we reach an endpoint (lower than lower threshold). Note, all strong edge pixels are also weak edge, but not vice versa. This ensures we keep the true weak edges (which show up adjacent to strong edges), but discard false ones which might have come from noise.

Results
---------
####Input Image:
![sec](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Canny%20Edge%20Detector/lena.bmp)

####Result Compared with Other Edge Detectors:
![sec](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Canny%20Edge%20Detector/comparison.png)

####Some Intermediate Stages:
![sec](https://raw.githubusercontent.com/tanay-bits/cvlib/master/Canny%20Edge%20Detector/stages.png)

Our implementation of the canny detector produced better result than MATLAB’s sobel, roberts and zerocross edge detectors -  sobel and roberts captured very few edges, whereas zerocross’ output was noisy, had more false positive edges.

Comparing different percentages of non-edge area showed the following trend: the lower the percentage (like 50%), the more false positives, and the higher the percentage (like 90%), the more false negatives (sparse edge map). For lena.bmp, a good percentage was 70-80%. 

Higher sigma values (like 5) in the Gaussian smoothing step blurred the input too much and resulted in detection of only the strongest edges, while missing many more true but weaker edges. Very low sigma (like 0.4) hardly smoothed the input, causing a lot more edges (including false positives) to be detected. A good sigma was 1.4.