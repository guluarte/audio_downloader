# -*- coding: utf-8 -*-
from gui.mainform import MainForm
from model.downloader import Downloader

import wx

def main():
    global app
    base_url = 'http://www.howjsay.com/mp3/'
    model = Downloader(base_url)
    app = wx.App()
    #downpatrick.mp3
    MainForm(None, title='Howjsay Downloader', model=model).set_base_url(base_url)
    app.MainLoop()


if __name__ == '__main__':
    main()