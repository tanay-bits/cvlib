clear all;
%% TRAINING

hist_bag = [];

im1 = imread('gun1.bmp');
hist1 = build_hist(im1);
hist_bag = cat(3, hist_bag, hist1);

im2 = imread('joy1.bmp');
hist2 = build_hist(im2);
hist_bag = cat(3, hist_bag, hist2);

im3 = imread('pointer1.bmp');
hist3 = build_hist(im3);
hist_bag = cat(3, hist_bag, hist3);

im4 = imread('4.jpg');
hist4 = build_hist(im4);
hist_bag = cat(3, hist_bag, hist4);

im5 = imread('5.jpg');
hist5 = build_hist(im5);
hist_bag = cat(3, hist_bag, hist5);

im6 = imread('6.jpg');
hist6 = build_hist(im6);
hist_bag = cat(3, hist_bag, hist6);

im7 = imread('7.png');
hist7 = build_hist(im7);
hist_bag = cat(3, hist_bag, hist7);

im8 = imread('8.jpg');
hist8 = build_hist(im8);
hist_bag = cat(3, hist_bag, hist8);

im9 = imread('9.jpeg');
hist9 = build_hist(im9);
hist_bag = cat(3, hist_bag, hist9);

im10 = imread('10.jpg');
hist10 = build_hist(im10);
hist_bag = cat(3, hist_bag, hist10);

im11 = imread('11.jpg');
hist11 = build_hist(im11);
hist_bag = cat(3, hist_bag, hist11);

im12 = imread('12.jpg');
hist12 = build_hist(im12);
hist_bag = cat(3, hist_bag, hist12);

im13 = imread('13.jpg');
hist13 = build_hist(im13);
hist_bag = cat(3, hist_bag, hist13);

im14 = imread('14.jpg');
hist14 = build_hist(im14);
hist_bag = cat(3, hist_bag, hist14);

im15 = imread('15.jpg');
hist15 = build_hist(im15);
hist_bag = cat(3, hist_bag, hist15);

% Average of all normalized histograms:
hist_avg = mean(hist_bag, 3);

%% TESTING

imtest = imread('21.jpg');

imtest_skin = segmentskin(imtest, hist_avg);
