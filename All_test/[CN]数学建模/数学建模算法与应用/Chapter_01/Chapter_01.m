%%
clc,clear
c=[4,3];b=[10,8,7];
a=[2,1;1,1;0,1];lb=zeros(2,1);
[x,fval]=linprog(-c,a,b,[],[],lb)
y=-fval

%%
clc,clear
prob=optimproblem('ObjectiveSense','max')
c=[4;3];b=[10;8;7];
a=[2,1;1,1;0,1];
x=optimvar('x',2,'LowerBound',0);  %决策变量 创建包含两个元素的向量,下界被限制为0
prob.Objective=c'*x;               %创建prob的目标函数
prob.Constraints.con=a*x<=b;       %约束条件
[sol,fval,flag,out]=solve(prob)
sol.x

%%
clc,clear
c=[-2;-3;5];            % 价值向量
a=[-2,5,-1;1,3,1];b=[-10;12];   % a,b 线性不等式约束
aeq=[1,1,1];beq=7;              % aeq,beq 线性等式约束
[x,y]=linprog(c,a,b,aeq,beq,zeros(3,1));
x,y=-y

%%
clc,clear
prob=optimproblem('ObjectiveSense','max');
x=optimvar('x',3,'LowerBound',0);
prob.Objective=2*x(1)+3*x(2)-5*x(3);
prob.Constraints.con1=x(1)+x(2)+x(3)==7;
prob.Constraints.con2=2*x(1)-5*x(2)+x(3)>=10;
prob.Constraints.con3=x(1)+3*x(2)+x(3)<=12;
[sol,fval,flag,out]=solve(prob),sol.x

%%
clc,clear
prob=optimproblem; %默认目标函数最小化
x=optimvar('x',4,4,'LowerBound',0);
prob.Objective=2800*sum(x(:,1))+4500*sum(x(1:3,2))+6000*sum(x(1:2,3))+7300*x(1,4);
prob.Constraints.con=[sum(x(1,:))>=15,
    sum(x(1,2:4))+sum(x(2,1:3))>=10,
    x(1,3)+x(1,4)+x(2,2)+x(2,3)+x(3,1+x(3,2))>=20,
    x(1,4)+x(2,3)+x(3,2)+x(4,1)>=12];
[sol,fval,flag,out]=solve(prob),sol.x

%%
clc,clear,a=load('data1_5_1.txt');
c=a(1:end-1,1:end-1);
e=a(1:end-1,end);d=a(end,1:end-1);
prob=optimproblem;
x=optimvar('x',6,8,'LowerBound',0);
prob.Objective=sum(sum(c.*x));     % 目标函数
prob.Constraints.con1=sum(x,1)==d;  % 计算 x矩阵 列总和
prob.Constraints.con2=sum(x,2)<=e;  % 极速那 x矩阵 行总和
[sol,fval,flag,out]=solve(prob),xx=sol.x
writematrix(xx,'data1_5_2.xlsx')

%%
clc,clear
c=[1:4]';b=[-2,-1,-1/2]';
a=[1,-1,-1,1;1,-1,1,-3;1,-1,-2,3];
prob=optimproblem;
u=optimvar('u',4,'LowerBound',0);
v=optimvar('v',4,'LowerBound',0);
prob.Objective=sum(c'*(u+v));
prob.Constraints.con=a*(u-v)<=b;
[sol,fval,flag,out]=solve(prob)
x=sol.u-sol.v

%%
clc,clear,close all  % close all 关闭所有图像窗口
prob=optimproblem('ObjectiveSense','max');
x=optimvar('x',5,1,'LowerBound',0);
c=[0.05,0.27,0.19,0.185,0.185]; % 净收益率
Aeq=[1,1.01,1.02,1.045,1.065];  % 等号约束矩阵
prob.Objective=c*x;M=10000;
prob.Constraints.con1=Aeq*x==M;
q=[0.025,0.015,0.055,0.026]';   %风险损失率
a=0;aa=[];QQ=[];XX=[];hold on
while a<0.05
    prob.Constraints.con2=q.*x(2:end)<=a*M;
    [sol,Q,flag,out]=solve(prob);
    aa=[aa;a];QQ=[QQ,Q];
    XX=[XX;sol.x'];a=a+0.001;
end
plot(aa,QQ,'*k')
xlabel('$a$','Interpreter','Latex'),
ylabel('$Q$','Interpreter','Rotation',0)

%%
clc,clear,close all,format long g % 设置输出结果的显示格式。
M=10000;prob=optimproblem;
x=optimvar('x',6,1,'LowerBound',0);
r=[0.05,0.28,0.21,0.23,0.25]; % 收益率
p=[0,0.01,0.02,0.045,0.065];  % 交易费率
q=[0,0.025,0.015,0.055,0.026]'; % 风险损失率
w=[0.766, 0.767,0.810,0.811,0.824,0.825,0.962,0.963,1.0]
V=[];   % 风险初始化
Q=[];   % 收益初值化
X=[];   % 最优解的初始化
prob.Constraints.con1=(1+p)*x(1:end-1)==M
prob.Constraints.con2=q(2,end).*x(2:end-1)<=x(end);
for i =1:length(w)
    prob.Objective=w(i)*x(end)-(1-w(i))*(r-p)*x(1:end-1);
    [sol,fval,flag,out]=solve(prob);
    xx=sol.x; V=[V,max(q.*xx(1:end-1))];
    Q=[Q,(r-p)*xx(1:end-1)];X=[X;xx'];
    plot(V,Q,'*-');grid on
    xlabel('风险/元');ylabel('收益/元')
end
V,Q,format


