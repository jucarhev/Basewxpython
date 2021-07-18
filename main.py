# -*- coding: utf-8 -*- 
#!/usr/bin/python3

import wx

class main(wx.Frame):
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY)
		favicon = wx.Icon('notebook.ico',wx.BITMAP_TYPE_ICO, 16,16)
		self.SetIcon(favicon)
		self.SetSize((620,530))
		self.SetTitle("Title")
		self.Centre()
		self.Show()

app = wx.App()
main(None)
app.MainLoop()