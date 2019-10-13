import numpy as np
import matplotlib.pyplot as plt
lambdas = 12.5
"""
w = np.array([17.17, 12.28, 18.42, 7.06, 10.85, 18.91, 18.76, 15.70, 14.28, 10.15, 19.04, 06.97, 15.96, 14.70, 17.50, 10.97, 16.25, 17.53, 09.84])
b = np.array([0.0935, 0.0417, 0.1007, 0.0561, 0.0540, 0.1414, 0.0793, 0.1064, 0.0850, 0.0460, 0.0650, 0.0549, 0.0619, 0.0633, 0.0607, 0.2272, 0.1224, 0.0826, 0.0869])
wi = 17.17
bi = 0.0935
def utility(PLoad):
	PLoad[PLoad>=wi/(2*bi)] = (wi**2)/(4*bi)
	para = PLoad<wi/(2*bi)
	PLoad[para] = wi*PLoad[para] - bi*(PLoad[para]**2)
	return PLoad
	
def lambdaP(PLoad):
	return lambdas * PLoad

def surplus(PLoad):
	return utility(PLoad.copy()) - lambdaP(PLoad.copy())
	
PLoad = np.arange(0,351)
a = utility(PLoad.copy())
b = lambdaP(PLoad.copy())
print((wi-lambdas)/(2*bi))
plt.plot(PLoad, a, 'r', PLoad, b, 'b', PLoad, a-b, 'g')
plt.show()
"""
alpha = np.array([0.0031, 0.0074, 0.0066, 0.0063, 0.0069, 0.0014, 0.0041, 0.0051, 0.0032, 0.0025])
beta = np.array([8.71, 3.53, 7.58, 2.24, 8.53, 2.25, 6.29, 4.30, 8.26, 5.30])
alphai = 0.0417
betai = 6.53
def cost(PGen):
	return alphai * PGen ** 2 + betai * PGen
	
def lambdaP(PGen):
	return lambdas * PGen

def surplus(PGen):
	return cost(PGen) - lambdaP(PGen)
	
PGen = np.arange(0,351)
a = cost(PGen.copy())
b = lambdaP(PGen.copy())
print((lambdas-betai)/(2*alphai))
plt.plot(PGen, a, 'r', PGen, b, 'b', PGen, b-a, 'g')
plt.show()
