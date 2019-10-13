clear
clc
rng(11)
x = [150., 150., 100., 50.];
la = [7.63, 7.63, 8.24, 8.42];
y = [600., -150., 650., -50.];
De = [750, 750];
Pin = [1/2, 0, 0, 1/2;
	   1/3, 1/3, 1/3, 0;
	   0, 0, 1/2, 1/2;
	   0, 1/2, 0, 1/2];
Qout = [1/2, 0, 0, 1/3;
	    1/2, 1/2, 1/2, 0;
	    0, 0, 1/2, 1/3;
	    0, 1/2, 0, 1/3];
epsilon = 7.75e-4;
alpha = [-2535.2, -2535.2, -2023.2, -826.8];
beta = [352.1, 352.1, 257.5, 103.7];
gamma = [-8616.8, -7631.0, -3216.7];
x_max = [600., 600., 400., 200.];
x_min = [150., 150., 100., 50.];
x_old = [150., 150., 100., 50.];

%%%%
n = length(x);
Id = eye(n);
Bd = diag(beta);
C = [Pin, epsilon*Id; Bd*(Id-Pin), Qout-epsilon*Bd];
X = [la, y];
F = eye(2*n);
P = eye(2*n);
R = (0^2)*eye(2*n);
Q = 1e-5*eye(2*n);

start = 50;
finish = 70;
%%%%

iteration = 0;
attack = true;

%%%%
Xs = [];
Ys = [];
Las = [];
Ds = [];
while any(abs(y) > 1e-9)
	iteration = iteration + 1
    
    X = X * F';
	P = F * P * F' + Q;
	Z = X * C';
    if attack
		if iteration >= start && iteration < finish
			Z(1) = Z(1) + randn() * 10;
%R = (10^2)*eye(2*n);
        elseif iteration == finish
			R = (0^2)*eye(2*n);
        end
    end
    K = P * pinv(P + R);
	X = X + (Z - X) * K';
	P = P - K * P;
    %X = X * C';
    
    la = X(1:n);
    y = X(n+1:end);
    x = calX(beta, alpha, la, x_max, x_min, true);
    
    Xs = [Xs; x];
    Ys = [Ys; y];
    Las = [Las; la];
    Ds = [Ds; De];
    
    if iteration > 10000
        break
    end
end
%%%%

X = Xs';
Y = Ys';
La = Las';
D = Ds';

[m, n] = size(X);
it = 1:n;
subplot(221)
%figure(1)
hold on
title('Generation Power')
xlabel('iteration')
ylabel('power')
for i = 1:m
    plot(it, X(i,:))
    hold on
end

[m, n] = size(Y);
it = 1:n;
subplot(222)
%figure(2)
hold on
title('Local Mismatch')
xlabel('iteration')
ylabel('power')
for i = 1:m
    plot(it, Y(i,:))
    hold on
end

[m, n] = size(La);
it = 1:n;
subplot(223)
%figure(3)
hold on
title('Incremental Cost')
xlabel('iteration')
ylabel('\lambda')
for i = 1:m
    plot(it, La(i,:))
    hold on
end

subplot(224)
%figure(4)
tX = sum(X);
tD = sum(D);
[m, n] = size(La);
it = 1:n;
hold on
title('Total Power Mismatch')
xlabel('iteration')
ylabel('power')
plot(it, tX, it, tD, '--')
legend('generation power', 'demand power')