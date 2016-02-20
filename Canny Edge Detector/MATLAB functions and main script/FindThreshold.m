function [ T_low, T_high ] = FindThreshold( Mag, percentageOfNonEdge )
% percentageOfNonEdge should be b/w 0 and 100

[Histo, edges] = histcounts(Mag);
cHisto = cumsum(Histo);
totalcount = sum(Histo);
temp = find(cHisto > (percentageOfNonEdge/100)*totalcount);
tau = temp(1);

T_high = (tau/(size(Histo,2)-1))*(max(Mag(:))-min(Mag(:))) + min(Mag(:));
T_low = T_high/2;
    
end

