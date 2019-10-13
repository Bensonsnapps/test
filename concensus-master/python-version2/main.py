import numpy as np
import matplotlib.pyplot as plt

# initiate paramters
x = np.array([150., 150., 100., 50.])
la = np.array([7.63, 7.63, 8.24, 8.42])
y = np.array([600., -150., 650., -50.])
De = np.array([750, 750])
De_old = np.array([750, 750])
group = np.array([0, 2])
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
epsilon = 7.75e-4
alpha = np.array([-2535.2, -2535.2, -2023.2, -826.8])
beta = np.array([352.1, 352.1, 257.5, 103.7])
gamma = np.array([-8616.8, -7631.0, -3216.7])
a = np.array([791.8, 847.2])
b = np.array([-5.35, -11.99])
r = np.array([788.3, 904.1])
x_max = np.array([600., 600., 400., 200.])
x_min = np.array([150., 150., 100., 50.])
x_old = np.array([150., 150., 100., 50.])

def calY():
	temp = Qout @ y - x + x_old
	temp[group] += (De - De_old)
	return temp

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
	
def calDe():
	return b * la[group] + a 

attack = False
iteration = 0
Ps = []
while any(np.abs(y) > 1e-9):
	iteration += 1
	la = calLambda()
	x_old = x
	x = calX(True)
	De_old = De
	De = calDe()
	y = calY()
	if attack:
		#la[0] += 10 * (0.15 ** iteration)
		#y[0] += 20 * (0.85 ** iteration)
		if iteration >= 5 and iteration <= 10:
			la[0] += (1 + np.random.randn() * 10)
			y[0] += (1 + np.random.randn() * 10)
	
	Ps.append(la)
	print(la)
	print(iteration)
	
	if iteration > 500:
		break

Ps = np.array(Ps).T
it = np.arange(Ps.shape[1])
for i in range(Ps.shape[0]):
	plt.plot(it, Ps[i, :])

plt.show()