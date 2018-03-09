import math
import collections
from sklearn.cluster import KMeans


def centroid_locator(X, stopping_criterion, initial_clusters):
    # Priming loop
    i = initial_clusters
    old_inertia = math.inf
    inertia_history = []
    k_history = []
    # stopping_criterion = 0.15

    while True:

        # Initializing KMeans
        kmeans = KMeans(n_clusters=i)

        # Fitting with inputs
        kmeans = kmeans.fit(X)

        # if the difference is less than a ratio of our current inertia,
        # select k
        if old_inertia - kmeans.inertia_ < stopping_criterion * kmeans.inertia_:
            break

        old_inertia = kmeans.inertia_
        k_history.append(i)
        inertia_history.append(old_inertia)

        i = i + 1

    cluster_count = collections.Counter(kmeans.labels_)
    clusters = cluster_count.most_common(i)
    centroids = [kmeans.cluster_centers_[cluster[0]] for cluster in clusters]
    centroids = [[int(round(x)), int(round(y))] for x, y in centroids]

    return centroids
