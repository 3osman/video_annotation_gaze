
AIC = zeros(10,1);
BIC = zeros(10,1);
dim1 = 2;
dim2 = 3;
%data_p = unique(data(:,dim1:dim2),'rows');
X = data;
X(:,1) = X(:,1) - min(X(:,1));
X(:,1) = (X(:,1) - min(X(:,1))) / ( max(X(:,1)) - min(X(:,1)) );
X(:,2) = (X(:,2) - min(X(:,2))) / ( max(X(:,2)) - min(X(:,2)) );
X(:,3) = (X(:,3) - min(X(:,3))) / ( max(X(:,3)) - min(X(:,3)) );
data_p = X;
GMModels = cell(1,10);
options = statset('MaxIter',1000);
for k = 1:10
    GMModels{k} = fitgmdist(data_p,k,'Options',options,'RegularizationValue',0.001,'CovarianceType','full',...
        'SharedCovariance',false);
    AIC(k)= GMModels{k}.AIC;
    BIC(k) = GMModels{k}.BIC;
end

[minAIC,numComponents] = min(AIC);
%numComponents


[minBIC,numBComponents] = min(BIC);
%numBComponents

BestModel = GMModels{numComponents};
disp('GMM AIC')
disp(BestModel.NumComponents);
BestBModel = GMModels{numBComponents};
disp('=============================')
disp('GMM BIC')

disp(BestBModel.NumComponents);

disp('=============================')
disp('CalinskiHarabasz with K-means')

eva_k_CH = evalclusters(data_p,'kmeans','CalinskiHarabasz','KList',[1:10]);
disp(eva_k_CH.OptimalK)

disp('=============================')
disp('DaviesBoulidn with K-means')

eva_k_DB = evalclusters(data_p,'kmeans','DaviesBouldin','KList',[1:10]);
disp(eva_k_DB.OptimalK)

disp('=============================')
disp('Silhoutte with K-means')

eva_k_silhouette = evalclusters(data_p,'kmeans','silhouette','KList',[1:10]);
disp(eva_k_silhouette.OptimalK)

disp('=============================')
disp('=============================')
disp('CalinskiHarabasz with GMM')

eva_g_CH = evalclusters(data_p,'gmdistribution','CalinskiHarabasz','KList',[1:10]);
disp(eva_g_CH.OptimalK)

disp('=============================')
disp('DaviesBoulidn with GMM')

eva_g_DB = evalclusters(data_p,'gmdistribution','DaviesBouldin','KList',[1:10]);
disp(eva_g_DB.OptimalK)

disp('=============================')
disp('Silhoutte with GMM')

eva_g_silhouette = evalclusters(data_p,'gmdistribution','silhouette','KList',[1:10]);
disp(eva_g_silhouette.OptimalK)

