function [ segmented_img ] = segmentskin( imtest, hist_avg )
% Return segmented image for skin color

imtest_hsv = rgb2hsv(imtest);
% imtest_seg_rg = imtest;
imtest_seg_hs = imtest;

[nrows ncols] = size(imtest(:,:,1));

imtest_h = imtest_hsv(:,:,1);
imtest_s = imtest_hsv(:,:,2);

thresh_hs = 0.0001;      %could also be determined from myKmeans.m
for i = 1:nrows
    for j = 1:ncols
        h = imtest_h(i,j);
        s = imtest_s(i,j);
        
        if (round(h*1000)+1 <= 1000) && (round(s*1000)+1 <= 1000)
            if hist_avg(round(h*1000)+1, round(s*1000)+1) < thresh_hs
                imtest_seg_hs(i,j,:) = 0;
            end
%         else
%             imtest_seg_hs(i,j,:) = 0;
        end
    end
end

segmented_img = imtest_seg_hs;

end

