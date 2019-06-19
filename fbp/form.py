# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx


import wx.xrc
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import \
FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from detectorData import DetectorData

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):

    Data = None

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Обработка данных детектора", pos = wx.DefaultPosition, size = wx.Size( 737,425 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

        bSizer61 = wx.BoxSizer( wx.VERTICAL )

        gSizer21 = wx.GridSizer( 0, 2, 0, 0 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
        self.graphPanel1 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		
        self.graphPanel1.SetSizer( bSizer14 )
        self.graphPanel1.Layout()
        bSizer14.Fit( self.graphPanel1 )
        bSizer6.Add( self.graphPanel1, 1, wx.EXPAND |wx.ALL, 5 )

###########
        self.figure1 = Figure()
        #self.axes1 = self.figure.add_subplot(111)
        self.canvas1 = FigureCanvas(self, wx.ID_ANY, self.figure1)
        bSizer14.Add(self.canvas1, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        self.toolbar1 = NavigationToolbar2Wx(self.canvas1)
        self.toolbar1.Realize()
        bSizer14.Add(self.toolbar1, 0, wx.LEFT | wx.EXPAND)
        self.toolbar1.Show()
        self.Fit()
################

        gSizer21.Add( bSizer14, 2, wx.EXPAND, 5 )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

        bSizer7.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

        bSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_staticText6 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

        bSizer7.Add( self.m_staticText6, 0, wx.ALL, 5 )


        gSizer21.Add( bSizer7, 0, wx.EXPAND, 5 )


        bSizer61.Add( gSizer21, 1, wx.EXPAND, 5 )

        gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

        bSizer62 = wx.BoxSizer( wx.VERTICAL )


        gSizer3.Add( bSizer62, 1, wx.EXPAND, 5 )

        bSizer71 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText41 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText41.Wrap( -1 )
        self.m_staticText41.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

        bSizer71.Add( self.m_staticText41, 0, wx.ALL, 5 )

        self.m_staticText51 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText51.Wrap( -1 )
        self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

        bSizer71.Add( self.m_staticText51, 0, wx.ALL, 5 )

        self.m_staticText61 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText61.Wrap( -1 )
        self.m_staticText61.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

        bSizer71.Add( self.m_staticText61, 0, wx.ALL, 5 )


        gSizer3.Add( bSizer71, 1, wx.EXPAND, 5 )


        bSizer61.Add( gSizer3, 1, wx.EXPAND, 5 )


        self.m_panel2.SetSizer( bSizer61 )
        self.m_panel2.Layout()
        bSizer61.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Открыть...", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem1 )

        self.m_menu1.AppendSeparator()

        self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Выход", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem2 )

        self.m_menubar1.Append( self.m_menu1, u"Файл" )

        self.m_menu2 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"График 1", wx.EmptyString, wx.ITEM_CHECK )
        self.m_menu2.AppendItem( self.m_menuItem3 )
        self.m_menuItem3.Check( True )

        self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"График 2", wx.EmptyString, wx.ITEM_CHECK )
        self.m_menu2.AppendItem( self.m_menuItem4 )
        self.m_menuItem4.Check( True )

        self.m_menubar1.Append( self.m_menu2, u"Показать" )

        self.SetMenuBar( self.m_menubar1 )


        self.Centre( wx.BOTH )

        # COnnect events
        self.Bind( wx.EVT_MENU, self.openFile, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.showGraph1, id = self.m_menuItem3.GetId() )

    def showGraph1( self, event ):
        if self.m_menuItem3.IsChecked() == False:
            self.graphPanel1.Hide()
            self.canvas1.Hide()
            self.toolbar1.Hide()
        else:
            self.graphPanel1.Show()
            self.canvas1.Show()
            self.toolbar1.Show()

    def __del__( self ):
        pass


    def openFile( self, event ):
        with wx.FileDialog(self, "Открыть файл данных детектора", wildcard="DAT файлы (*.dat)|*.dat",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                self.Data = DetectorData(pathname)
                self.axes1 = self.figure1.add_subplot(111)
                self.axes1.plot( self.Data.datTim, self.Data.inten )
                self.axes1.set_xlabel("Время хуемя")
                self.axes1.set_ylabel("Интенсивность")

                self.axes2 = self.figure1.add_subplot(111)
                self.axes2.plot( self.Data.datTim, self.Data.press )
                self.axes2.set_ylabel("Давление")

            except IOError:
                wx.LogError("Не удалось открыть файл '%s'." % newfile)

class DetectorApp(wx.App):

     # wxWidgets calls this method to initialize the application
     def OnInit(self):

         # Create an instance of our customized Frame class
         frame = mainFrame(None)
         frame.Show(True)

         # Return a success flag
         return True
