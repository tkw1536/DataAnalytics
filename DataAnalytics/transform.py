import numpy
import matplotlib.mlab
from sklearn import manifold

# (c) Tom Wiesing 2015
# licensed under MIT license

def PCA(M,axis=1):
    """
        Applies an unscaled PCA to a matrix.

        M: Matrix to apply PCA to.
        axis: Axis to normalise against. Needs to be either 1 or 0. Defaults to 1.
    """

    # ensure axis is of the right type.
    if axis != 1 and axis != 0:
        raise ValueError("Axis must be 0 or 1")

    # create a matrix P.
    if axis == 1:
        P = M.T
    else:
        P = M

    # compute a PCA object
    pcaobj = matplotlib.mlab.PCA(P,standardize=False)

    # replace each row of the matrix P
    for r in range(P.shape[0]):
        P[r, :] = pcaobj.project(P[r, :])

    # and return the right version.
    if axis == 1:
        return P.T
    else:
        return P

def MDS(M, n, seed=None):
    """
        Applies an (metric) MDS transform to a similarities matrix.

        M: Matrix to tranform.
        n: Dimensionality of embedded space.
    """

    mds_obj = manifold.MDS(n_components=n, dissimilarity="precomputed", random_state=seed)
    return mds_obj.fit_transform(M)

def NMDS(M, n, seed=None):
    """
        Applies an nonmetric MDS transform to a similarities matrix.

        M: Matrix to tranform.
        n: Dimensionality of embedded space.
        seed: Random number generator seed to use. Optional.
    """

    mds_obj = manifold.MDS(metric=False, n_init=1, n_components=n, dissimilarity="precomputed", random_state=seed)
    return mds_obj.fit_transform(M)

def permute(M,sigma,axis=1):
    """
        Reorders data items according to a permutation sigma.

        M: Matrix to apply PCA to.
        sigma: Permutation of the attributes of M.
        axis: Axis to permute against. Needs to be either 1 or 0. Defaults to 1.
    """

    if axis == 1:
        P = M.T
    else:
        P = M

    Q = numpy.zeros(P.shape)

    for r in range(P.shape[1]):
        print(r, sigma[r])
        Q[:, r] = P[:, sigma[r]]

    if axis == 1:
        return Q.T
    else:
        return Q
