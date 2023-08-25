%% 
clc,clear
prob=optimproblem('ObjectiveSense','max');
x=optimvar('x',3,'LowerBound',0);
prob.Objective=3*x(1)-x(2)-x(3);
prob.Constraints.con1=x(1)-2*x(2)+x(3)<=11;
prob.Constraints.con2=-4*x(1)+x(2)+2*x(3)>=3;
prob.Constraints.con3=-2*x(1)+x(3)==1;
[sol,fval,flag,out]=solve(prob)
xx=sol.x
%%
clc,clear
c=[1,4]';b=[0,1,-1/2];A=[1,-1,-1,1;1,-1,1,-3;1,-1,-2,3];
prob=optimproblem;
u=optimvar('u',4,'LowerBound',0);
v=optimvar('v',4,'LowerBound',0);
prob.Objective=sum(c'*(u+v));
prob.Constraints.con=a*(u-v)<=b;
[sol,fval,flag,out]=solve(prob)
x=sol.u-sol.v

%%
clc,clear,format long g
x=optimvar('x',9,'Type','integer','LowerBound',0);
prob=optimproblem('ObjectiveSense','max');
prob.Objective=x(1)+x(2)+1.65*x(8)+2.3*x(9)-0.05*(5*x(1)+10*x(6))-312/1000*(7*x(2)+9*x(7)+12*x(9))...
    -250/4000*(6*x(3)+8*x(8))-783/7000*(4*x(4)+11*x(9))-200/4000*(7*x(5));
con1=[5*x(1)+10*x(6)<=6000,7*x(2)+9*x(7)+12*x(9)<=10000,6*x(3)+8*x(8)<=4000,4*x(4)+11*x(9)<=7000,7*x(5)<=4000];
con2=[x(1)+x(2)==x(3)+x(4)+x(5),x(6)+x(7)==x(8)];
prob.Constraints.con1=con1
prob.Constraints.con2=con2
[sol,fval,flag]=solve(prob),
sol.x,format
