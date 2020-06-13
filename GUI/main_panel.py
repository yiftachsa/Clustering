from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E


class Panel:

    def __init__(self, master):
        self.master = master
        master.title("K Means Clustering")

        self.total = 0
        self.entered_number = 0

        # self.total_label_text = IntVar()
        # self.total_label_text.set(self.total)
        # self.total_label = Label(master, textvariable=self.total_label_text)

        # Pre-Processing
        self.path_label = Label(master, text="Path to data:")
        vcmd = master.register(self.validate)  # we have to wrap the command
        self.path = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.browse_button = Button(master, text="Browse", command=lambda: self.update(""))
        # Number of clusters k
        self.n_clusters_label = Label(master, text="Number of clusters k:")
        self.n_clusters = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        # Number of runs
        self.n_init_label = Label(master, text="Number of runs:")
        self.n_init = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.pre_process_button = Button(master, text="Pre-process", command=lambda: self.update("add"))
        self.cluster_button = Button(master, text="Cluster", command=lambda: self.update("add"))

        # LAYOUT

        self.path_label.grid(row=0, column=0, sticky=W)
        self.path.grid(row=0, column=1, columnspan=6, sticky=W + E)
        self.browse_button.grid(row=0, column=8, columnspan=2, sticky=W + E)

        self.n_clusters_label.grid(row=1, column=0, sticky=W)
        self.n_clusters.grid(row=1, column=1, columnspan=3, sticky=W + E)

        self.n_init_label.grid(row=2, column=0, sticky=W)
        self.n_init.grid(row=2, column=1, columnspan=3, sticky=W + E)

        self.pre_process_button.grid(row=3, column=1, columnspan=3, sticky=W + E)
        self.cluster_button.grid(row=4, column=1, columnspan=3, sticky=W + E)


    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def browse(self, path):
        print('browse')

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else:  # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)


root = Tk()
my_gui = Panel(root)
root.mainloop()
