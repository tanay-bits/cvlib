function [ E ] = EdgeLinking( MagNMS, T_high, T_low )

[m, n] = size(MagNMS);
res = zeros(m,n);


for i = 2:m-1
    for j = 2:n-1
        if MagNMS(i,j) >= T_high    %strong edge
            res = AddWeakEdges(i, j, res, MagNMS, T_low);
        end
    end
end

E = res;

end
