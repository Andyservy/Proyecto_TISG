# Packages Third-party
import wx
import wx.lib.agw.gradientbutton as GB

# Package Project
from Proyecto_TISG.Package import Btnbicolor, Formulary


class menú_Main(wx.Panel):

    def __init__(self, parent, Name, Colour):
        super(menú_Main, self).__init__(parent)
        self.Verificación_Configuración = Formulary.Verificación(self)
        self.User_name = Name
        self.SetBackgroundColour(Colour)
        self.init_GUI(Colour)

    def init_GUI(self, colour_universal):
        # CONTENEDORES

        box_main = wx.BoxSizer(wx.VERTICAL)
        Data_sesión = wx.BoxSizer(wx.HORIZONTAL)
        Items_colum1 = wx.BoxSizer(wx.VERTICAL)
        Items_colum2 = wx.BoxSizer(wx.VERTICAL)
        Items = wx.BoxSizer(wx.HORIZONTAL)

        # WIDGETS
        Greeting = wx.StaticText(self, -1, label=("Buen día %s" % str(self.User_name)), style=wx.ALIGN_CENTER)
        Data_sesión.Add(Greeting, 2, wx.EXPAND | wx.ALL, 10)

        bmpBtn_Configuration = GB.GradientButton(self, wx.ID_ANY, label="Configuración")
        Data_sesión.Add(bmpBtn_Configuration, 1, wx.EXPAND | wx.ALL, 20)
        bmpBtn_Configuration.Bind(wx.EVT_BUTTON, self.OnClick_Configuración)

        Facturación = wx.Button(self, -1, 'FACTURACIÓN')
        # Facturación.Bind(self, self.OnClick_Facturación)

        Inventario = wx.Button(self, -1, 'INVENTARIO')
        Utilería = wx.Button(self, -1, 'UTILERÍA')
        Estadísticas = wx.Button(self, -1, 'ESTADÍSTICAS')
        Agenda = wx.Button(self, -1, 'AGENDA')
        Nomina = wx.Button(self, -1, 'NOMINA')

        Items_List = [Facturación, Inventario, Utilería, Estadísticas, Agenda, Nomina]

        # _____________________________________________________________________________________________________________

        Items_STYLES_1 = [Facturación, Inventario, Utilería]
        Items_Styles_2 = [Estadísticas, Agenda, Nomina]

        for button in Items_STYLES_1:
            Items_colum1.Add(button, 1, wx.EXPAND | wx.ALL, 10)

        for button in Items_Styles_2:
            Items_colum2.Add(button, 1, wx.EXPAND | wx.ALL, 10)

        Items.Add(Items_colum1, 1, wx.EXPAND)
        Items.Add(Items_colum2, 1, wx.EXPAND)

        # _____________________________________________________________________________________________________________

        # AÑADIENDO LOS BOX AL BOX PRINCIPAL
        box_main.Add(Data_sesión, 1, wx.EXPAND)
        box_main.Add(Items, 3, wx.EXPAND)

        # CONFIGURANDO SIZER
        self.SetSizer(box_main)

        # COLOUR and SIZE
        Font_Greeting = wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL)
        Greeting.SetBackgroundColour(colour_universal)
        Greeting.SetForegroundColour("#FFFFFF")
        Greeting.SetFont(Font_Greeting)

        Font_bmp_configuration = wx.Font(20, wx.SCRIPT, wx.NORMAL, wx.NORMAL)
        bmpBtn_Configuration.SetFont(Font_bmp_configuration)
        bmpBtn_Configuration.SetForegroundColour("#FFFFFF")

        for button_font in Items_List:
            Font_Items = wx.Font(20, wx.SWISS, wx.NORMAL, wx.LIGHT)
            button_font.SetFont(Font_Items)
            button_font.SetForegroundColour("#7D95B7")

        # ESTILOS DE BOTONES

        Btnbicolor(Items_List, '#2C4158', '#384A5F')

    def OnClick_Configuración(self, event):

        self.Verificación_Configuración.ShowModal()


    def OnClickCancel(self, event):
        self.Verificación_Configuración.Close()

