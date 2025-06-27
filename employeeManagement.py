# DÖNEM2 PROJE ÖDEVİ
def calisan_ekle():
   isim=input("CALİSANİN İSMİNİ GİRİNİZ :")
   soy_isim=input("SOYİSMİNİ GİRİNİZ:")
   id=input("CALİSANA ÖZEL İDSİNİ GİRİNİZ:")
   yas=input("YASİNİ GİRİNİZ:")
   try:
     cocuk_sayi=int(input("ÇOCUK SAYISINI GİRİNİZ:"))
   except ValueError:
      cocuk_sayi = int(input("YANLIŞ VERİ TİPİ. TEKRAR ÇOCUK SAYISINI GİRİNİZ:"))
   eski_maas = input("ESKİ MAASINI GİRİNİZ:")
   yeni_maas = input("YENİ MAASİNİ GİRİNİZ:")
   with open("22100011016.txt","a") as dosya:
      dosya.write("{}-{}-{}-{}-{}-{}-{}\n".format(isim,soy_isim,id,yas,cocuk_sayi,eski_maas,yeni_maas))
def calisan_sil():
   goruntu = []
   sil = []
   yazilacak = []
   with open("22100011016.txt","r") as dosya:
      calisanlar=dosya.readlines()
   for i in calisanlar:
      goruntu.append(" ".join(i[:-1].split("-")))
   a = 1
   for i in goruntu:
      print("{}-{}".format(a, i))
      a += 1
   for i in goruntu:
      i=i.split(" ")
      sil.append(i)
   secim = input("SİLMEK İSTEDİGİNİZ CALİSANIN İDSİNİ GİRİNİZ:")
   kontrol=0
   for i in range(len(sil)):
      if secim == sil[i][2]:
         kontrol=1
         goruntu.pop(i)
   if kontrol==0:
      print("BU IDDE BİR CALİSAN BULUNMAMAKTADIR!")
   for i in goruntu:
      i=i.split(" ")
      yazilacak.append(i)
   with open("22100011016.txt", "w") as dosya:
      if len(yazilacak)>0:
         for i in range(len(yazilacak)):
            dosya.write("{}-{}-{}-{}-{}-{}-{}\n".format(yazilacak[i][0],yazilacak[i][1],yazilacak[i][2],yazilacak[i][3],yazilacak[i][4],yazilacak[i][5],yazilacak[i][6]))
def calisan_ara():
   goruntu=[]
   bilgi=[]
   with open("22100011016.txt","r") as dosya:
      calisanlar=dosya.readlines()
   secim = input("BİLGİLERİNİ GÖRÜNTÜLEMEK İSTEDİGİNİZ CALİSANİN İDSİNİ GİRİNİZ :")
   for i in calisanlar:
      goruntu.append(" ".join(i[:-1].split("-")))
   for i in goruntu:
      i = i.split(" ")
      bilgi.append(i)
   kontrol=0
   for i in range(len(bilgi)):
      if secim == bilgi[i][2]:
          kontrol=1
          print("İSİM:{} SOYİSİM:{} YAŞ:{} ÇOCUK SAYISI:{}  ESKİ MAAS:{} YENİ MAAS:{}".format(bilgi[i][0],bilgi[i][1],bilgi[i][3],bilgi[i][4],bilgi[i][5],bilgi[i][6]))
   if kontrol==0:
      print("BU IDDE BİR CALİSAN BULUNMAMAKTADIR!")
def calisan_guncelle():
   goruntu=[]
   guncelle = []
   yazilacak=[]
   with open("22100011016.txt","r") as dosya:
      calisanlar=dosya.readlines()
   for i in calisanlar:
      goruntu.append(" ".join(i[:-1].split("-")))
   a = 1
   for i in goruntu:
      print("{}-{}".format(a, i))
      a += 1
   for i in goruntu:
      i=i.split(" ")
      guncelle.append(i)
   secim = input("BİLGİLERİNİ GUNCELLEMEK İSTEDİGİNİZ CALİSANIN İDSİNİ GİRİNİZ:")
   kontrol=0
   for i in range(len(guncelle)):
      if secim == guncelle[i][2]:
         kontrol=1
         isim = input("CALİSANİN İSMİNİ GİRİNİZ :")
         soy_isim = input("SOYİSMİNİ GİRİNİZ:")
         yas = input("YASİNİ GİRİNİZ:")
         cocuk_sayi = input("ÇOCUK SAYISINI GİRİNİZ:")
         eski_maas = input("ESKİ MAASINI GİRİNİZ:")
         yeni_maas = input("YENİ MAASİNİ GİRİNİZ:")
         guncelle[i][0]=isim
         guncelle[i][1]=soy_isim
         guncelle[i][3]=yas
         guncelle[i][4]=cocuk_sayi
         guncelle[i][5]=eski_maas
         guncelle[i][6]=yeni_maas
   if kontrol==0:
      print("BU IDDE BİR CALİSAN BULUNMAMAKTADIR!")
   for i in guncelle:
      yazilacak.append(i)
   with open("22100011016.txt", "w") as dosya:
      if len(yazilacak)>0:
         for i in range(len(yazilacak)):
           dosya.write("{}-{}-{}-{}-{}-{}\n".format(yazilacak[i][0],yazilacak[i][1],yazilacak[i][2],yazilacak[i][3],yazilacak[i][4],yazilacak[i][5],yazilacak[i][6]))
def zam_hesapla():
   goruntu = []
   bilgi = []
   with open("22100011016.txt", "r") as dosya:
      calisanlar = dosya.readlines()
   for i in calisanlar:
      goruntu.append(" ".join(i[:-1].split("-")))
   a=1
   for i in goruntu:
      print("{}-{}".format(a,i))
      a+=1
   for i in goruntu:
      i = i.split(" ")
      bilgi.append(i)
   secim = input("ZAM YÜZDESİNİ HESAPLAMAK İSTEDİGİNİZ CALİSANİN İDSİNİ GİRİNİZ :")
   kontrol = 0
   yuzde=0
   for i in range(len(bilgi)):
      if secim ==bilgi[i][2]:
         kontrol=1
         yuzde+=((int(bilgi[i][6])-int(bilgi[i][5]))*100)/int(bilgi[i][5])
         print("{} {} İSİMLİ ÇALIŞANIN ZAM YÜZDESİ ={}".format(bilgi[i][0], bilgi[i][1], yuzde))
   if kontrol == 0:
      print("BU IDDE BİR CALİSAN BULUNMAMAKTADIR!")
def en_zam():
   goruntu = []
   bilgi = []
   liste1=[]
   liste2=[]
   sozluk={}
   with open("22100011016.txt", "r") as dosya:
      calisanlar = dosya.readlines()
   for i in calisanlar:
      goruntu.append(" ".join(i[:-1].split("-")))
   for i in goruntu:
      i = i.split(" ")
      bilgi.append(i)
   for i in range(len(bilgi)):
      yuzde=0
      yuzde += ((int(bilgi[i][6]) - int(bilgi[i][5])) * 100) / int(bilgi[i][5])
      liste2.append(yuzde)
   for i in range(len(bilgi)):
      t=bilgi[i][2]
      liste1.append(t)
   for i in range(len(liste1)):
      sozluk[liste1[i]]=liste2[i]
   en_yuksek=sozluk[liste1[0]]
   for i in range(len(liste1)):
      if sozluk[liste1[i]]>en_yuksek:
         en_yuksek=sozluk[liste1[i]]
   p=liste2.index(en_yuksek)
   print("MAAS ZAM YUZDESİ EN YUKSEK OLAN KİSİNİN İSMİ:{} {} ZAM YUZDESİ:{}".format(bilgi[p][0],bilgi[p][1],en_yuksek))
def menu():
   while True:
      islem_liste=[calisan_ekle,calisan_sil,calisan_ara,calisan_guncelle,zam_hesapla,en_zam]
      print("1-ÇALIŞAN EKLE\n2-ÇALIŞAN SİL\n3-ÇALIŞAN ARA\n4-ÇALIŞAN GUNCELLE\n5-ZAM HESAPLA\n6-EN YUKSEK ZAMMI BUL\n7-ÇIKIŞ YAP")
      try:
        secim=int(input("LUTFEN YAPMAK İSTEDİGİNİZ İŞLEMİ SEÇİN:"))
      except ValueError:
        secim = int(input("YANLIŞ VERİ TİPİ.TEKRAR İSTEDİGİNİZ İŞLEMİ SEÇİN:"))
      if secim>7 or secim<1:
         print("GECERSİZ İSLEM GİRDİNİZ!")
         continue
      elif secim==7:
         print("ÇIKIŞ YAPILIYOR...")
         break
      else:
         islem_liste[secim-1]()
menu()
