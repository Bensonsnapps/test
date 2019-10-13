function x = calX(beta, alpha, la, x_max, x_min, constraint)
	if constraint
		temp = beta .* la + alpha;
		maximum = temp > x_max;
		temp(maximum) = x_max(maximum);
		minimum = temp < x_min;
		temp(minimum) = x_min(minimum);
		x = temp;
    else
		x = beta .* la + alpha;
end