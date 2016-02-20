function [ MagNMS ] = NonmaximaSuppress( Mag, Theta )

[m, n] = size(Mag);
MagNMS = zeros(m,n);

%convert atan2 rads to rads b/w 0 and 2pi:
for i=1:m
    for j=1:n
        if Theta(i,j) < 0
            Theta(i,j) = Theta(i,j) + 2*pi;
        end
    end
end

%nonmaxima suppression using 4 sections:
for i=2:m-1
    for j=2:n-1
        %section 0:
        if ((7*pi/4 + pi/8) < Theta(i,j) < 2*pi) || (0 <= Theta(i,j) <= pi/8) || (3*pi/4 + pi/8) < Theta(i,j) <= (pi + pi/8)
            if Mag(i,j) < Mag(i,j+1) || Mag(i,j) < Mag(i,j-1)
                MagNMS(i,j) = 0;
            else
                MagNMS(i,j) = Mag(i,j);
            end
        end
        %section 1:
        if ((pi/4 - pi/8) < Theta(i,j) <= (pi/4 + pi/8)) || ((5*pi/4 - pi/8) < Theta(i,j) <= (5*pi/4 + pi/8))
            if Mag(i,j) < Mag(i-1,j+1) || Mag(i,j) < Mag(i+1,j-1)
                MagNMS(i,j) = 0;
            else
                MagNMS(i,j) = Mag(i,j);
            end
        end
        %section 2:
        if ((pi/2 - pi/8) < Theta(i,j) <= (pi/2 + pi/8)) || ((6*pi/4 - pi/8) < Theta(i,j) <= (6*pi/4 + pi/8))
            if Mag(i,j) < Mag(i-1,j) || Mag(i,j) < Mag(i+1,j)
                MagNMS(i,j) = 0;
            else
                MagNMS(i,j) = Mag(i,j);
            end
        end
        %section 3:
        if ((3*pi/4 - pi/8) < Theta(i,j) <= (3*pi/4 + pi/8)) || ((7*pi/4 - pi/8) < Theta(i,j) <= (7*pi/4 + pi/8))
            if Mag(i,j) < Mag(i-1,j-1) || Mag(i,j) < Mag(i+1,j+1)
                MagNMS(i,j) = 0;
            else
                MagNMS(i,j) = Mag(i,j);
            end
        end
    end
end

end

