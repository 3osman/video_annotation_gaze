clus = zeros(324,1);
for i=1:length(clusts_R{6})
    for j=1:length(clusts_R{6}{i})
        clus(clusts_R{6}{i}(j)) = i;
    end
end
 
clr = hsv(K);
figure, hold on
%tmp_clr1 = tmp_clr(1:9,:);
scatter(data(:,2), data(:,3), 100, tmp_clr(clus,:), 'Marker','.')
%scatter3(C(:,1), C(:,2), C(:,3), 100, clr, 'Marker','o', 'LineWidth',3)
hold off
%view(3), axis vis3d, box on, rotate3d on
xlabel('X'), ylabel('Y')
%, zlabel('Y')



%# K-means clustering
%# (K: number of clusters, G: assigned groups, C: cluster centers)
K = 10;
X= data;
%f = X(:,1) - min(X(:,1));
X = X - repmat(mean(X),size(X,1),1);
X = X/max(max(abs(X)));
%X(:,1) = X(:,1) - min(X(:,1));
%X(:,1) = (X(:,1) - min(X(:,1))) / ( max(X(:,1)) - min(X(:,1)) );
%X(:,2) = (X(:,2) - min(X(:,2))) / ( max(X(:,2)) - min(X(:,2)) );
%X(:,3) = (X(:,3) - min(X(:,3))) / ( max(X(:,3)) - min(X(:,3)) );

[G,C] = kmeans(X, K, 'distance','sqEuclidean','MaxIter',1000,'Replicates',50);
%# show points and clusters (color-coded)
clr = hsv(K);
figure, hold on
%tmp_clr1 = tmp_clr(1:9,:);
scatter3(data(:,1), data(:,2), data(:,3), 36, clr(G,:), 'Marker','.')
%scatter3(C(:,1), C(:,2), C(:,3), 100, clr, 'Marker','o', 'LineWidth',3)
hold off
view(3), axis vis3d, box on, rotate3d on
xlabel('Time'), ylabel('X'), zlabel('Y')

k_gmm = 9;
obj = fitgmdist(X,k_gmm,'Options',options,'CovarianceType','full',...
        'SharedCovariance',false,'RegularizationValue',0.001,'Replicates',50);
converged = obj.Converged
figure, hold on
[idx,nlogl,P] = cluster(obj,X);
scatter3(data(:,1), data(:,2), data(:,3), 36, clr(idx,:), 'Marker','.')
%scatter3(C(:,1), C(:,2), C(:,3), 100, tmp_clr, 'Marker','o', 'LineWidth',3)
hold off
view(3), axis vis3d, box on, rotate3d on
xlabel('Time'), ylabel('X'), zlabel('Y')