function Pload_new = calPload(lambda, group, w, b, Pload_max)
	lambda_l = lambda(group);
	Pload_new = (w - lambda_l) ./ (2 * b);
	Pload_new(Pload_new < 0) = 0;
	maximum = Pload_new > Pload_max;
	Pload_new(maximum) = Pload_max(maximum);
end