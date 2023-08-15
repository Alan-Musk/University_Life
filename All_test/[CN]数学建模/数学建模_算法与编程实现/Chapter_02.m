A=[1 1/2 4 3 4;
2 1 7 5 5;
1/4 1/7 1 1/2 1/3;
1/3 1/5 2 1 1;
1/3 1/5 3 1 1];

function [W,Lmax,CI,CR]= aAHP(A)
W=prod(A,2);
n=size(A,1);
W=nthroot(W,n);
W=W/sum(W);
Lmax=mean((A*M) ./M);
CI=(Lmax - n) /(n-1);
RI=[0 0 0.58 0.90 1.12 1.24 1.32 1.41 1.45 1.49 1.51];
CR=CI/RI(n);
end