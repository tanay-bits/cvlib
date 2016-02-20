close all
clear all

img = imread('lena.bmp');
I = rgb2gray(img);
S = GaussSmoothing(I,15,2);
[mags, thetas] = ImageGradient(S);
[T_l, T_h] = FindThreshold(mags, 60);
magsNMS = NonmaximaSuppress(mags, thetas);
[mags_high, mags_low] = createThresholded(magsNMS, T_h, T_l); %optional
img_canny = EdgeLinking(magsNMS, T_h, T_l);

figure,
subplot(3,2,1), imshow(img); title('Original Image');
subplot(3,2,2), imshow(S); title('Gaussian Smoothed');
subplot(3,2,3), imshow(mags_high); title('High Thresholded NMS');
subplot(3,2,4), imshow(mags_low); title('Low Thresholded NMS');
subplot(3,2,5:6), imshow(img_canny); title('Canny Edges');

% Display the raw (non-thresholded) NMS image:
%imshow(magsNMS);