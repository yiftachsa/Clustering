import matplotlib.pyplot as plt
import numpy as np


def plot_scatter(data_frame, x_name, y_name, x_label, y_label, title, color_by_name):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.scatter(data_frame[x_name],data_frame[y_name], c=data_frame[color_by_name]) #df['Social support'], df['Generosity'])
    figure = plt.figure()
    plt.show() #TODO: sholud show or return the plot?
    return figure
