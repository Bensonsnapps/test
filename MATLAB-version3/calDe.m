function [De , disperse]= calDe(b, a, la, group, constraint, n, lo_max, lo_min)
	disperse = b .* la(group) + a;
	if constraint
		maximum = disperse > lo_max;
		disperse(maximum) = lo_max(maximum);
		minimum = disperse < lo_min;
		disperse(minimum) = lo_min(minimum);
    end
	
	De = zeros(1,n);
	for j=1:length(group)
		De(group(j)) = De(group(j)) + disperse(j);
    end
end