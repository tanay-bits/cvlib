%% K-MEANS CLUSTERING (K=2)

Hnorm = Hhs_norm;
dim1 = 1000;
dim2 = 1000;

% initialize cluster centers:
C1 = 0.002;
C0 = 0;

% initialize cluster bags:
g1 = [];
g0 = [];

% initialize avg squared Euclidean distances:
dC1mean = 1;
dC0mean = 1;

% iterate till both distances converge:
iterations = 0;
while ((dC1mean > 0.0001) || (dC0mean > 0.0001)) && iterations < 4
    % group each data point (i,j indices of 2D hist in this case):
    for i = 1:dim1
        for j = 1:dim2
            z = Hnorm(i,j);
            dC1 = (z - C1)^2;
            dC0 = (z - C0)^2;
            if dC1 < dC0
                g1 = cat(1,g1,[i j]);
            else
                g0 = cat(1,g0,[i j]);
            end
        end
    end

    % find the new cluster centers:
    z1s = [];
    for g1ind = 1:size(g1,1)
        ij = g1(g1ind,:);
        i = ij(1);
        j = ij(2);   
        z1s = cat(1, z1s, Hnorm(i,j));
    end
    C1 = mean(z1s);

    z0s = [];
    for g0ind = 1:size(g0,1)
        ij = g0(g0ind,:);
        i = ij(1);
        j = ij(2);   
        z0s = cat(1, z0s, Hnorm(i,j));
    end
    C0 = mean(z0s);

    % find avg squared Euclidean distance of each cluster from its 
    % new center:
    dC1bag = [];
    for g1ind = 1:size(g1,1)
        ij = g1(g1ind,:);
        i = ij(1);
        j = ij(2);   
        
        z = Hnorm(i,j);
        dC1 = (z - C1)^2;
        dC1bag = cat(1, dC1bag, dC1);
    end
    dC1mean = mean(dC1bag);

    dC0bag = [];
    for g0ind = 1:size(g0,1)
        ij = g0(g0ind,:);
        i = ij(1);
        j = ij(2);   
        
        z = Hnorm(i,j);
        dC0 = (z - C0)^2;
        dC0bag = cat(1, dC0bag, dC0);
    end
    dC0mean = mean(dC0bag);

    
    iterations = iterations + 1;
end
