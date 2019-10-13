init
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
    De = calDe(b, a, la, group);
	y = calY(Qout, y, x, x_old, De, De_old, group);
    
    if iteration == 50
        la_attack = la(1);
        y_attack = y(1);
    end
    if attack
%         la(1) = la(1) + 10 * (0.9 ^ iteration);
%         y(1) = y(1) + 20 * (0.85 ^ iteration);
        if iteration >= 60 && iteration <= 70
%             la(1) = la(1) + 10 * randn() + 1;
%             y(1) = y(1) + 10 * randn() + 1;
            la(1) = la_attack+1;
            y(1) = y_attack+10;
        end
    end

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
subplot(221)
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
hold on
title('Incremental Cost')
xlabel('iteration')
ylabel('\lambda')
for i = 1:m
    plot(it, La(i,:))
    hold on
end

subplot(224)
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