function [out] = AddWeakEdges( x, y, res2, MagNMS2, T_low2 )

% res2(x,y) = MagNMS2(x,y);
res2(x,y) = true;

for r = -1:1
    for c = -1:1
        if ((x+r)>1) && ((x+r)<size(MagNMS2,1)) && ((y+c)>1) && ((y+c)<size(MagNMS2,2))
            if (MagNMS2(x+r, y+c) >= T_low2) && (res2(x+r, y+c) == 0)
                res2 = AddWeakEdges(x+r, y+c, res2, MagNMS2, T_low2);
            end
        end
    end
end

out = res2;

end
            
