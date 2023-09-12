%%
clc,clear
x=0:0.5:4*pi;
y=sin(x); h=cos(x);
w=1./(1+exp(-x));
g=(1/(2*pi*2)^0.5).*exp((-1.*(x-2*pi).^2)./(2*2^2));
plot(x,y,'bd-',x,h,'gp:',x,w,'ro-',x,g,'c^-');
legend('sin(x)','cos(x)','Sigmoid','Gauss function');

%%
x=linspace(0,3);y=x.^2.*sin(x); plot(x,y);
line([2,2],[0,2^2*sin(2)]);
str='$$ \int_{0}^{2} x^2\sin(x) dx $$';
text(0.25,2.5,str,'Interpreter','latex');
annotation('arrow','X',[0,32,0.5],'Y',[0.6,0.4]);

%%
t=1:0.01:2;
f=t.^2;g=sin(2*pi.*t);
plot(t,f,'b-',t,g,'ro-');
title('Mini Assignment # 1')
xlabel('Time (ms)')
ylabel('f(t)')

%%
x=linspace(0,2*pi,1000);
y=sin(x);
h=plot(x,y);
get(h);
set(gca,'XLim',[0,2*pi])
set(h,'LineStyle','-.','LineWidth',7.0,'Color','g');
delete(h)

%%
x=rand(20,1);set(gca,'FontSize',18);
plot(x,'-md','LineWidth',2,'MarkerEdgeColor','k','MarkerFaceColor','g','MarkerSize',10);
xlim([1,20]);

%%
hold on
t=1:0.01:2;
f=t.^2;g=sin(2*pi.*t);
set(gca,'FontSize',18)
plot(t,f,'k-','LineWidth',5);
plot(t,g,'mo-','MarkerFaceColor','k');
title('Mini Assignment # 1')
xlabel('Time (ms)')
ylabel('f(t)')
