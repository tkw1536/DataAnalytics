import numpy
import scipy.linalg

# (c) Tom Wiesing 2015
# licensed under MIT license

def normalize(M,I=(0, 1),axis=1):
    """
        Normalises a matrix by rescaling each dimension to a certain interval.

        M: Matrix to normalise.
        I: Interval to scale to. Defaults to (0, 0).
        axis: Axis to normalise against. Needs to be either 1 or 0. Defaults to 1.
    """

    # compute max and min.
    mmax = numpy.max(M,axis=axis)
    mmin = numpy.min(M,axis=axis)

    # compute the shift and rescaling factors.
    shift = I[0]
    fac = I[1] - I[0]

    # shift by axis.
    if axis == 1:
        return fac*( (M - mmin[:,numpy.newaxis]) / (mmax - mmin)[:,numpy.newaxis] ) + shift
    elif axis == 0:
        return fac*( (M - mmin[numpy.newaxis,:]) / (mmax - mmin)[numpy.newaxis,:] ) + shift
    else:
        raise ValueError("Axis must be 0 or 1")

def sphere(M,mean=0,std=1,axis=1):
    """
        Normalises a matrix by rescaling each axis to have a certain mean and standard deviation.

        M: Matrix to normalise.
        mean: Mean to normalise to. Defaults to 0.
        var: Variance to normalise to. Defaults to 1.
        axis: Axis to normalise against. Needs to be either 1 or 0. Defaults to 1.
    """

    # compute mean and variance
    mmean = numpy.mean(M,axis=axis)
    mvar = numpy.var(M,axis=axis)

    if axis == 1:
        return std*( (M - mmean[:,numpy.newaxis]) / (numpy.sqrt(mvar))[:,numpy.newaxis] ) + mean
    elif axis == 0:
        return std*( (M - mmean[numpy.newaxis,:]) / (numpy.sqrt(mvar))[numpy.newaxis,:] ) + mean
    else:
        raise ValueError("Axis must be 0 or 1")

def whitening(M, axis=1):
    """
        Normalises a matrix by ensuring the covariance matrix is the identity.

        M: Matrix to normalise.
        axis: Axis to normalise against. Needs to be either 1 or 0. Defaults to 1.
    """

    # ensure axis is of the right type.
    if axis != 1 and axis != 0:
        raise ValueError("Axis must be 0 or 1")

    # compute the covariance matrix C
    C=numpy.cov(M,rowvar=axis)

    # compute C^{-0.5}
    C_fac = scipy.linalg.inv(scipy.linalg.sqrtm(C))

    # multiply with that factor.
    return numpy.dot(C_fac, M)
