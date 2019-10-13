lambda = 12.5;
wi = 17.17;
bi = 0.0935;
PLoad = 0:350;
a = utility(PLoad, wi, bi);
b = lambdaPL(PLoad, lambda);
figure(1)
plot(PLoad, a, 'r', PLoad, b, 'b', PLoad, a-b, 'g')

PGen = 0:350;
alphai = 0.0417;
betai = 6.53;
a = cost(PGen, alphai, betai);
b = lambdaPG(PGen, lambda);
figure(2)
plot(PGen, a, 'r', PGen, b, 'b', PGen, b-a, 'g')

function PLoad = utility(PLoad, wi, bi)
    PLoad(PLoad>=wi/(2*bi)) = (wi^2)/(4*bi);
	para = PLoad<wi/(2*bi);
	PLoad(para) = wi*PLoad(para) - bi*(PLoad(para).^2);
end
	
function la = lambdaPL(PLoad, lambda)
    la =  lambda * PLoad;
end

function c = cost(PGen, alphai, betai)
	c = alphai * PGen .^ 2 + betai * PGen;
end
	
function la = lambdaPG(PGen, lambda)
	la = lambda * PGen;
end
