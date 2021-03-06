# -*- coding: utf-8 -*-
import wx
from org.bysun.apkreader import GUI

modules ={u'GUI': [1, 'Main frame of Application', u'GUI.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = GUI.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
