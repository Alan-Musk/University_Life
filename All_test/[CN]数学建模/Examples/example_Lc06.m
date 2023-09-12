%%
x=logspace(-1,1,100); % 生成一个对数尺度上均匀分布的数值
y=x.^2;
subplot(2,2,1);        % 创建一个多图窗口 argument1:行 argument2:列 argument3:序号
plot(x,y);
title('Plot');
subplot(2,2,2);
semilogx(x,y);  %用于在半对数坐标轴上绘制图形。半对数坐标轴指的是其中一个坐标轴（通常是 x 轴或 y 轴）使用对数刻度，而另一个坐标轴使用线性刻度
subplot(2,2,3);
semilogy(x,y);
title('Semilogy');
subplot(2,2,4);
loglog(x,y);
title('Loglog'); %用于在双对数坐标轴上绘制图形
grid on;

%% 波浪图
x=0:0.01:20;
y1=200*exp(-0.05*x).*sin(x);
y2=0.8*exp(-0.5*x).*sin(10*x);
[AX,H1,H2]=plotyy(x,y1,x,y2);
set(get(AX(1),'Ylabel'),'String','Left Y-axis')
set(get(AX(2),'Ylabel'),'String','Right Y-axis')
title('Labeling plotyy');
set(H1,'LineStyle','--');
set(H2,'LineStyle',':');

%% 柱状图 总体
y=randn(1,1000);  % 1行 1000列
subplot(2,1,1);
hist(y,10);         % 将数据分为10个区间
title('Bins=10');
subplot(2,1,2);
hist(y,50);
title('Bins=50');

%% 柱状体 个体
x=[1,2,5,4,8];
y=[x;1:5];
subplot(1,3,1); bar(x); title('A bargraph of vector x');
subplot(1,3,2); bar(y); title('A bargraph of vector y');
subplot(1,3,3); bar3(y); title('A 3D bargraph');

%% 柱状图 叠放形式 水平形式
x=[1,2,5,4,8];
y=[x;1:5];
subplot(1,2,1);
bar(y,'stacked');
title('Stacked');

subplot(1,2,2);
barh(y);
title('Horizontal');

%% pie charts
a=[10 5 20 30];
subplot(1,3,1); pie(a);
subplot(1,3,2); pie(a,[0,0,1,1]);
subplot(1,3,3); pie3(a);

%% 极坐标图
x=1:100;
theta=x/10;
r=log10(x);
subplot(1,4,1); polar(theta,r);
theta=linspace(0,2*pi); r=cos(4*theta);
subplot(1,4,2); polar(theta,r);
theta=linspace(0,2*pi,7); r=ones(1,length(theta));
subplot(1,4,3); polar(theta,r);
theta=linspace(0,2*pi); r=1-sin(theta);
subplot(1,4,4); polar(theta,r);

%% 梯形图 或 分散柱图
x=linspace(0,4*pi,40);
y=sin(x);
subplot(1,2,1); stairs(y);
subplot(1,2,2); stem(y);

%% 3D 彩图
[x,y]=meshgrid(-3:.2:3,-3:.2:3);  %用于生成二维坐标网格
z=x.^2+x.*y+y.^2; 
surf(x,y,z); box on;  %surf 函数用于绘制三维曲面图
set(gca,'FontSize',16); zlabel('z');
xlim([-4 4]); xlabel('x'); ylim([-4 4]); ylabel('y');
imagesc(z); axis square;  %设置坐标轴纵横比为正方形
colorbar;
colormap(cool);

%% 
x=-2:0.05:2;
y=-2:0.05:2;
[X,Y]=meshgrid(x,y);
Z=X.*exp(-X.^2-Y.^2);
[C,h]=contourf(Z,[-0.45:0.05:0.45]);
clabel(C,h);
axis square

set(gca,'XTick',1:20:81);
set(gca,'YTick',1:10:81);
set(gca,'XTickLabel',-2:1:2);
set(gca,'YTickLabel',-2:0.5:2);
colormap("jet");
axis square

%%
