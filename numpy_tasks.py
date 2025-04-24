import numpy as np

def uniform_intervals(a, b, n):
    return np.linspace(a, b, n+1)

def cyclic123_array(n): 
    return np.tile([1, 2, 3], n)

def first_n_odd_number(n):
    return np.arange(1, 2*n, 2)

def zeros_array_with_border(n):
    A = np.zeros((n, n))
    A[0, :] = 1
    A[-1, :] = 1
    A[:, 0] = 1
    A[:, -1] = 1
    return A

def chess_board(n):
    return (np.indices((n, n)).sum(axis=0) % 2)

def matrix_with_sum_index(n):
    return np.indices((n, n)).sum(axis=0)

def cos_sin_as_two_rows(a, b, dx):
    x = np.arange(a, b, dx)
    cos_values = np.cos(x)
    sin_values = np.sin(x)
    return np.vstack((cos_values, sin_values))

def compute_mean_rowssum_columnssum(A):
    mean = np.mean(A)
    row_sums = np.sum(A, axis=1)
    col_sums = np.sum(A, axis=0)
    return mean, row_sums, col_sums

def sort_array_by_column(A, j):
    return A[A[:, j].argsort()]

def compute_integral(a, b, f, dx, method):
    x = np.arange(a, b, dx)
    y = f(x)
    
    if method == 'rectangular':
        return np.sum(y) * dx
    
    elif method == 'trapezoidal':
        return np.sum((y[:-1] + y[1:]) * dx / 2)
    
    elif method == 'simpson':
        return (dx / 3) * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]) + y[-1])
    
    else:
        raise ValueError("Неизвестный метод. Выберите 'rectangular', 'trapezoidal' или 'simpson'.")


