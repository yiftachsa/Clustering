from sklearn.cluster import KMeans


def k_means_model(data_frame, num_clusters, num_init):
    model = KMeans(n_clusters=num_clusters, n_init=num_init, init='random')
    model.fit(data_frame.loc[:, data_frame.columns != 'country'])
    return model.labels_

def k_means_cluster(data_frame, num_clusters, num_init):
    clusters = k_means_model(data_frame, num_clusters, num_init)
    data_frame['cluster'] = clusters
    return data_frame


