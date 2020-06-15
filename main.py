from pre_processing import preprocess as pp
from Cluster import KMeans
from Visualization import scatter
from Visualization import maps
from datetime import datetime
import os
import shutil

# TODO: start GUI model
# datetime string containing current date and time
output_path = ""
df = {}  # dataframe


def pre_process():
    global df
    df = pp.preprocess(
        "D:\\Documents\\Studies\\Documents for higher education\\Courses\\Year 3 Semester 2\\מדעי הנתונים ובינה עסקית\\עבודות להגשה\\תרגיל 4\\Dataset.xlsx",
        True)  # TODO: Receive from GUI model

    print("Preprocessing completed successfully!")  # TODO: print to GUI


def cluster():
    global df, output_path
    time_stamp = datetime.now().strftime("%d-%m-%Y")
    output_path = os.getcwd() + '/Output/' + time_stamp
    try:
        if (os.path.isdir(output_path)):
            shutil.rmtree(output_path)
        os.mkdir(output_path)
    except OSError:
        print("Creation of the directory %s failed" % output_path)

    n_clusters = 3  # default=8 TODO: Receive from GUI model
    n_init = 10  # default=10 TODO: Receive from GUI model

    df = KMeans.k_means_cluster(df, n_clusters, n_init)
    # TODO: Check if the real values are needed for display(and not after standardization) if so - write another
    #  function in pre-process with out the standardization line.

    scatter.plot_scatter(df, 'Social support', 'Generosity', 'Social support', 'Generosity',
                         'Generosity in dependence of Social support', 'cluster', output_path)
    maps.plot_choropleth_map(df, output_path)
    # TODO: Display results
    # TODO: Display new dialog with "Clustering completed" with an ok button


pre_process()
cluster()

# for Clusters analysis
#
# def clusterGrouping():
#     global df, output_path
#     df_not_normalize = pp.preprocess(
#         "D:\\Documents\\Studies\\Documents for higher education\\Courses\\Year 3 Semester 2\\מדעי הנתונים ובינה עסקית\\עבודות להגשה\\תרגיל 4\\Dataset.xlsx",
#         False)  # TODO: Receive from GUI model
#     df_not_normalize['cluster'] = df['cluster']
#     grouped = df_not_normalize.groupby(['cluster']).mean()
#     grouped.to_csv(output_path + "/grouped.csv")
#
#
# clusterGrouping()
