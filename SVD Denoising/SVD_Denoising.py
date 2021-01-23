import matplotlib.pyplot as plt
import numpy as np

'''This function is used to plot singular values to find breaking point.
	because of similarity between red,green and blue diagrams, I assume a particular K for all 3 color channels that is k = 13
'''
def plot_singular_values(S):
	x = [i for i in range(S.shape[0])]
	y = [value for value in S]
	plt.figure()
	plt.plot(x,y,'b')
	plt.show()

#This function is used to fill new diagonal matrixes we need.
def fill_diag(mat, k, new_shape):
	new_mat = np.zeros((new_shape[0],new_shape[1]))
	for i in range(k+1):
		new_mat[i][i] = mat[i]	
	return new_mat


img = plt.imread('noisy.jpg',)

#Getting picture data
width = img.shape[0]
height = img.shape[1]
red_matrix = img[:,:,0]
green_matrix = img[:,:,1]
blue_matrix = img[:,:,2]

#Finding SVD factorization
Ur,Sr,Vhr = np.linalg.svd(red_matrix)
Ug,Sg,Vhg = np.linalg.svd(green_matrix)
Ub,Sb,Vhb = np.linalg.svd(blue_matrix)

#Making new matrixes using k = 13
k = 13
new_Sr = fill_diag(Sr,k,(width,height))
new_Sg = fill_diag(Sg,k,(width,height))
new_Sb = fill_diag(Sb,k,(width,height))
new_red = np.matmul(np.matmul(Ur,new_Sr),Vhr)
new_green = np.matmul(np.matmul(Ug,new_Sg),Vhg)
new_blue = np.matmul(np.matmul(Ub,new_Sr),Vhb)
new_img = np.zeros((width,height,3),dtype=np.uint8)
for i in range(width):
	for j in range(height):
		new_img[i,j,0] = new_red[i,j]
		new_img[i,j,1] = new_green[i,j]
		new_img[i,j,2] = new_blue[i,j]

plt.imsave(f'saved{k}.jpeg',new_img)
