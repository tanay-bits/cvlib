function [ S ] = GaussSmoothing( I, N, sigma )
%Using a Gaussian filter to smooth a given gray scale image

Gmask = fspecial('gaussian',[N,N], sigma);
K = conv2(I, Gmask, 'same');
S = mat2gray(K);

end

