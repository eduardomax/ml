import math
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # <--- This is important for 3d plotting 
from matplotlib import cm
import numpy as np

class Regression:
	def __init__(self, X, y, alfa=0.001):
		self.theta = [4,6] #random numbers
		self.X = X
		self.y = y
		self.alfa = alfa

	def h(self, x): #h(x) = T_0 + T_1*x
		return self.theta[0] + self.theta[1]*x

	def dJ(self, ntheta=None): #derivada de J
		soma = 0
		for i in range(len(self.X)):
			aux = self.h(self.X[i]) - self.y[i] #h(x_i) - y_id
			if (ntheta == 1):
				aux = aux*self.X[i]
			soma = soma + aux

		return soma/len(self.X)

	def J(self): #J(T_0, T_1)
		soma = 0
		for i in range(len(self.X)):
			aux = math.pow(self.h(self.X[i]) - self.y[i], 2)
			soma = soma + aux

		return soma/(len(self.X)*2)

	def Jmod(self, theta_i, theta_j):
		soma = 0
		for i in range(len(self.X)):
			aux = math.pow(theta_i + theta_j*self.X[i] - self.y[i], 2)
			soma = soma + aux

		return soma/(len(self.X)*2)

	def train(self, interacoes):
		for i in range(interacoes):
			erro0 = self.alfa*self.dJ(0)
			erro1 = self.alfa*self.dJ(1)
			temp0 = self.theta[0] - erro0
			temp1 = self.theta[1] - erro1
			self.theta[0] = temp0
			self.theta[1] = temp1
			print('erro: ', self.J())
		print('theta0: ', self.theta[0])
		print('theta1: ', self.theta[1])

def plotGraph(regression):
	x = []
	y = []
	z = []
	for theta_i in range(20):
		for theta_j in range(20):
			x.append(theta_i)
			y.append(theta_j)
			z.append([regression.Jmod(theta_i, theta_j)])
	
	fig = plt.figure()
	ax = plt.axes(projection='3d')
	ax.scatter(x, y, np.asarray(z), depthshade=True, cmap='viridis' )
	plt.show()

if __name__=="__main__":
	A = open('ex2x.dat','r')
	B = open('ex2y.dat','r')

	X = []
	y = []

	for line in A:
		X.append(float(line))
	for line in B:
		y.append(float(line))

	reta = Regression(X, y)
	reta.train(100)

	plotGraph(reta)
