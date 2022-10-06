
a=[33,1,7,55,13,8,99,66,42,57,41,19,0]
def buble_sort(liste):
    for i in range(len(liste)):
        for x in range(0,len(liste)-1):
            if liste[x]>liste[x+1]:
                liste[x],liste[x+1]=liste[x+1],liste[x]

    return (liste)
def fibonacci(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        x=fibonacci(x - 2) + fibonacci(x - 1)
        return (x)
def faktoriyel(y):
    z=1
    for i in range(1,y+1):
        z=z*i
    return (z)
def asal_sayi(a):
    c = int(input("1-ci asal sayi araliginizi belirtin: "))
    d = int(input("2-ci asal sayi araliginizi belirtin: "))
    sonuc=[]
    for i in range(c, d + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                sonuc.append(i)
    print(sonuc)
while True:
    kullanici=int(input(" Calismasini istediginiz proqram icin bir secim yapin \n1) Siralama alqoritmasi proqrami \n2) fibonacci proqrami\n3) faktoriyel proqrami\n4) Asal sayilari bulan proqram\n5) Exit"))
    if kullanici== 1:
        sayiList=[]
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
        print("Dizinin sirali hali: ",buble_sort(sayiList))
    elif kullanici==2:
        a=int(input("fibonacci sayinizi belirtin: "))
        if a<=0:
            print("Lutfen pozitiv rakam girin!")
            continue
        else:
            for i in range(1, a+1):
                print(fibonacci(i))
    elif kullanici==3:
        b = int(input("faktoriyelini bulmak istediginiz sayiyi belirtin: "))
        if b<=0:
            print("Lutfen pozitiv rakam girin!")
        else:
            print("Rakamin faktoriyeli -----> ",faktoriyel(b))
            kullanici = int(input(" Calismasini istediginiz proqram icin bir secim yapin: "))
    elif kullanici==4:
        print(asal_sayi(a))


    elif kullanici==5:
        print("Proqram sonlandi. Tesekkurler!")
        break
    else:
        print("Yalnis rakam sectiniz! Bir daha deneyin!")













