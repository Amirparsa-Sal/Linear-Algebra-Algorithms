import numpy as np 

class RowReductionHandler():

	def __init__(self, aug_matrix):
		self.pivot_positions = []
		self.aug_matrix = aug_matrix
		self.rows_num = aug_matrix.shape[0]
		self.cols_num = aug_matrix.shape[1]

	def interchange_row(self,row1,row2):
		if row1 == row2:
			return
		for i in range(self.cols_num):
			self.aug_matrix[row1,i],self.aug_matrix[row2,i] = self.aug_matrix[row2,i],self.aug_matrix[row1,i]

	def scale_row(self,row,scale):
		self.aug_matrix[row]*=scale

	def replacement_row(self,row1,row2,col=0):
		if self.aug_matrix[row2,col] == 0:
			return
		self.aug_matrix[row1] -= self.aug_matrix[row1,col]/self.aug_matrix[row2,col] * self.aug_matrix[row2]

	def is_zero(self, arr):
		for num in arr:
			if num != 0:
				return False
		return True

	def find_pivot_column(self, starting_row=0, starting_col=0):
		for i in range(starting_col,self.cols_num):
			if not self.is_zero(self.aug_matrix[starting_row:,i]):
				return i
		return -1

	def find_absolute_max_in_column(self, col,starting_row=0):
		max_num = self.aug_matrix[:,col][starting_row]
		index = starting_row
		for i in range(starting_row,self.rows_num):
			number = self.aug_matrix[:,col][i]
			if abs(number)>abs(max_num):
				max_num = number
				index = i
		return index
	
	def do_forward_phase(self, starting_row=0, starting_col=0):
		pivot_col = self.find_pivot_column(starting_row,starting_col)
		if pivot_col!=-1:
			self.pivot_positions.append((starting_row,pivot_col))
			if starting_row == self.rows_num-1 or pivot_col == self.cols_num-1:
				return
			max_index = self.find_absolute_max_in_column(pivot_col,starting_row)
			self.interchange_row(starting_row,max_index)
			for i in range(starting_row+1,self.rows_num):
				self.replacement_row(i,starting_row,pivot_col)
			self.do_forward_phase(starting_row+1,starting_col+1)

	def do_backward_phase(self):
		for i in range(len(self.pivot_positions)-1,-1,-1):
			pivot = self.pivot_positions[i]
			row = pivot[0]
			col = pivot[1]
			num = self.aug_matrix[row,col]
			if num!=1:
				self.scale_row(row,1/num)
			for i in range(row-1,-1,-1):
				self.replacement_row(i,row,col)	

	def run(self):
		self.do_forward_phase()
		self.do_backward_phase()

	def has_answer(self):
		for pivot in self.pivot_positions:
			if pivot[1] == self.cols_num-1:
				return False
		return True

	def show_result(self):
		if not self.has_answer():
			print("The system has no answer!")
		else:
			for i in range(self.cols_num-1):
				if i<self.rows_num and self.aug_matrix[i,i]==1:
					asnwer=""
					other_cols = [j for j in range(self.cols_num-1) if j!=i]
					print(f"X{i+1} = {self.aug_matrix[i,-1]}",end="")
					for j in other_cols:
						cof = self.aug_matrix[i,j]
						if cof>0:
							asnwer += f" - {cof}X{j+1}"
						elif cof<0:
							asnwer += f" + {abs(cof)}X{j+1}"
				else:
					print(f"X{i+1} is a free variable")

# Getting input
rows,cols = list(map(int, input("Please enter number of rows and columns respectively:\n> ").split(" ")))
aug_matrix = np.zeros((rows,cols))
for i in range(rows):
	row = list(map(float, input(f"Please enter row {i+1}:\n> ").split(" ")))
	for j in range (len(row)):
		aug_matrix[i][j] = row[j]
constants = list(map(int, input("Please enter constant values:\n> ").split(" ")))
aug_matrix=np.hstack((aug_matrix, np.array(constants).reshape(-1,1)))
# Run algorithm
handler = RowReductionHandler(aug_matrix)
handler.run()
print(handler.aug_matrix)
handler.show_result()