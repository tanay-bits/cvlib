function [ Mag, Theta ] = ImageGradient( S )
%Return the magnitude and direction of the edge map of S

Gy = fspecial('sobel');
Gx = Gy';
Ey = conv2(S, Gy, 'same');
Ex = conv2(S, Gx, 'same');

Mag = sqrt(Ey.^2 + Ex.^2);
Theta = atan2(Ey, Ex);

end

