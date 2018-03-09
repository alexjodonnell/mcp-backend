import numpy as np
import math
import matplotlib.pyplot as plt
import collections
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

def cnetroid_locator(X, stopping_criterion, initial_clusters):
    # Priming loop
    # i = 3
    old_inertia = math.inf;
    inertia_history = []
    k_history = []
    # stopping_criterion = 0.15

    while True:

        # Initializing KMeans
        kmeans = KMeans(n_clusters=i)

        # Fitting with inputs
        kmeans = kmeans.fit(X)

        # Predicting the clusters
        labels = kmeans.predict(X)

        # if the difference is less than a ratio of our current inertia,
        # select k
        if old_inertia - kmeans.inertia_ < stopping_criterion * kmeans.inertia_:
            C = kmeans.cluster_centers_
            fig = plt.figure()
            plt.scatter(X[:, 0], X[:, 1], c=y)
            plt.scatter(C[:, 0], C[:, 1], marker='.', c='#050505', s=1000)
            plt.show()
            break

        old_inertia = kmeans.inertia_
        k_history.append(i)
        inertia_history.append(old_inertia)

        i = i + 1

    return kmeans




