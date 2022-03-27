import datetime

class Bus:
    def __init__(self):
        self.nummerlinii =0
        self.czasy=[]
        self.przystanki =[]

    def ustawParametry(self,czasy,nummerlinii,przystanki):
        self.czasy = czasy
        self.nummerlinii =nummerlinii
        self.przystanki =przystanki

class Timetable(Bus):
    def __init__(self):
        Bus.__init__(self)

    def printowanie(self):
        self.data = datetime.date.today()
        self.godzina = "wprowadź godzine:"
        print("wprowadź numer przystaneku ")
        print(self.przystanki)
        self.x =int(input())-1
        print("dnia {} ".format(self.data) +"autobus linii {} ".format(self.nummerlinii) +" odjedzie z przystanku {}".format(self.przystanki[self.x]))
        for ab in range(86400):
            if ((self.czasy[self.x]+ab*600 >= 86400)):
                break
            print(datetime.timedelta(seconds=self.czasy[self.x]+ab*600))

class Passager:

    def ustawPassazera(self, imie,znizka):
        self.imie = imie
        self.znizka =znizka


class Ticket(Passager):
    cenabazowabilietu = 4
    def ustalCeneBiletu(self):
        print("Passażer {} ".format(self.imie) +" objęty jest zniżka: {}".format(str(self.znizka*100)+"% ")+ \
              "cena biletu wynosi {} zł".format((1-self.znizka)*self.cenabazowabilietu))



klaudia =Ticket()
krystian =Ticket()
klaudia.ustawPassazera("klaudia",0.3)
krystian.ustawPassazera("krystian",0.2)
krystian.ustalCeneBiletu()
klaudia.ustalCeneBiletu()
klaudia.cenabazowabilietu =5
klaudia.ustalCeneBiletu()

czasy = [600,1200,4800]
przystanki = [" 1- Jana Pawła","2 - Czesława Niemena", "3- zakola"]
czasy2 = [111,1223,4830]
przystanki2 = [" 1-Samuraja","2 -Ninja", "3- Sensei"]

#inicjacja obiektów
bus911 =Timetable()
bus922= Timetable()
bus911.nummerlinii =911
bus911.czasy.extend(czasy)
bus911.przystanki.extend(przystanki)
bus911.printowanie()

bus922.ustawParametry(czasy2,922,przystanki2)
bus922.printowanie()