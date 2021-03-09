import wx

app=wx.App()

frm = wx.Frame(None, title='title')
pan = wx.Panel(frm)

sizer = wx.BoxSizer(wx.HORIZONTAL)
sizer.Add(wx.SpinCtrl(pan))
sizer.Add(wx.SpinCtrl(pan))

pan.SetSizerAndFit(sizer)
frm.Fit()
frm.SetMinSize(frm.GetEffectiveMinSize())
frm.Show()

app.MainLoop()