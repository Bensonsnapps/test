import numpy as np
import matplotlib.pyplot as plt

# initiate paramters
A = np.array([
	[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
	[1, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
	[1, 0, 0, 1, 0, 0, 1, 0, 0, 0], 
	[0, 1, 1, 0, 1, 1, 0, 1, 0, 0], 
	[0, 1, 0, 1, 0, 0, 0, 1, 0, 0], 
	[0, 0, 0, 1, 0, 0, 1, 1, 1, 1], 
	[0, 0, 1, 0, 0, 1, 0, 0, 0, 1], 
	[0, 0, 0, 1, 1, 1, 0, 0, 1, 0], 
	[0, 0, 0, 0, 0, 1, 0, 1, 0, 1], 
	[0, 0, 0, 0, 0, 1, 1, 0, 1, 0]
])
n_A = A.shape[0]
w = np.array([17.17, 12.28, 18.42, 7.06, 10.85, 18.91, 18.76, 15.70, 14.28, 10.15, 19.04, 16.97, 15.96, 14.70, 17.50, 10.97, 6.25, 17.53, 9.84])
b = np.array([0.0935, 0.0517, 0.1007, 0.0561, 0.0540, 0.1414, 0.0793, 0.1064, 0.0850, 0.0460, 0.0650, 0.0549, 0.0619, 0.0633, 0.0607, 0.2272, 0.1224, 0.0826, 0.0869])
alpha = np.array([0.0213, 0.0174, 0.0166, 0.0326, 0.0169, 0.0146, 0.0241, 0.0351, 0.0326, 0.0524])
beta = np.array([8.71, 5.63, 7.58, 10.24, 6.53, 12.25, 11.29, 10.30, 8.26, 5.30])
PGen_max = np.array([113.23, 179.10, 90.03, 106.41, 193.80, 37.19, 195.4, 62.17, 143.41, 125.00])
Pload_max = np.array([91.79, 147.29, 91.41, 62.96, 100.53, 66.88, 118.35, 73.81, 84.00, 110.32, 146.46, 62.61, 128.91, 116.08, 144.04, 24.15, 66.39,  106.14, 56.60])
lambdas = np.array([10., 9., 11., 15., 8., 14., 13., 14., 10., 7.])
group = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10])

deltax = 0.03
Ki = 1

def calPLo(P_load):
	P_Ls = np.zeros(len(lambdas))
	for j, i in enumerate(group):
		P_Ls[i-1] += P_load[j]
	return P_Ls

def calDeltaP(P_Gen, P_Lo):
	return P_Gen - P_Lo

def calDeltaPT(deltaP):
	a = np.sum(A, axis=1)
	return (deltaP @ (A - np.diag(a)).T) / a
	#return deltaP @ A.T

def calLambda(deltaPT_old, deltaPT):
	global sumPT
	sumPT += (deltaPT + deltaPT_old) * (deltax/2)
	return Ki * sumPT
	
def calPGen(lambdas):
	PGen_new = (lambdas - beta) / (2 * alpha)
	PGen_new[PGen_new < 0] = 0
	maximum = PGen_new > PGen_max
	PGen_new[maximum] = PGen_max[maximum]
	return PGen_new
	
def calPload(lambdas):
	lambdas_l = lambdas[group-1]
	Pload_new = (w - lambdas_l) / (2 * b)
	Pload_new[Pload_new < 0] = 0
	maximum = Pload_new > Pload_max
	Pload_new[maximum] = Pload_max[maximum]
	return Pload_new

deltaPT = np.ones(len(lambdas))
sumPT = lambdas

"""
phi_L = np.zeros(len(lambdas))
for j, i in enumerate(group):
	phi_L[i-1] += 1/(2*b[j])
phi_Gen = 1/(2*alpha)
phi_C = phi_L + phi_Gen
print(np.sum(phi_C))
"""
"""
print("lambdas: "+str(lambdas))
print("PGen: "+str(calPGen(lambdas)))
"""
iteration = 0
P = []
while any(np.abs(deltaPT) > 1e-9):
	iteration += 1
	P_Gen = calPGen(lambdas)
	P.append(P_Gen)
	P_load = calPload(lambdas)
	#P.append(P_load)
	
	P_Lo = calPLo(P_load)
	
	deltaP = calDeltaP(P_Gen, P_Lo)
	
	deltaPT_old = deltaPT
	deltaPT = calDeltaPT(deltaP)
	print(deltaPT)
	
	#lambdas = calLambda(deltaPT_old, deltaPT) if iteration != 1 else calLambda(deltaPT, deltaPT)
	lambdas = calLambda(0, deltaPT)
	#print(lambdas)
	print(iteration)
	if iteration > 10000:
		break

P = np.array(P).T
it = np.arange(P.shape[1])
for i in range(P.shape[0]):
	plt.plot(it, P[i, :])

plt.show()