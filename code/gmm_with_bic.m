
AIC = zeros(7,4);
BIC = zeros(7,4);

GMModels = cell(1,7);
options = statset('MaxIter',500);
for k = 1:7
    GMModels{k} = fitgmdist(unique(data(:,2:3),'rows'),k,'Options',options,'CovarianceType','diagonal');
    AIC(k)= GMModels{k}.AIC;
    BIC(k) = GMModels{k}.BIC;
end

[minAIC,numComponents] = min(AIC);
numComponents


[minBIC,numBComponents] = min(BIC);
numBComponents

BestModel = GMModels{numComponents}

BestBModel = GMModels{numBComponents}

eva = evalclusters(unique(data(:,2:3),'rows'),'kmeans','CalinskiHarabasz','KList',[1:7])
eva2 = evalclusters(unique(data(:,2:3),'rows'),'gmdistribution','CalinskiHarabasz','KList',[1:7])
