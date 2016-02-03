function [ hist_norm ] = build_hist( im )
%Return normalized 2D histogram of input image im

%% LOAD TRAINING IMAGE, EXTRACT ROI AND ITS COLORSPACES
% select ROI:
im_roi = imcrop(im);
[nrows ncols] = size(im_roi(:,:,1));

% extract R, G from cropped training image:
im_roi_r = im_roi(:,:,1);
im_roi_g = im_roi(:,:,2);

% extract H, S from cropped training image:
im_roi_hsv = rgb2hsv(im_roi);
im_roi_h = im_roi_hsv(:,:,1);
im_roi_s = im_roi_hsv(:,:,2);

% extract N-R, N-G from cropped training image:
im_roi_b = im_roi(:,:,3);
im_roi_nr = im_roi_r./(im_roi_r+im_roi_g+im_roi_b);
im_roi_ng = im_roi_g./(im_roi_r+im_roi_g+im_roi_b);

%% CREATE 2D NORMALIZED HISTOGRAM (currently in H-S space)

% R-G histogram:
% Hrg = zeros(256,256);
% for i = 1:nrows
%     for j = 1:ncols
%         r = im_roi_r(i,j);
%         g = im_roi_g(i,j);
%        
%         Hrg(r,g) = Hrg(r,g)+1;
%     end
% end
% Hrg_norm = Hrg./sum(Hrg(:));

% H-S histogram:
Hhs = zeros(1000,1000);
for i = 1:nrows
    for j = 1:ncols
        h = im_roi_h(i,j);
        s = im_roi_s(i,j);
       
        Hhs(round(h*1000)+1, round(s*1000)+1) = Hhs(round(h*1000)+1, round(s*1000)+1)+1;
    end
end
Hhs_norm = Hhs./sum(Hhs(:));

% NR-NG histogram:
% Hnrng = zeros(1000,1000);
% for i = 1:nrows
%     for j = 1:ncols
%         nr = round(im_roi_nr(i,j)*1000);
%         ng = round(im_roi_ng(i,j)*1000);
%             
%         Hnrng(round(nr*1000)+1, round(ng*1000)+1) = Hnrng(round(nr*1000)+1, round(ng*1000)+1)+1;
%     end
% end
% Hnrng_norm = Hnrng./sum(Hnrng(:));

%% RETURN OUTPUT
hist_norm = Hhs_norm;
end



