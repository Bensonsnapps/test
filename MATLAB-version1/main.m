init
P_G = [];
P_L = [];
% n = randi(10);
n = 3;
c_iter = 90;
while any(abs(deltaPT) > 1e-9)
	iteration = iteration + 1;
	P_Gen = calPGen(beta, alpha, lambda, PGen_max);
    P_G = [P_G; P_Gen];
	P_load = calPload(lambda, group, w, b, Pload_max);
    P_L = [P_L; P_load];
	
	P_Lo = calPLo(n_gen, P_load, group);
	
	deltaP = calDeltaP(P_Gen, P_Lo);
    
    if iteration == c_iter
        noise = wgn(1,1,15)
        deltaP(n) = deltaP(n) + wgn(1,1,15);
    end
	
	if iteration == 1
        deltaPT_old = zeros(1, n_gen);
    else
        deltaPT_old = deltaPT;
    end
    
	deltaPT = calDeltaPT(deltaP, A);
	
	[lambda, sumPT] = calLambda(0, deltaPT, sumPT, Ki, deltax);
    if iteration > 1000
        break
    end
end
P_G = P_G';
P_L = P_L';
[m, n] = size(P_G);
it = 1:n;
figure(1)
for i = 1:m
    plot(it, P_G(i,:))
    hold on
end

[m, n] = size(P_L);
it = 1:n;
figure(2)
for i = 1:m
    plot(it, P_L(i,:))
    hold on
end
D=diag(sum(A,2));
L=D-A;
t0=0; tf=50;
figure (3)
[t,x]=ode45(@thesisfun,[t0 tf], lambda, [], L);
plot(t,x)