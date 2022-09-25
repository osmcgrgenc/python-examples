dizi = [1,10,2,11,3,8,4,-1,15]
# i = 0
# y = 0
# en_kucuk = 
# dizi = [-1,10, 2,11,3,8,4,1,15]
dizi.sort()
print(dizi)
dizi_sonuc = [-1, 1, 2, 3, 4, 8, 10, 11, 15]



dizi_result = []
for i in range(len(dizi)):
    print("i="+ str(i))
    y = i
    print("y="+str(y))
    en_kucuk = dizi[i]
    print("en_kucuk="+str(en_kucuk))
    en_kucuk_index = i
    print("en_kucuk_index="+str(en_kucuk_index))
    while(y < len(dizi)):
        print("y="+str(y))
        print("dizi[y]="+str(dizi[y]))
        if dizi[y]< en_kucuk:
            en_kucuk=dizi[y]
            print("en_kucuk="+str(en_kucuk))
            en_kucuk_index = y
            print("en_kucuk_index="+str(en_kucuk_index))
            dizi[y]=dizi[i]
            print("dizi[y]="+str(dizi[y]))
            dizi[i]=en_kucuk
            print(str(i)+".index dizi[i]="+str(dizi[i]))
            print(dizi)
        y=y+1
    dizi_result.append(en_kucuk)
    print(dizi_result)

print(dizi_result)
print(dizi)


