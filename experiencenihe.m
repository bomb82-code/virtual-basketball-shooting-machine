clear
clc
BX = xlsread('/gradient_descent.csv');
x=[BX(:,2)];
y=[BX(:,3)];
z=[BX(:,4)];
m=[BX(:,6)];

plot3(x,y,m,'r*');
% plot3(y,z,m,'r*');
hold on

%  mesh(X,Y,m);
meanx=mean(x);
meany=mean(y);
meanz=mean(z);
x1=x-meanx;
y1=y-meany;
z1=z-meanz;

 modelfun1=@(c,BX)(c(1)*(x1).^2+c(2)*(y1).^2+c(3)*(z1).^2+c(4)*x1+c(5)*y1+c(6)*z1+c(7));
 beta1=[0 0 0 0 0 0 0];
%  modelfun1=@(c,BX)(c(1)*(x1-c(5)).^2+c(2)*(y1-c(6)).^2+c(3)*(z1-c(7)).^2+c(4));
%  beta1=[0 0 0 0 0 0 0];
mdl1=fitnlm(BX,m,modelfun1,beta1)
c=mdl1.Coefficients.Estimate;

x3=99.8:0.0001:100.2; 
y3=-0.1:0.0001:0.1; 
z3=44.99:0.0001:45.01;
[X,Y,Z]=meshgrid(x3,y3,z3);
findmax=(c(1)*(X-meanx).^2+c(2)*(Y-meany).^2+c(3)*(Z-meanz).^2+c(4)*(X-meanx)+c(5)*(Y-meany)+c(6)*(Z-meanz)+c(7));
[max_value, max_col] = max(findmax,[],(1));
[max_value, max_row] = max(findmax,[],(2));
[max_value, max_pal] = max(findmax,[],(3));
  


[X,Y]=meshgrid(x3,y3);
mnihe=c(1)*(X-meanx).^2+c(2)*(Y-meany).^2+c(4)*(X-meanx)+c(5)*(Y-meany)+c(7);
mesh(X,Y,mnihe);
% [Y,Z]=meshgrid(y3,z3);
% mnihe=c(2)*(Y-meany).^2+c(3)*(Z-meanz).^2+c(5)*(Y-meany)+c(6)*(Z-meanz)+c(7);
  
% mesh(Y,Z,mnihe);
colormap('winter')
shading interp 
hold off 
title('figure 1')

% plot(m,mnihe)

mnihe_result=c(1)*(100.0015-meanx)^2+c(2)*(-0.0002-meany)^2+c(3)*(45.0006-meanz)^2+c(4)*(100.0015-meanx)+c(5)*(-0.0002-meany)+c(6)*(45.0006-meanz)+c(7)