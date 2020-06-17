import wx, os
import main as currmain

pathData = ""
cluster = 0
runs = 0
flag = False
cluster_button = 0


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.InitMainPanel()
        self.SetSize((1400, 800))
        self.SetTitle('K Means Clustering')
        self.Center()
        self.Show(True)

    def InitMainPanel(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(vbox)

        # add main widgets
        widgets = self.loadWidgets(panel)
        fgs = wx.FlexGridSizer(rows=len(widgets), cols=2, vgap=10, hgap=15)
        fgs.AddMany([(widget) for widget in widgets])
        vbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=20)

        # pre process
        button_box = wx.BoxSizer(wx.HORIZONTAL)
        pre_button = wx.Button(panel, label='Pre-process', size=(100, 30))
        button_box.Add(pre_button, flag=wx.RIGHT)
        vbox.Add(button_box, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        pre_button.Bind(wx.EVT_BUTTON, self.preProcessFunc)

        # cluster
        global cluster_button
        cluster_button = wx.Button(panel, label='Cluster', size=(100, 30))
        button_box.Add(cluster_button, flag=wx.RIGHT)
        vbox.Add(button_box, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        cluster_button.Bind(wx.EVT_BUTTON, self.clusterFunc)
        cluster_button.Disable();

    def loadWidgets(self, panel):

        widgets = []

        # data file
        fl_ctrl_label = wx.StaticText(panel, label='Path Of Data')
        fl_ctrl = wx.FilePickerCtrl(panel, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition,
                                    wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        fl_ctrl.Bind(wx.EVT_FILEPICKER_CHANGED, self.on_open_file)
        widgets.append(fl_ctrl_label)
        widgets.append(fl_ctrl)

        # number of clusters
        text_cluster_control_label = wx.StaticText(panel, label='Number of clusters k')
        textControlCluster = wx.TextCtrl(panel)
        textControlCluster.Bind(wx.EVT_TEXT, self.catchClusterNumber)
        widgets.append(text_cluster_control_label)
        widgets.append(textControlCluster)

        # number of runs
        text_run_control_label = wx.StaticText(panel, label='Number of runs')
        textControlRun = wx.TextCtrl(panel)
        textControlRun.Bind(wx.EVT_TEXT, self.catchRunNumber)
        widgets.append(text_run_control_label)
        widgets.append(textControlRun)

        return widgets

    # helper functions

    def on_open_file(self, event):
        path = event.GetPath()
        global pathData
        pathData = path;
        return path;

    def catchClusterNumber(self, event):
        sender = event.GetEventObject()
        global cluster
        cluster = sender.GetValue()


    def catchRunNumber(self, event):
        sender = event.GetEventObject()
        global runs
        runs = sender.GetValue()


    def preProcessFunc(self, e):
        try:
            currmain.pre_process(pathData)
        except:
            about_text = 'Please enter valid path'
            dlg = wx.MessageDialog(self, about_text, 'K Means Clustering', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            return False

        about_text = 'Preprocessing completed successfully!'
        dlg = wx.MessageDialog(self, about_text, 'K Means Clustering', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        global cluster_button
        cluster_button.Enable()
        return True



    def clusterFunc(self, e):
        errorMessage = ""
        if (currmain.getDataFrameLength() < int(cluster) or int(cluster) < 3):
            errorMessage += 'Alert: The number of clusters should be smaller than \n the amount of records in the given dataset \n and bigger than 2 \n'
        if (int(runs) > 20 or int(runs) <= 0):
            errorMessage += 'Alert: The number of runs should be a positive integer smaller than 20'
        if (len(errorMessage) != 0):
            dlg = wx.MessageDialog(self, errorMessage, 'K Means Clustering', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            return False

        try:
            pathOfImages = currmain.cluster(cluster, runs)
        except:
            about_text = 'an error have occurred'
            dlg = wx.MessageDialog(self, about_text, 'K Means Clustering', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            return False
        pos = 10
        myobject = e.GetEventObject()
        myobject.Disable()

        # for name png
        pngName = wx.Image(pathOfImages + '/name.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, pngName, (pos, pos), (pngName.GetWidth(), pngName.GetHeight()))

        # for scatter png
        pngScatter = wx.Image(pathOfImages + '/scatter.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, pngScatter, (pos + 800, pos), (pngScatter.GetWidth(), pngScatter.GetHeight()))

        about_text = 'Cluster process finished'
        dlg = wx.MessageDialog(self, about_text, 'K Means Clustering', wx.OK)  # wx.OK|wx.ICON_INFORMATION
        result = dlg.ShowModal()
        dlg.Destroy()
        self.Close()

    def OnQuit(self, e):
        self.Close()


def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()
