'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import datetime
import os
ilksaat    = datetime.datetime(1994, 4, 12,0,0,0)
sonsaat   = datetime.datetime(2022, 10, 13,22,0,0)
def gunhesaplama(date1,date2):
    return (date2-date1).days
def saathesaplama(date1,date2):
    doneceksaat = ""
    kalan = (date2-date1).total_seconds()
    saat = int(kalan/60/60)
    kalan = kalan - saat *60*60
    dakika = int (kalan /60)
    kalan = kalan -dakika*60
    saniye = int(kalan)
    doneceksaat = str(saat)+ ":"+str(dakika)+":"+str(saniye)
    return doneceksaat

dersinbaslamasaati = datetime.datetime.now()
while(True):
    suankisaat = datetime.datetime.now()
    
    os.system("clear")
    print(saathesaplama(dersinbaslamasaati,suankisaat))
    if (suankisaat-dersinbaslamasaati).total_seconds() > 3600:
        break
    


print("Hello World")

#function



def toplama(x,y):
    return x + y
    


class Dersler():
    def baslangic(self,saat):
        pass
    def mola(self,saat, sure):
        pass
    def bitis(self, saat):
        pass
        
class Matematik(Dersler):
    def toplama(self,x,y):
        pass
    def logaritma(self,x,taban):
        pass
    
class Person():
    pass
class Work():
    name=""
    __baslamaSaati=0
    __bitisiSaati=0
    def __init__(self,name):
        self.name=name
    def setBaslama(self, time):
        self.__baslamaSaati = time
    def setBitis(self, time):
        self.__bitisSaati = time
    def kacSaatCalisir(self):
        return self.__bitisSaati - self.__baslamaSaati
    pass
    
class WorkOfPerson():
    def __init__(self, person:Person, work:Work):
        self.work = work
        self.person = person
        
    def kacSaatCalisir(self):
        return self.work.kacSaatCalisir()
    
aziz = Person()
is1 = Work("polis")
is1.setBaslama(7) # is1.baslamaSaati = 7
is1.setBitis(18)
print(str(is1.kacSaatCalisir()))
azizinisi = WorkOfPerson(aziz,is1)
print(azizinisi.kacSaatCalisir())
    
