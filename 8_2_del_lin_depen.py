import numpy as np

def remove_linear_dependent_rows(matrix):
    matrix = np.array(matrix)
    rref, _ = np.linalg.qr(matrix.T, mode='r')
    rref = rref.T
    pivot_cols = np.flatnonzero(np.max(np.abs(rref), axis=1))
    return matrix[:, pivot_cols].tolist()
