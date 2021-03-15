import wx
import wx.lib.masked as masked

########################################################################
class MyPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        control = ["Phone No", "(###) ###-#### x:###", "", 'F^-', "^\(\d{3}\) \d{3}-\d{4}", '','','']
        maskText = masked.TextCtrl(self, 
                                   mask = control[1],
                                   excludeChars = control[2],
                                   formatcodes  = control[3],
                                   includeChars = "",
                                   validRegex   = control[4],
                                   validRange   = control[5],
                                   choices      = control[6],
                                   choiceRequired = True,
                                   defaultValue = control[7],
                                   demo         = True,
                                   name         = control[0],
                                   style=wx.TE_PROCESS_ENTER)
        maskText.Bind(wx.EVT_KEY_DOWN, self.onEnter)

    #----------------------------------------------------------------------
    def onEnter(self, event):
        """"""
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER: 
            print ("you pressed ENTER!")
        event.Skip()

########################################################################
class MyFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Masked!")
        panel = MyPanel(self)
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()