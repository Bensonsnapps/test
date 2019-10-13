function PGen_new = calPGen(beta, alpha, lambda, PGen_max)
	PGen_new = (lambda - beta) ./ (2 * alpha);
	PGen_new(PGen_new < 0) = 0;
	maximum = PGen_new > PGen_max;
	PGen_new(maximum) = PGen_max(maximum);
end