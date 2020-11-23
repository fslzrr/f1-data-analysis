% Carlos Gerardo Herrera Cortina - a00821946
% hecho en matlab

M = readtable('results.csv');
head(M);
points = M(:,10);
pointsArray = table2array(points);
hist(pointsArray)
%pointsArray = pointsArray.'
%pointsArray = cell2mat(pointsArray);
hist(pointsArray)
media = mean(pointsArray)
varianza = var(pointsArray)
std = std(pointsArray)
simetria = skewness (pointsArray)
curtosis = kurtosis(pointsArray)

h = adtest(pointsArray) % la distribucion no es normal

% hacer clear si no funcionan las variables


%expfit = expfit(pointsArray)

%h1 = lillietest(log(pointsArray),'Distribution','extreme value')

%pd = fitdist(pointsArray,'Weibull'); h = chi2gof(pointsArray,'CDF',pd)
pd = fitdist (pointsArray, 'Exponential')
%if isvector(pointsArray)
%    disp("xd")
%end
boxplot(pointsArray)
boxplot(pd)
