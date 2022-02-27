import sys
import numpy as np

# Taking number of unknowns from user
n = int(input('Enter number of unknowns: '))
# Array initialized with zeroes to store the matrix and its size = n * n + 1
x = np.zeros((n , n + 1))
# Array initialized with zeroes to store the solution and its size = n
y = np.zeros(n)

# Take matrix coefficients from user one by one
print('Enter Matrix Coefficients one by one : ')
for i in range(n):
    for j in range(n + 1):
        x[i][j] = float(input( 'x['+ str(i) + '][' + str(j) +'] = '))

# Gauss Elimination Algorithm
for i in range(n):
    if x[i][i] == 0.0:
        sys.exit('Runtime Error: Division By Zero')
    for j in range(i + 1 , n):
        ratio = x[j][i] / x[i][i]
        for k in range(n + 1):
            x[j][k] = x[j][k] - ratio * x[i][k]

# Back Substitution
y[n - 1] = x[n - 1][n] / x[n - 1][n - 1]
for i in range(n - 2 , -1 , -1):
    y[i] = x[i][n]
    for j in range(i + 1 , n):
        y[i] = y[i] - x[i][j] * y[j]
    y[i] = y[i] / x[i][i]

# Showing the result
print('\nThe solution is: ')
for i in range(n):
    print("Y{:d} = {:0.2f}".format(i , y[i]) , end = "     ")