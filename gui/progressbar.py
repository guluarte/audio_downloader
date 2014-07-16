import wx

class Progressbar(wx.Frame):
    def __init__(self, max):
        style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
        wx.Frame.__init__(self, None, -1, 'Downloading', size=(350, 150), style=style)
        panel = wx.Panel(self)
        self.count = 0
        self.max = max
        self.gauge = wx.Gauge(panel, -1, self.max, size=(250, 25))
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(8)
        self.label = wx.StaticText(panel, label='Downloading')
        self.label.SetFont(font)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.label, flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(self.gauge, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        panel.SetSizer(vbox)

        self.Refresh()


    def step(self):
        self.count += 1
        self.gauge.SetValue(self.count)

    def set_label(self, label):
        self.label.SetLabel(label)
