init39bus
X = [];
Y = [];
La = [];
D = [];

while any(abs(y) > 1e-9)
	iteration = iteration + 1
	la = calLambda(Pin, la, epsilon, y);
	x_old = x;
	x = calX(beta, alpha, la, x_max, x_min, true);
    De_old = De;
    [De, dis] = calDe(b, a, la, group, true, n, lo_max, lo_min);
	y = calY(Qout, y, x, x_old, De, De_old, generator);

    X = [X; x];
    Y = [Y; y];
    La = [La; la];
    D = [D; De];
    if iteration > 10000
        break
    end
end

X = X';
Y = Y';
La = La';
D = D';

[m, n] = size(X);
it = 1:n;
%subplot(221)
figure(1)
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
%subplot(222)
figure(2)
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
%subplot(223)
figure(3)
hold on
title('Incremental Cost')
xlabel('iteration')
ylabel('\lambda')
for i = 1:m
    plot(it, La(i,:))
    hold on
end

%subplot(224)
figure(4)
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
