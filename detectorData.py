import dateutil.parser
from matplotlib import dates
import datetime as dt
import numpy as np

class DetectorData:
    """Класс обеспечивающий парсинг и хранение данных из файлов детекторов"""

    datTim = []
    press = []
    inten = []
    intenFixed = []
    fit = []
    A = 0
    B = 0
    iMax, iMin = 0, 0
    pMax, pMin = 0, 0
    ifMax, ifMin = 0, 0
    intenName = " "
    p = None

    P0=[]
    I0=[]
    beta=0

    def parseFile(self, fileName):
        if "URG" in fileName:
            self.intenName = "$ с^{-1}$"
            i = 2
            p = 1
        else:
            self.intenName = "$ мин^{-1}$"
            i = 1
            p = 2
        with open(fileName) as data:
            next(data)
            for line in data:
                line = line.strip().split("\t")
                self.datTim.append(line[0])
                self.press.append(float(line[p]))
                self.inten.append(float(line[i]))
            data.close()
            self.datTim = [dateutil.parser.datetime.datetime.strptime(s, '%d.%m.%Y %H:%M') for s in self.datTim]
            self.datTim = dates.date2num(self.datTim)

            self.pMax, self.pMin = round(max(self.press),2), round(min(self.press),2)
            self.iMax, self.iMin = round(max(self.inten),2), round(min(self.inten),2)
            self.P0 = [round(np.mean(self.press), 2), round(np.std(self.press),2)]
            print(self.P0[0], self.P0[1])
            self.I0 = [round(np.mean(self.inten), 2), round(np.std(self.inten), 2)]



        return 1

    def intenFix(self):
        n = len(self.inten)

        self.B = round((n*sum(self.press[i]*self.inten[i] for i in range(0, n)) -
        sum(self.inten)*sum(self.press))/(n*sum(p*p for p in self.press) - pow(sum(self.press), 2)), 2)

        self.A = round((sum(self.inten) - self.B * sum(self.press)) / n, 2)

        z = np.polyfit(self.press, self.inten, 1)
        self.p = np.poly1d(z)

        print ("y = {0} + {1}x".format(self.A, self.B))


        pavg = sum(self.press)/float(len(self.press))
        self.intenFixed = [self.inten[i] + self.B*(pavg - self.press[i]) for i in range(0, n)]
        self.ifMax, self.ifMin = round(max(self.intenFixed),2), round(min(self.intenFixed),2)
        self.beta = round(self.B/self.I0[0]*100, 2)

    def __init__(self, fileName):
        self.datTim = []
        self.press = []
        self.inten = []
        self.intenFixed = []
        self.fit = []
        self.P0 =[]
        self.I0 = []

        self.parseFile(fileName)
        self.intenFix()


