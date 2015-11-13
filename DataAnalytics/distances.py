import numpy as np
from scipy.spatial.distance import pdist, cdist, cosine, squareform

def order_by_distance(v, A, d=None):
    """
        Returns a list of indexes sorted by distance to a vector.

        v: Vector to compute distance from
        A: List of vectors (matrix) to compute distacnes from.
        d: Distance Function (metric) to use. Defaults to cosine.
    """

    # default to the cosine matrix
    if d == None:
        d = cosine

    # compute distances
    distances = [d(v, a) for a in A]

    # and sort by it
    return np.argsort(distances)

def pairwise_euclidean_distance(M, axis=0):
    """
        Returns a square matrix of pairwise euclidean distances of elements
        within a matrix.

        M: Matrix to compute distances in.
        axis: Axis to compute distance against. Defaults to 0.
    """

    return pairwise_distance(M, 'euclidean', axis=axis)

def pairwise_cosine_distance(M, axis=0):
    """
        Returns a square matrix of pairwise cosine distances of elements
        within a matrix.

        M: Matrix to compute distances in.
        axis: Axis to compute distance against. Defaults to 0.
    """

    return pairwise_distance(M, 'cosine', axis=axis)

def pairwise_distance(M, d, axis=0):
    """
        Returns a square matrix of pairwise distances of elements
        within a matrix.

        M: Matrix to compute distances in.
        d: Distance metric to apply.
        axis: Axis to compute distance against. Defaults to 0.
    """

    return squareform(pdist(M if axis==0 else M.T, d))
