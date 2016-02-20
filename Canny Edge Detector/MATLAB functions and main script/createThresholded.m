function [ Mag_high, Mag_low ] = createThresholded( MagNMS, T_high, T_low )

[m, n] = size(MagNMS);

for i = 1:m
    for j = 1:n
        if MagNMS(i,j)<T_high
            Mag_high(i,j) = 0;
        else
            Mag_high(i,j) = MagNMS(i,j);
        end
    end
end

for i = 1:m
    for j = 1:n
        if MagNMS(i,j)<T_low
            Mag_low(i,j) = 0;
        else
            Mag_low(i,j) = MagNMS(i,j);
        end
    end
end
