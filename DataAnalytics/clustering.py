from sklearn import cluster

def k_means(M, k, seed=None):
    """
        Computes a k-means clustering algorithm.

        M: matrix to use
        k: number of clusters to find.
        seed: Random number generator seed to use. Optional.
    """

    # tolerance: change of sum of distances to centers = 1e-4
    k_means_obj = cluster.KMeans(n_clusters=k, n_init=1, max_iter=300, tol=1e-4, random_state=seed)
    return k_means_obj.fit_predict(M)

def DBSCAN(M, eps=0.5, min_pts=5, d='euclidean'):
    """
        Performs DBSCAN clustering.

        M: matrix to use
        eps: Epsilon for DBSCAN algorithm, Neighbourhood to find points in
        min_pts: Threshold to consider neighbourhood dense.
        d: Distance metric to use.
    """

    dbscan_obj = cluster.DBSCAN(eps=eps, min_samples=min_pts, metric=d)
    return dbscan_obj.fit_predict(M)
