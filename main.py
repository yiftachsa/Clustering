from pre_processing import preprocess as pp
from Cluster import KMeans
from Visualization import scatter
from Visualization import maps

#TODO: start GUI model

df ={}#dataframe

def pre_process():
    global df
    df = pp.preprocess(
    "D:\\Documents\\Studies\\Documents for higher education\\Courses\\Year 3 Semester 2\\מדעי הנתונים ובינה עסקית\\עבודות להגשה\\תרגיל 4\\Dataset.xlsx") #TODO: Receive from GUI model

    print("Preprocessing completed successfully!")  # TODO: print to GUI

def cluster():
    global df
    n_clusters = 3  # default=8 TODO: Receive from GUI model
    n_init = 10  # default=10 TODO: Receive from GUI model

    df = KMeans.k_means_cluster(df, n_clusters, n_init)
    # TODO: Check if the real values are needed for display(and not after standardization) if so - write another function in pre-process with out the standardization line.
    scatter.plot_scatter(df, 'Social support', 'Generosity', 'Social support', 'Generosity', 'Generosity in dependence of Social support', 'cluster')


pre_process()
cluster()
maps.plot_choropleth_map(df)

