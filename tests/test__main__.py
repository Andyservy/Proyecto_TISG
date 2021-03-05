import wx

class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        panel = wx.Panel(self)

        # left panel
        lPan = wx.Panel(panel)
        lPan.SetBackgroundColour('#9C4141')
        lPan.Bind(wx.EVT_LEFT_DOWN, lambda e, p='left': self.onLeftDown(e, p))
        lPan.Bind(wx.EVT_LEFT_UP, lambda e, p='left': self.onLeftUp(e, p))

        # right panel
        rPan = wx.Panel(panel)
        rPan.SetBackgroundColour('#415C9C')
        rPan.Bind(wx.EVT_LEFT_DOWN, lambda e, p='right': self.onLeftDown(e, p))
        rPan.Bind(wx.EVT_LEFT_UP, lambda e, p='right': self.onLeftUp(e, p))

        # box sizer
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(lPan, 1, flag=wx.EXPAND)
        hbox.Add(rPan, 1, flag=wx.EXPAND)
        panel.SetSizer(hbox)

        self.Show()

    def onLeftDown(self, e, panel):
        print('Mouse down on {} panel'.format(panel))

    def onLeftUp(self, e, panel):
        print('Mouse up on {} panel'.format(panel))

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Down and Up click', size=(200, 150))
    app.MainLoop()