function [lambda, sumPT] = calLambda(deltaPT_old, deltaPT, sumPT, Ki, deltax)
    sumPT = sumPT + (deltaPT + deltaPT_old) * (deltax/2);
    lambda = Ki * sumPT;
end
