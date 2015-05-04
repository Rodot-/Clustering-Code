from numpy import argmin, array, empty, mean, sum  



def comparison(data, means): #Method by which we cluster

	return argmin([sum((point - means)**2, axis = 1) for point in data], axis = 1)

def kmeans(data, *means): #Kmeans clustering function

	K = len(means)
	old_means = array(means)*0
	means = array(means)
	data = array(data)
	clusters = empty(len(data), dtype = '>i4') #An array of cluster indecies
	while (old_means != means).any(): #Keep going until no change.
		clusters[0:] = comparison(data, means)
		old_means = means
		means = array([mean(data[clusters == i], axis = 0) for i in xrange(K)])
		print "".join(( '\033[93m',"".join(('|' for i in xrange(K))))),'\033[92m','\033[0m' #prints bars indicating K for multi processing.
	return array([data[clusters == i] for i in xrange(K)]), means

def kmeans_generator(data, *means): #Kmeans clustering function as a generator for each step.  Used to observe progress of clustering code.

	K = len(means)
	old_means = array(means)*0
	means = array(means)
	data = array(data)
	clusters = empty(len(data), dtype = '>i4')
	while (old_means != means).any():
		clusters[0:] = comparison(data, means)
		old_means = means
		means = array([mean(data[clusters == i], axis = 0) for i in xrange(K)])
		yield {'clusters':array([data[clusters == i] for i in xrange(K)]), 'means':means}


