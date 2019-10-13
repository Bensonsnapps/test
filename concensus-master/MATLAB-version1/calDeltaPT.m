function deltaPT = calDeltaPT(deltaP, A)
    a = sum(A,2)';
    deltaPT = (deltaP * (A - diag(a))') ./ a;
end