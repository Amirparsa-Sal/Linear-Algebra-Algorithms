from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog,Tk
import matplotlib.pyplot as plt 

def get_input():
	y = float(input("Please enter shear lambda: "))
	print("Select your image: ")
	window = Tk()
	window.withdraw()
	file_name = filedialog.askopenfilename()
	window.destroy()
	return (y,file_name)

def gray_mask(matrix):
	height  = matrix.shape[0]
	width = matrix.shape[1]
	gray_matrix = np.full((height,width,3), 255)
	for i in range(height):
		for j in range(width):
			if not np.all(matrix[i][j] == [255,255,255]):
				gray_matrix[i,j,:] = 40
	return gray_matrix

def shear(matrix, y):
	height = matrix.shape[0]
	width = matrix.shape[1]
	sheared = np.full((height, int(width + y * height), 3), 255)
	for i in range(height):
		for j in range(width):
			if not np.all(matrix[i][j] == [255,255,255]):
				sheared[i, int(j + y * i) , :] = 40
	return sheared

def replace_pixels(gray_matrix, matrix):
	height = matrix.shape[0]
	width = matrix.shape[1]
	for i in range(height):
		for j in range(width):
			if np.all(matrix[i][j] == [255,255,255]):
				if np.all(gray_matrix[i][j] == [40,40,40]):
					matrix[i,j,:] = 40
	return matrix

y,filename = get_input()
matrix = np.array(Image.open(filename))
gray_matrix = gray_mask(matrix)
sheared_gray = shear(matrix, y)
sheared = replace_pixels(sheared_gray,matrix)
plt.figure()
plt.imshow(sheared)
plt.show()