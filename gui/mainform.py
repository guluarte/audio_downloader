# -*- coding: utf-8 -*-
import wx


class MainForm(wx.Frame):

    def __init__(self, parent, title, model):
        style = style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
        super(MainForm, self).__init__(parent, title=title,size=(400, 300), style = style)
        self.model = model
        self.InitUI()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(8)

        label_base_url = wx.StaticText(panel, label='Base URL:')
        label_base_url.SetFont(font)
        sizer.Add(label_base_url, flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)

        self.text_box_base_url = wx.TextCtrl(panel)
        sizer.Add(self.text_box_base_url,flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.BOTTOM, border=5)


        label = wx.StaticText(panel, label='List of words, one per line:')
        label.SetFont(font)
        sizer.Add(label,flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)

        self.text_box = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        self.text_box.SetFont(font)
        self.text_box.Refresh()

        sizer.Add(self.text_box, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        self.button_download = wx.Button(panel, label='Download')
        self.button_download.Bind(wx.EVT_BUTTON, self.OnDownload)
        sizer.Add((-1,25))
        sizer.Add(self.button_download, flag=wx.ALIGN_RIGHT, border=10)

        sizer.Add((-1,10))

        panel.SetSizerAndFit(sizer)

    def set_base_url(self, base_url):
        self.text_box_base_url.SetValue(base_url)

    def ShowMessage(self):
        wx.MessageBox('Download completed', 'Info', wx.OK|wx.ICON_INFORMATION)


    def OnDownload(self, e):

        self.button_download.Enable(False)
        words_text = self.text_box.GetValue()
        words_not_downloaded = list()
        words = words_text.split('\n')
        len_words_text = len(words_text)
        if len_words_text > 0:
            for word in words:
                try:
                    self.model.download(word)
                except:
                    print 'error'
                    words_not_downloaded.append(word)

        else:
            wx.MessageBox('Enter some words', 'Info', wx.OK | wx.ICON_INFORMATION)
        self.button_download.Enable(True)

        if len(words_not_downloaded) > 0:
            wx.MessageBox('Some words couln\'t be downloaded', 'Info', wx.OK | wx.ICON_ERROR)
        elif len_words_text > 0:
            wx.MessageBox('Download complete!', 'Info', wx.OK | wx.ICON_INFORMATION)

        self.text_box.SetValue('\n'.join(words_not_downloaded))


