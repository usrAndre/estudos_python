#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 09:32:58 2022

@author: andreluizrodriguesdasilva
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set() # Plot styling


rand = np.random.RandomState(42)

X = rand.rand(10, 2)
plt.scatter(X[:, 0], X[:, 1], s=100);

dist_sq = np.sum((X[:,np.newaxis,:] - X[np.newaxis,:,:]) ** 2, axis=1)

# for eache pair of points, compute differences in their coordinates
differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
differences.shape

# square the coordinate differences
sq_differences = differences ** 2
sq_differences.shape

# sum the coordinate differences to get the squared distance
dist_sq = sq_differences.sum(-1)
dist_sq.shape

'''
Just to double-check what we are doing, we should see that the diagonal of this matrix
(i.e., the set of distances between each point and itself) is all zero:
'''

dist_sq.diagonal()

'''
It checks out! With the pairwise square-distances converted, we can now use np.arg
sort to sort along each row. The leftmost columns will then give the indices of the
nearest neighbors:
'''
nearest = np.argsort(dist_sq, axis=1)
print(nearest)

'''
Notice that the first column gives the numbers 0 through 9 in order: this is due to the
fact that each point’s closest neighbor is itself, as we would expect.
By using a full sort here, we’ve actually done more work than we need to in this case.
If we’re simply interested in the nearest k neighbors, all we need is to partition each
row so that the smallest k + 1 squared distances come first, with larger distances fill‐
ing the remaining positions of the array. We can do this with the np.argpartition
function:
'''
K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)

'''
In order to visualize this network of neighbors, let’s quickly plot the points along with
lines representing the connections from each point to its two nearest neighbors
'''
plt.scatter(X[:, 0],X[:, 1], s=100)
# draw lines from each point to its two nearest neighbors
K = 2

for i in range(X.shape[0]):
    for j in nearest_partition[1, :K+1]:
        # plot a line from X[i] to X[j]
        # use some zip magic to make it happen:
        plt.plot(*zip(X[j], X[i]), color='black')                     