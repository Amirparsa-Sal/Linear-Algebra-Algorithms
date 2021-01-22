import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def get_matrix(data_frame):
	data_size = data_frame.size
	mat = np.zeros((data_size,2))
	for i in range(data_size):
		mat[i,0] = i;
		mat[i,1] = data_frame.iloc[i,0];
	return mat

def find_less_min_square(A,B):
	return np.linalg.solve(np.matmul(A.T,A),np.matmul(A.T,B))

def calc_error(A,X,expected_y):
	return np.matmul(A,X) - expected_y


def show_result(A,X,Y,err,size):

	for i in range (size-10,size):
		print(f'Day {int(A[i,1])}')
		print(f'Calculated Value: {X[i,0]}')
		print(f'Actual Value: {Y[i,0]}')
		print(f'error: {err[i,0]}')
	print("---------------------------------------")
	days = [i for i in range(size)]
	plt.figure()
	plt.plot(days,Y,'ro')
	plt.plot(days,X,'b')
	plt.show()

#Reading database
data_frame = pd.read_csv("GOOGL.csv", usecols=['Open']);
data_size = data_frame.size
matrix = get_matrix(data_frame)
y_matrix = matrix[:data_size,1].reshape(-1,1)

#Calculating linear solution
print('Calculating linear solution:')
linear_x_matrix = np.hstack((np.ones((data_size,1)), matrix[:data_size,0].reshape(-1,1)));
linear_solution = find_less_min_square(linear_x_matrix[:data_size-10], y_matrix[:data_size-10])
linear_err = calc_error(linear_x_matrix, linear_solution, y_matrix)
linear_estimated_values = np.matmul(linear_x_matrix, linear_solution)
show_result(linear_x_matrix, linear_estimated_values, y_matrix, linear_err, data_size)

#Calculating Polynomial solution
print('Calculating Polynomial solution:')
polynomial_x_matrix = np.hstack((np.ones((data_size,1)), matrix[:data_size,0].reshape(-1,1),matrix[:data_size,0].reshape(-1,1)**2));
polynomial_solution = find_less_min_square(polynomial_x_matrix[:data_size-10], y_matrix[:data_size-10])
polynomial_err = calc_error(polynomial_x_matrix, polynomial_solution, y_matrix)
polynomial_estimated_values = np.matmul(polynomial_x_matrix, polynomial_solution)
show_result(polynomial_x_matrix, polynomial_estimated_values, y_matrix, polynomial_err, data_size)

print(f'Total linear error: {np.sum(np.abs(linear_err))}')
print(f'Total polynomial error: {np.sum(np.abs(polynomial_err))}')
