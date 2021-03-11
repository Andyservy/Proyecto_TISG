# Packages Third-party
import wx

# Package Project



class frame_main(wx.Dialog):
    def __init__(self, parent, title, size):
        super(frame_main, self).__init__(parent, title=title, size=size)
        self.Centre()
        self.GUIinit()

    def GUIinit(self):

        button = wx.Button(self, -1, "Andy")
        button.Bind(wx.EVT_BUTTON, self.OnClik)

    def OnClik(self, event):
        pass


class ventana(wx.Frame):
    def __init__(self, parent, title, size):
        super(ventana, self).__init__(parent, title=title, size=size)

        Andy = frame_main(self, "perro", (200, 200))
        Andy.ShowModal()


def main():
    app = wx.App()

    Formulario = ventana(None, title='Boost Manager', size=(500, 300))

    app.MainLoop()

if __name__ == '__main__':
    main()
