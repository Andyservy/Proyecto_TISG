#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

try:
    import wx
except ImportError as error:
    print(error)
    sys.exit(1)

# para usar paquetes
from Proyecto_TISG.info import (__author__,
                                __appname__,
                                __contact__,
                                __license__,
                                __projecturl__,
                                __licensefull__,
                                __description__,
                                __descriptionfull__, )

from Proyecto_TISG.Formulary import Ventana


def main():
    """Llamada a la ventana principal, esta ventana inicia las otras"""
    app = wx.App()

    Formulario = Ventana(None, title='Boost Manager', size=(500, 300), colour="#212F3C", style=wx.BORDER_NONE)
    Formulario.Show()

    app.MainLoop()
