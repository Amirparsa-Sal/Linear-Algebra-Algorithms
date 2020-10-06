import numpy as np 

class RowReductionHandler():

	def __init__(self, aug_matrix):
		self.pivot_positions = []
		self.aug_matrix = aug_matrix
		self.rows_num = aug_matrix.shape[0]
		self.cols_num = aug_matrix.shape[1]

	def interchange_row(self,row1,row2):
		for i in range(self.cols_num):
			self.aug_matrix[row1,i],self.aug_matrix[row2,i] = self.aug_matrix[row2,i],self.aug_matrix[row1,i]

	def scale_row(self,row,scale):
		self.aug_matrix[row]*=scale

	def replacement_row(self,row1,row2,col=0):
		if self.aug_matrix[row2,col] == 0:
			return
		self.aug_matrix[row1] -= self.aug_matrix[row1,col]/self.aug_matrix[row2,col] * self.aug_matrix[row2]

#Getting input
rows,cols = list(map(int, input("Please enter number of rows and columns respectively:\n> ").split(" ")))
aug_matrix = np.zeros((rows,cols))
for i in range(rows):
	row = list(map(float, input(f"Please enter row {i+1}:\n> ").split(" ")))
	for j in range (len(row)):
		aug_matrix[i][j] = row[j]

constants = list(map(int, input("Please enter constant values:\n> ").split(" ")))
aug_matrix=np.hstack((aug_matrix, np.array(constants).reshape(-1,1)))

#Start row reduction

handler = RowReductionHandler(aug_matrix)
print(handler.aug_matrix)
handler.interchange_row(0,1)
print(handler.aug_matrix)
handler.scale_row(0,2)
print(handler.aug_matrix)
handler.replacement_row(1,0,0)
print(handler.aug_matrix)