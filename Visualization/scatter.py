import matplotlib.pyplot as plt
import numpy as np


def plot_scatter(data_frame, x_name, y_name, x_label, y_label, title, color_by_name, output_path):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.scatter(data_frame[x_name], data_frame[y_name],
                c=data_frame[color_by_name])  # df['Social support'], df['Generosity'])
    plt.draw()
    plt.savefig(output_path + '/scatter.png', bbox_inches='tight')
    # plt.show()
