#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# System Packages
import sys

# Project Packages
from Proyecto_TISG.Package import Btnbicolor, show_messange
# third party packages
import wx
import mysql.connector

# COSULTA


"""
Advertencias: 
- Un caso en el que definitivamente tienes que hacer event.Skip()es en el controlador al vincularte a 
  wx.EVT_CLOSE. Si no lo hace, el cierre no sucederá correctamente
- Revisar para la propagación de eventos: https://wiki.wxpython.org/EventPropagation
- Herencia multiple: https://realpython.com/python-super/#an-overview-of-pythons-super-function
"""

Title = "Boost Mannager"


class Verificación(wx.Dialog):
    """
    - Para hacer la llamada, se debe usar ShowModal (Esto limita al usuario a no saltarse la verificación)
    - Tener en cuenta que esta clase debe ir antes del pedazo código que quiere proteger

    Para insertar las condiciones, se recomienda llamar a if Variable.OnClickOK

    Al condicionar OnClickCancel, si se cierra el padre también, debe especificar un control de error
    """

    def __init__(self, parent):
        super(Verificación, self).__init__(parent, title="Boost Mannager", size=(500, 300))

        Colour = "#212F3C"

        self.SetBackgroundColour(Colour)
        self.Centre()
        self.SetWindowStyleFlag(wx.BORDER_NONE)

        self.panel = Panel(self, Colour)
        self.Name_User = self.panel.ENTRADA_Name

        self.panel.BTN_Cancel.Bind(wx.EVT_BUTTON, self.Parent.OnClickCancel)


class Panel(wx.Panel):

    # noinspection PyCompatibility
    def __init__(self, parent, Colour):
        super(Panel, self).__init__(parent)

        self.BTN_Cancel = wx.Button(self, -1, "CANCEL")

        # ------------------------------------------------------------------------------------------------------------------
        self.ENTRADA_Contraseña = wx.TextCtrl(self, -1,
                                              style=wx.BORDER_NONE | wx.ALIGN_CENTER | wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)

        self.ENTRADA_Name = wx.TextCtrl(self, -1,
                                        style=wx.BORDER_NONE | wx.ALIGN_CENTER & ~ wx.TE_PASSWORD)
        # ------------------------------------------------------------------------------------------------------------------

        self.initGUI()

        self.Color_font = Colour

        """
        RECORDATORIO:
        def surface_area(self):
            face_area = super(Square, self).area()
            return face_area * 6

        def volume(self):
            face_area = super(Square, self).area()
            return face_area * self.length
            
        En este ejemplo específico, el comportamiento no cambia. Pero imagina que Square también implementó una 
        .area()función que querías asegurarte de Cube que no se usara. Llamar super()de esta manera le permite hacer 
        eso. 
        """

    def initGUI(self):
        # Contenedores
        Box_Main = wx.BoxSizer(wx.VERTICAL)
        Box_Entrada = wx.BoxSizer(wx.VERTICAL)
        Box_Cancel_OK = wx.BoxSizer(wx.HORIZONTAL)

        # CONTROLES
        self.ENTRADA_Name.SetHint('Ingrese su nombre')
        Box_Entrada.Add(self.ENTRADA_Name, 1, wx.EXPAND | wx.ALL, 10)

        self.ENTRADA_Contraseña.SetHint('Ingrese su contraseña')
        Box_Entrada.Add(self.ENTRADA_Contraseña, 1, wx.EXPAND | wx.ALL, 10)

        BTN_OK = wx.Button(self, -1, 'OK')

        Box_Cancel_OK.Add(BTN_OK, 1, wx.EXPAND | wx.ALL, 15)

        Box_Cancel_OK.Add(self.BTN_Cancel, 1, wx.EXPAND | wx.ALL, 15)

        # AÑADIENDO LOS BOXERS HIJOS AL PADRE

        Box_Main.Add(Box_Entrada, 3, wx.EXPAND)
        Box_Main.Add(Box_Cancel_OK, 2, wx.EXPAND)

        # CONFIGURANDO SIZER

        self.SetSizer(Box_Main)

        # EVENTOS

        BTN_OK.Bind(wx.EVT_BUTTON, self.OnClickOK)

        # MODIFICANDO FUENTES

        Font_Entrada = wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL)
        self.ENTRADA_Name.SetFont(Font_Entrada)
        self.ENTRADA_Contraseña.SetFont(Font_Entrada)

        Font_Botones = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        BTN_OK.SetFont(Font_Botones)
        self.BTN_Cancel.SetFont(Font_Botones)

        # MODIFICANDO COLOR

        self.ENTRADA_Name.SetBackgroundColour('#283747')

        self.ENTRADA_Contraseña.SetBackgroundColour('#283747')

        # ESTILO A LOS BOTONES
        Botones_OK_CANCEL = [BTN_OK, self.BTN_Cancel]
        Btnbicolor(Botones_OK_CANCEL, '#2C4158', '#384A5F')

    def OnClickOK(self, event):

        user_name = self.ENTRADA_Name.GetValue()
        user_contraseña = self.ENTRADA_Contraseña.GetValue()

        consult_mysql = "SELECT Contraseña FROM login_history WHERE Nombre_User = '%s'" % user_name

        # Verifica si están vacíos
        if user_name and user_contraseña:
            db = mysql.connector.connect(host="127.0.0.1", user="root", password="76743571mysql",
                                         database="boost_mannager")
            cursor = db.cursor()  # Conectamos a la base de datos

            try:
                # Cubrimos si es que la base de datos no es correcta
                cursor.execute(consult_mysql)
                Contraseña = cursor.fetchall()  # Colectamos en un tuple el valor seleccionado

                if Contraseña:
                    if str(int(Contraseña[0][
                                   0])) == user_contraseña:  # convertimos a int el valor de contraseña para así,
                        # poder eliminar sus parenthesis, luego lo pasamos a str para compararlo con lo que introduce
                        # el usuario, lo cual es str
                        self.Parent.Destroy()
                        db.close()

                        """
                        Para destruir la ventana directamente, se necesita especificar el parámetro en Panel, 
                        para que, al ser usado en Ventana, se introduzca un self, así:
                        
                        import wx

                        class MainScene(wx.Frame):
                          def __init__(self, parent, title):
                            super(MainScene, self).__init__(parent, title=title, size=(300, 300))
                            self.InitUI()

                          def InitUI(self):
                            # Define Master Panel
                            masterPanel = wx.Panel(self)
                            masterPanel.SetBackgroundColour("gold")
                            horzbox = wx.BoxSizer(wx.HORIZONTAL)
                            subPanel=SubPanel(parent=masterPanel, size=(200, 200), mainWin=self)

                        class SubPanel(wx.Panel):
                          def __init__(self, parent, size, mainWin):
                            wx.Panel.__init__(self, parent, size=size)
                            self.mainWin = mainWin
                            self.SetBackgroundColour("gray")
                            vbox = wx.BoxSizer(wx.VERTICAL)
                            exit_button = wx.Button(self, label="Exit")
                            exit_button.Bind(wx.EVT_BUTTON, self.onClose)
                            vbox.Add(exit_button, proportion=1, flag=wx.ALL | wx.CENTER, border=5)
                            self.SetSizer(vbox)
                        
                          def onClose(self, event): 
                            print('Called from SubPanel')      
                            self.mainWin.Destroy()
                        """  # Si alguna vez se necesita especificar que es lo que se debe cerrar

                    else:
                        show_messange(Panel, "Contraseña no válida")
                        print(str(int(Contraseña[0][0])))

                else:
                    show_messange(Panel, "Usuario no existente")

            except mysql.connector.errors.ProgrammingError:
                db.rollback()

            finally:
                db.close()

        else:
            show_messange(Panel, "Nombre de usuario o la contraseña no deberían estar vacíos")
