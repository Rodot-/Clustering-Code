# Clustering-Code
Repository to Hold onto Various Clustering Tools.

##Contents
###kmeans.py
----
K-Means Clustering Code.

####Methods:

#####comparison(data, means):

  How the data is clustered.  Computes the euclidian distance between a data point and each mean, then finds the minimum.  Using the argmin function, this method finds the minimum for every point in data and returns an array of cluster indecies.  Cluster indecies are values whose index matches an index in data and whose values designate the cluster to which it belongs.
  
  Returns: clusters, means

#####kmeans(data, means):

  Basic K-means clustering method.  Takes in an NxM matrix of data points, and an KxM matrix of means.  Returns a list of K subsets of data (i.e. clusters), each subset is of the same form as data.

#####kmeans_struct(data, means):

  This works similarly to kmeans, but instead of a matrix input, this method takes numpy structured arrays.  The data and means must have the same dtype.   Returns a list of K subsets of data (clusters), each with the same dtype as data.

  Returns: clusters, means

#####arg_[METHOD]

  Any method beginning with 'arg_' returns the array of cluster indecies rather than the clusters themselves.  Useful for clustering data sets in which all columns do not need to be clustered.
  
  Returns: cluster indecies, means
  
####Examples:

    >>> from kmeans import *
    >>> import numpy as np
    >>> Data = np.arange(50).reshape((10,5))
    >>> Means = np.arange(15).reshape((3,5))
    >>> Means
    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14]])
    >>> clusters, means = kmean(Data, Means)
    >>> clusters.shape
    (3,)
    >>> clusters[0]
    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14]])
    >>> means.shape
    (3, 5)
    >>> means
    array([[  5. ,   6. ,   7. ,   8. ,   9. ],
           [ 20. ,  21. ,  22. ,  23. ,  24. ],
           [ 37.5,  38.5,  39.5,  40.5,  41.5]])

  

