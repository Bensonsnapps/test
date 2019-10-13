import numpy as np
import matplotlib.pyplot as plt

np.random.seed(11)

x = np.array([150., 150., 100., 50.])
la = np.array([7.63, 7.63, 8.24, 8.42])
y = np.array([600., -150., 650., -50.])
De = 1500
Pin = np.array([
	[1/2, 0, 0, 1/2], 
	[1/3, 1/3, 1/3, 0], 
	[0, 0, 1/2, 1/2], 
	[0, 1/2, 0, 1/2]
])
Qout = np.array([
	[1/2, 0, 0, 1/3], 
	[1/2, 1/2, 1/2, 0], 
	[0, 0, 1/2, 1/3], 
	[0, 1/2, 0, 1/3] 
])
n = len(x)
epsilon = 7.75e-4
Id = np.eye(n)
alpha = np.array([-2535.2, -2535.2, -2023.2, -826.8])
beta = np.array([352.1, 352.1, 257.5, 103.7])
Bd = np.diag(beta)
gamma = np.array([-8616.8, -7631.0, -3216.7])
x_max = np.array([600., 600., 400., 200.])
x_min = np.array([150., 150., 100., 50.])
x_old = np.array([150., 150., 100., 50.])
C = np.vstack((np.hstack((Pin, epsilon*Id)), np.hstack((Bd@(Id-Pin), Qout-epsilon*Bd))))

X = np.hstack((la, y))
F = np.eye(2*n)
P = np.eye(2*n)
R = (0.**2)*np.eye(2*n)
Q = 1e-5*np.eye(2*n)

def calY():
	return Qout @ y - x + x_old

def calLambda():
	return Pin @ la + epsilon * y
	
def calX(constraint=False):
	if constraint:
		temp = beta * la + alpha
		maximum = temp > x_max
		temp[maximum] = x_max[maximum]
		minimum = temp < x_min
		temp[minimum] = x_min[minimum]
		return temp

	return beta * la + alpha
	
attack = True
start = 50
end = 70
iteration = 0
Ps = []
la = X[0:n]
y = X[n:]
while any(np.abs(y) > 1e-9):
	iteration += 1
	
	X = F @ X
	P = F @ P @ F.T + Q
	Z = C @ X
	if attack:
		if iteration >= start and iteration < end:
			Z[0] += np.random.randn() * 10
			R = (10.**2)*np.eye(2*n)
		elif iteration == end:
			R = (0.**2)*np.eye(2*n)
	K = P @ np.linalg.pinv(P + R)
	X = X + K @ (Z - X)
	P = P - K @ P
	#X = C @ X
	la = X[0:n]
	y = X[n:]
	x = calX(True)
	
	Ps.append(x)
	print(la)
	print(iteration)
	
	if iteration > 50000:
		break

Ps = np.array(Ps).T
Ss = Ps.sum(axis=0)
it = np.arange(Ps.shape[1])
plt.plot(it, Ss, [1, len(Ss)], [De, De], '--')
#for i in range(Ps.shape[0]):
#	plt.plot(it, Ps[i, :])

plt.show()