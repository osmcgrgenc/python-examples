class ListSortClass():
    def definationListe(self):
        sayiList = []
        while(True):
            k_deger=input("Bir sayi giriniz(0'dan küçük bir değer sonlandırır):")
            if(k_deger == ""):
                print("bir şey yazmadın")
                break
            try:
                new_point=int(k_deger)
                sayiList.append(new_point)
            except:
                break
        
        self.liste = sayiList
    def PrintList(self):
        print(self.liste)
        return self.liste
    def BubbleSort(self):
        liste = self.liste.copy()
        for i in range(len(liste)):
            for x in range(0,len(liste)-1):
                if liste[x]>liste[x+1]:
                    liste[x],liste[x+1]=liste[x+1],liste[x]
        print(liste)
        return (liste)
    