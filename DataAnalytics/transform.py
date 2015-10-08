import numpy
import matplotlib.mlab

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
