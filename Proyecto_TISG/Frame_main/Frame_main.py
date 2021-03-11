# Packages Third-party
import wx

# Package Project
from Proyecto_TISG.Frame_main.Menú_main import menú_Main
from Proyecto_TISG.Package.Formulary import Verificación, Panel


class frame_main(wx.Frame):
    def __init__(self, parent, title, size, colour):
        super(frame_main, self).__init__(parent, title=title, size=size)
        self.Centre()
        self.GUI_init(colour)

    def GUI_init(self, colour):
        Verificación_Call = Verificación(self)
        Verificación_Call.ShowModal()

        try:

            Nombre_Usuario = Verificación_Call.Name_User
            menu_main = menú_Main(self, "Nombre_Usuario", colour)

        except RuntimeError:
            exit(0)

    def OnClickCancel(self, event):
        self.Close()




"""
Al usar show () fuera de la definición de los atributos, se debe establecer una variable que herede la clase que 
acumula al Frame, ya que con esto se está resolviendo el primer parámetro, que en este caso sería self (solo admite 
de tipo window, y la variable a la que asignamos el frame se vuelve de esa clase)
Example:

- Frame.Show(self:No esta llenado, Bool: True)
- Variable = Frame(Parámetros)
  Variable.Show(self:Variable, Bool:True

"""
