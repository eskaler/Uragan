# -*- coding: utf-8 -*-

## Python code generated with wxFormBuilder (version Jun 17 2015)

import wx
import wx.xrc
##
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import \
FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx


class MainFrame ( wx.Frame ):

    def initForm( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Обработка данных детектора", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gSizer1 = wx.GridSizer( 0, 2, 0, 1 )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

        gSizer4 = wx.GridSizer( 2, 3, 0, 0 )

        self.m_checkBox1 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Темп счета нейтронов (без учета БЭ)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox1.SetValue(True)
        gSizer4.Add( self.m_checkBox1, 0, wx.ALL, 1 )

        self.m_checkBox2 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Давление", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox2.SetValue(True)
        gSizer4.Add( self.m_checkBox2, 0, wx.ALL, 1 )

        self.m_checkBox3 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Темп счета нейтронов(с учетом БЭ)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox3.SetValue(True)
        gSizer4.Add( self.m_checkBox3, 0, wx.ALL, 1 )


        self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"min:\nmax:\navg:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        gSizer4.Add( self.m_staticText4, 0, wx.ALL, 3 )

        self.m_staticText5 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"min:\nmax:\navg:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        gSizer4.Add( self.m_staticText5, 0, wx.ALL, 3 )

        self.m_staticText6 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"min:\nmax:\navg:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        gSizer4.Add( self.m_staticText6, 0, wx.ALL, 3 )



        self.m_panel1.SetSizer( gSizer4 )
        self.m_panel1.Layout()
        gSizer4.Fit( self.m_panel1 )
        self.m_panel1.Layout()
        bSizer2.Add( self.m_panel1, 0.88, wx.EXPAND, 5 )


        gSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        bSizer31 = wx.BoxSizer( wx.VERTICAL )
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
        self.m_staticText7 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"P0 = ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer31.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"I0 = ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        bSizer31.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"B = ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer31.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"β = ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        bSizer31.Add( self.m_staticText10, 0, wx.ALL, 5 )


        self.m_panel2.SetSizer( bSizer31 )
        self.m_panel2.Layout()
        bSizer31.Fit( self.m_panel2 )
        bSizer3.Add( self.m_panel2, 0.9, wx.EXPAND, 5 )


        gSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


        self.SetSizer( gSizer1 )
        self.Layout()
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_fileMenu = wx.Menu()
        self.m_mbopenFile = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"Открыть", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_fileMenu.AppendItem( self.m_mbopenFile )

        self.m_fileMenu.AppendSeparator()

        self.m_mbexit = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"Выход", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_fileMenu.AppendItem( self.m_mbexit )

        self.m_menubar1.Append( self.m_fileMenu, u"Файл" )

        #self.m_menu3 = wx.Menu()
        #self.m_mbGraph1 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Данные 1", wx.EmptyString, wx.ITEM_CHECK )
        #self.m_menu3.AppendItem( self.m_mbGraph1 )
        #self.m_mbGraph1.Check( True )

        #self.m_mbGraph2 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Данные 2", wx.EmptyString, wx.ITEM_CHECK )
        #self.m_menu3.AppendItem( self.m_mbGraph2 )
        #self.m_mbGraph2.Check( True )

        #self.m_menubar1.Append( self.m_menu3, u"Скрыть" )

        self.SetMenuBar( self.m_menubar1 )



        #заготовки для графикa 1
        self.figure1 = Figure()

        self.canvas1 = FigureCanvas(self, wx.ID_ANY, self.figure1)
        bSizer2.Add(self.canvas1, 3, wx.LEFT | wx.TOP | wx.EXPAND)
        self.toolbar1 = NavigationToolbar2Wx(self.canvas1)
        self.toolbar1.Realize()
        bSizer2.Add(self.toolbar1, 0, wx.LEFT | wx.EXPAND)
        #self.Fit()
        #####

        #2
        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self, wx.ID_ANY, self.figure2)
        bSizer3.Add(self.canvas2, 3, wx.LEFT | wx.TOP | wx.EXPAND)
        self.toolbar2 = NavigationToolbar2Wx(self.canvas2)
        self.toolbar2.Realize()
        bSizer3.Add(self.toolbar2, 0, wx.LEFT | wx.EXPAND)

        #self.Fit()
        ##
        self.SetAutoLayout(True)
        self.Centre( wx.BOTH )
        self.SetIcon(wx.Icon('icon.ico', wx.BITMAP_TYPE_ICO))

        self.Refresh()


    def __del__( self ):
        pass


