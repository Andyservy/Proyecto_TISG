# Packages Third-party
import wx

# Package Project
from Proyecto_TISG.Frame_main.Menú_main import menú_Main
from Proyecto_TISG.Package.Formulary import Verificación, Panel


class frame_main(wx.Frame):
    def __init__(self, parent, title, size, colour):
        super(frame_main, self).__init__(parent, title=title, size=size)
        self.Verificación_Call = Verificación(self)
        self.Centre()
        self.GUI_init(colour)

    def GUI_init(self, colour):
        self.Verificación_Call.Centre()
        self.Verificación_Call.ShowModal()

    def OnClickCancel(self, event):
        self.Close()

    def OnClickOK(self, event):

        Nombre_Usuario = self.Verificación_Call.Name_User
        menu_main = menú_Main(self, "Nombre_Usuario", "#212F3C")

        event.Skip()


"""
Al usar show () fuera de la definición de los atributos, se debe establecer una variable que herede la clase que 
acumula al Frame, ya que con esto se está resolviendo el primer parámetro, que en este caso sería self (solo admite 
de tipo window, y la variable a la que asignamos el frame se vuelve de esa clase)
Example:

- Frame.Show(self:No esta llenado, Bool: True)
- Variable = Frame(Parámetros)
  Variable.Show(self:Variable, Bool:True

"""
