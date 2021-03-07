# import wx
# from Package import PG
# class Ventana(wx.Frame):
#
#     def __init__(self, parent):
#         super(Ventana, self).__init__(parent)
#         Panel(self)
#
# class Panel(wx.Panel):
#     # noinspection PyCompatibility
#     def __init__(self, parent):
#         super().__init__(parent)
#
#         Boton = wx.Button(self, -1, label="Ok")
#
#         botones = [Boton]
#
#         PG.Btnbicolor(botones, "#212F3C", '#384A5F')
#
#
#         # EVENTO
#
#         Boton.Bind(wx.EVT_BUTTON, self.OnClick)
#
#
#     def OnClick(self, e):
#         print("close")
#
# def main():
#     """Llamada a la ventana principal, esta ventana inicia las otras"""
#     app = wx.App()
#
#     Formulario = Ventana(None)
#     Formulario.Show()
#
#     app.MainLoop()
#
# if __name__ == '__main__':
#     main()

