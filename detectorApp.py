import wx
import wx.xrc
from detectorData import DetectorData
import detectorForm
from matplotlib import dates
from functools import partial
#import numpy as np

class EventHandler(detectorForm.MainFrame):
    """Класс наследующий форму и содержащий обработку ее событий"""

    Data = []

    def __init__(self):

        self.initForm(None)
        #бинды на события
        self.Bind( wx.EVT_MENU, self.openFile, id = self.m_mbopenFile.GetId() )
        self.Bind( wx.EVT_MENU, self.exitApp, id = self.m_mbexit.GetId() )
        #self.Bind( wx.EVT_MENU, self.showGraph1, id = self.m_mbGraph1.GetId() )
        #self.Bind( wx.EVT_MENU, self.showGraph2, id = self.m_mbGraph2.GetId() )
        self.m_checkBox1.Bind(wx.EVT_CHECKBOX, lambda evt, checkit=self.m_checkBox1, figure=self.figure1, axisno=0 : self.hideGraph(evt, checkit, figure, axisno))
        self.m_checkBox2.Bind(wx.EVT_CHECKBOX, lambda evt, checkit=self.m_checkBox2, figure=self.figure1, axisno=1 : self.hideGraph(evt, checkit, figure, axisno))
        self.m_checkBox3.Bind(wx.EVT_CHECKBOX, lambda evt, checkit=self.m_checkBox3, figure=self.figure1, axisno=2 : self.hideGraph(evt, checkit, figure, axisno))
        #self.m_checkBox1.Bind(wx.EVT_CHECKBOX, partial( self.hideGraph, checkit=self.m_checkBox1.IsChecked, figure=self.figure1, axisno=0))



    def openFile(self, event):
        with wx.FileDialog(self, "Открыть файл данных детектора", wildcard="DAT файлы (*.dat)|*.dat",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return


            pathname = fileDialog.GetPath()
            try:

                self.Data = DetectorData(pathname)
                self.drawGraph1()

                self.SetTitle(pathname)
                self.m_checkBox1.SetValue(True)
                self.m_checkBox2.SetValue(True)
                self.m_checkBox3.SetValue(True)

            except IOError:
                wx.LogError("Не удалось открыть файл '%s'." % newfile)

    def drawGraph1(self):

        self.figure1.clear()

        self.axes1 = self.figure1.add_subplot(111)
        self.axes1.plot_date( self.Data.datTim, self.Data.inten, 'b' )
        self.axes1.set_xlabel("Дата")
        self.axes1.set_ylabel(r"Темп счета нейтронов, "+self.Data.intenName, color='blue')
        self.axes1.xaxis.set_major_formatter(dates.DateFormatter('%d-%m-%Y %H:%M'))

        self.axes2 = self.axes1.twinx()
        self.axes2.plot_date( self.Data.datTim, self.Data.press, '#FFA500' )
        self.axes2.set_ylabel("Давление, $мбар$", color='#FFA500')

        self.axes1f = self.axes1.twiny()
        self.axes1f.set_xticklabels([])
        self.axes1f.plot_date( self.Data.datTim, self.Data.intenFixed, 'g' )

        self.figure1.autofmt_xdate(bottom=0.18)

        self.canvas1.draw()
        self.canvas1.Refresh()
        print(self.figure1.axes)

        #right thing
        self.figure2.clear()

        self.axes3 = self.figure2.add_subplot(111)
        self.axes3.plot( self.Data.press, self.Data.inten, linestyle='None', marker='o', markerfacecolor='white', color='b' )
        self.axes3.set_ylabel(r"Темп счета нейтронов, "+self.Data.intenName)
        self.axes3.set_xlabel("Давление, $мбар$")
        self.axes3.text(0.6, 0.8, 'A = {0} {1}\nB = {2} {3} {4}'.format(self.Data.A,
            self.Data.intenName, self.Data.B, self.Data.intenName, '$мбар^{-1}$'), color='r', horizontalalignment='left',
     verticalalignment='center',     transform = self.axes3.transAxes)


        self.axes4 = self.figure2.add_subplot(111)
        self.axes4.plot( self.Data.press, self.Data.intenFixed, linestyle='None', marker='o', markerfacecolor='white', color='g')

        self.axes3f = self.axes3.twiny()
        self.axes3f.plot(self.Data.press, self.Data.p(self.Data.press), color='r')


        self.canvas2.draw()
        self.canvas2.Refresh()


        #

        #ooh whatever
        self.m_staticText4.SetLabel("min: {0}\nmax: {1}\navg: {2}".format(self.Data.iMin, self.Data.iMax, self.Data.I0[0]))
        self.m_staticText5.SetLabel("min: {0}\nmax: {1}\navg: {2}".format(self.Data.pMin, self.Data.pMax, self.Data.P0[0]))
        self.m_staticText6.SetLabel("min: {0}\nmax: {1}\navg: {2}".format(self.Data.ifMin, self.Data.ifMax, round(sum(self.Data.intenFixed)/len(self.Data.intenFixed),2)))

        self.m_staticText7.SetLabel("P0 = {0} ± {1} мбар".format(self.Data.P0[0], self.Data.P0[1]))
        self.m_staticText8.SetLabel("I0 = {0} ± {1} {2}".format(self.Data.I0[0], self.Data.I0[1], self.Data.intenName[1:-1].replace('^{-1}', '\u207B\u00B9')))
        self.m_staticText9.SetLabel("B = {0} {1} {2}".format(self.Data.B, self.Data.intenName[1:-1].replace('^{-1}', '\u207B\u00B9'), u"мбар\u207B\u00B9"))
        self.m_staticText10.SetLabel("β = {0} %/мбар".format(self.Data.beta))

    def hideGraph( self, event, checkit, figure, axisno):
        print(checkit.GetValue(), figure.axes[axisno])
        figure.axes[axisno].set_visible(checkit.GetValue())
        figure.axes[axisno].xaxis.set_visible(True)
        #figure.axes[0].xaxis.set_visible(True)
        #figure.axes[axisno].xticks.set_visible(True)
        self.canvas1.draw()

    def showGraph1(self, event):
        if self.m_mbGraph1.IsChecked() == False:
            #self.graphPanel1.Hide()
            self.canvas1.Hide()
            self.toolbar1.Hide()
            self.m_panel1.Hide()
            #self.gSizer1.Layout()
            #self.canvas2.Fit()
            #self.toolbar2.Fit()
            #self.m_panel2.Fit()
            self.Refresh()

        else:
            #self.graphPanel1.Show()
            self.canvas1.Show()
            self.toolbar1.Show()
            self.m_panel1.Show()
            self.Refresh()

    def showGraph2(self, event):
        if self.m_mbGraph2.IsChecked() == False:
            #self.graphPanel1.Hide()
            self.canvas2.Hide()
            self.toolbar2.Hide()
            self.m_panel2.Hide()
            self.Refresh()

        else:
            #self.graphPanel1.Show()
            self.canvas2.Show()
            self.toolbar2.Show()
            self.m_panel2.Show()
            self.Refresh()

    def exitApp(self, event):
        wx.Frame.close()

    def __del__( self ):
        pass




class DetectorApp(wx.App):

     def OnInit(self):

         frame = EventHandler()
         frame.Show(True)
         frame.Maximize(True)

         return True
