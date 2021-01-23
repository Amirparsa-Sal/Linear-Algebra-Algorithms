from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math


def get_main_function():
    x = np.linspace(0, math.pi * 3 / 2, 30)
    y = np.linspace(0, math.pi * 3 / 2, 30)
    X, Y = np.meshgrid(x, y)
    return np.sin(X * Y)


def make_function_noisy(z):
    max_noise = 0.1
    t = 2 * np.random.rand(30 * 30) * max_noise - max_noise
    t = t.reshape(30, 30)
    return np.add(z, t)


def get_function():
    return make_function_noisy(get_main_function())


def show_my_matrix(Z):
    x = np.linspace(0, math.pi * 3 / 2, 30)
    y = np.linspace(0, math.pi * 3 / 2, 30)
    X, Y = np.meshgrid(x, y)
    ax = plt.axes(projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='black')
    ax.set_title('surface');
    ax.view_init(60, 35)
    plt.show()


def show_main():
    Z = get_main_function()
    show_my_matrix(Z)


def show_noisy():
    Z = get_function()
    show_my_matrix(Z)

#This function is used to fill new diagonal matrixes we need.
def fill_diag(mat, k, new_shape):
    new_mat = np.zeros((new_shape[0],new_shape[1]))
    for i in range(k+1):
        new_mat[i][i] = mat[i]  
    return new_mat

k = 8
z = get_function()
U,S,Vh = np.linalg.svd(z)
new_S = fill_diag(S,k,(z.shape[0],z.shape[1]))
new_z = np.matmul(np.matmul(U,new_S),Vh)
show_my_matrix(new_z)
