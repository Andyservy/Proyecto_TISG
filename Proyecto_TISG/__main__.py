import wx

from Proyecto_TISG.Frame_main import frame_main


def main():
    app = wx.App()

    Andy = frame_main(None, title='Boost Manager', size=(1000, 700), colour="#212F3C")
    Andy.Show()

    app.MainLoop()


if __name__ == '__main__':
    main()
"""Llamada a la ventana principal, esta ventana inicia las otras"""
