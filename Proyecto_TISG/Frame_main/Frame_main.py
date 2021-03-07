import wx


class Frame_main(wx.Frame):
    def __init__(self, parent, title, size):
        super(Frame_main, self).__init__(parent, title=title, size=size)
        self.Show()
        self.Centre()
