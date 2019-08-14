"""
   İbrahim BAYRAMLI tarafından yazılmıştır
   https://sites.google.com/view/ibrahim-bayramli

 """
import math
import time
print("Hazne veri hesaplayıcıya hoşgeldiniz.")
time.sleep(3)
print("Hesaplamalarda sürtünme kayıpları dışındaki bütün kayıplar ihmal edilmiştir. g=9.81 m/sn^2 alınmıştır.")
time.sleep(3)
print("Hesaplamalarda girilecek değerler su yüzü kotunda ve boru uzunluğunda (m), hızda (m/sn), debide (m^3/sn), boru çapında (mm)")
time.sleep(5)

print( "Hesaplama yapılabilmesi için girilmesi gereken veri setleri: ","1) ZA, L, V, D, f (hk, Q ve ZB'yi bulmak için.)" )
print(len("Hesaplama yapılabilmesi için girilmesi gereken veri setleri: ")*" ","2) ZB, L, V, D, f (hk, Q ve ZA'yı bulmak için.)" )
print(len( "Hesaplama yapılabilmesi için girilmesi gereken veri setleri: ")*" ","3) ZA, L, V, Q, f (hk, D ve ZB'yi bulmak için.)" )
print(len( "Hesaplama yapılabilmesi için girilmesi gereken veri setleri: ")*" ","4) ZB, L, V, Q, f (hk, D ve ZA'yı bulmak için.)" )
print(len( "Hesaplama yapılabilmesi için girilmesi gereken veri setleri: ")*" ","5) ZA, L, D, Q, f (hk, V ve ZB'yi bulmak için.)" )
print(len( "Hesaplama yapılabilmesi için girilmesi gereken veri setleri: ")*" ","6) ZB, L, D, Q, f (hk, V ve ZA'yı bulmak için.)" )
print(len( "Hesaplama yapılabilmesi için girilmesi gereken veri setleri: ")*" ","7) ZA, ZB, D, Q, f (hk, V ve L'yi bulmak için.)" )
print(len( "Hesaplama yapılabilmesi için girilmesi gereken veri setleri: ")*" ","8) ZA, ZB, D, V, f (hk, Q ve L'yi bulmak için.)" )
print(len( "Hesaplama yapılabilmesi için girilmesi gereken veri setleri: ")*" ","9) ZA, ZB, V, Q, f (hk, D ve L'yi bulmak için.)" )





while True:
    x=float(input("Lütfen işlem yapmak istediğiniz veri setini seçiniz: "))
    if x==1:
       za=float(input("ZA (metre) değerini giriniz: "))
       if za<0:
           print("Lütfen pozitif bir değer giriniz.")
           za=float(input("ZA (metre) değerini giriniz: "))
       l=float(input("Boru boyunu (L)(metre) giriniz: "))
       if l<0:
           print("Lütfen pozitif bir değer giriniz.")
           l=float(input("Boru boyunu (L)(metre) giriniz: "))
       v=float(input("Borudaki hızı (V)(m/sn) girin: "))
       if v<0:
           print("Lütfen pozitif bir değer giriniz.")
           v=float(input("Borudaki hızı (V)(m/sn) girin: "))
       d=float(input("Boru çapını (D)(mm) giriniz: "))
       if d<0:
           print("Lütfen pozitif bir değer giriniz.")
           d=float(input("Boru çapını (D)(mm) giriniz: "))
       f=float(input("Sürtünme katsayısını (f) giriniz: "))
       if f<0:
           print("Lütfen pozitif bir değer giriniz.")
           f=float(input("Sürtünme katsayısını (f) giriniz: "))

       print("Sonuçlar hesaplanıyor lütfen bekleyiniz...")
       time.sleep(1)
       a=za-(l*v**2*f)/((d/1000)*19.62)                         #ZB kotunu hesaplar
       print("ZB:", a ,"m")                                     #ZB kotunun çıktısı
       print("hk: ",(l*v**2*f)/((d/1000)*19.62),"m")            #hk çıktısı
       print("Q: ", v*(math.pi*(d/1000)**2)/4,"m^3/sn")         #Debi (Q) çıktısı





    if x==2 :
       zb=float(input("ZB (metre) değerini giriniz: "))
       if zb<0:
           print("Lütfen pozitif bir değer giriniz.")
           zb=float(input("ZB değerini giriniz: "))
       l=float(input("Boru boyunu (L)(metre) giriniz: "))
       if l<0:
           print("Lütfen pozitif bir değer giriniz.")
           l=float(input("Boru boyunu (L)(metre) giriniz: "))
       v=float(input("Borudaki hızı (V)(m/sn) girin: "))
       if v<0:
           print("Lütfen pozitif bir değer giriniz.")
           v=float(input("Borudaki hızı (V)(m/sn) girin: "))
       d=float(input("Boru çapını (D)(mm) giriniz: "))
       if d<0:
           print("Lütfen pozitif bir değer giriniz.")
           d=float(input("Boru çapını (D)(mm) giriniz: "))
       f=float(input("Sürtünme katsayısını (f) giriniz: "))
       if f<0:
           print("Lütfen pozitif bir değer giriniz.")
           f=float(input("Sürtünme katsayısını (f) giriniz: "))

       print("Sonuçlar hesaplanıyor lütfen bekleyiniz...")
       time.sleep(1)
       a=zb+(l*v**2*f)/((d/1000)*19.62)                          #ZA kotunu hesaplar
       print("ZA:", a ,"m")                                      #ZA kotunun çıktısı
       print("hk: ",(l*v**2*f)/((d/1000)*19.62),"m")             #hk çıktısı
       print("Q: ", v*(math.pi*(d/1000)**2)/4,"m^3/sn")          #Debi (Q) çıktısı




    if x==3 :
       za=float(input("ZA (metre) değerini giriniz: "))
       if za<0:
           print("Lütfen pozitif bir değer giriniz.")
           za=float(input("ZA (metre) değerini giriniz: "))
       l=float(input("Boru boyunu (L)(metre) giriniz: "))
       if l<0:
           print("Lütfen pozitif bir değer giriniz.")
           l=float(input("Boru boyunu (L)(metre) giriniz: "))
       v=float(input("Borudaki hızı (V)(m/sn) girin: "))
       if v<0:
           print("Lütfen pozitif bir değer giriniz.")
           v=float(input("Borudaki hızı (V)(m/sn) girin: "))
       q=float(input("Borudaki debiyi (Q)(m^3/sn) giriniz: "))
       if q<0:
           print("Lütfen pozitif bir değer giriniz.")
           q=float(input("Borudaki debiyi (Q)(m^3/sn) giriniz: "))
       f=float(input("Sürtünme katsayısını (f) giriniz: "))
       if f<0:
           print("Lütfen pozitif bir değer giriniz.")
           f=float(input("Sürtünme katsayısını (f) giriniz: "))

       print("Sonuçlar hesaplanıyor lütfen bekleyiniz...")
       time.sleep(1)
       d=float((((4*q)/(v*math.pi))**0.5))                        #D yi bulmak için yapılan hesap
       a=za-((f*l*v**2)/(d*19.62))                                #ZB kotunu hesaplar
       c=(f*l*v**2)/(d*19.62)                                     #hk hesaplar
       print("ZB:", a ,"m")                                       #ZB kotunun çıktısı
       print("hk: ", c ,"m")                                      #hk çıktısı
       print("D: ", (1000*l*v**2*f)/(c*19.62) ,"mm")              #Boru çapı (D) çıktısı




    if x==4 :
       zb=float(input("ZB (metre) değerini giriniz: "))
       if zb <0:
           print("Lütfen pozitif bir değer giriniz.")
           za=float(input("ZA (metre) değerini giriniz: "))
       l=float(input("Boru boyunu (L)(metre) giriniz: "))
       if l<0:
           print("Lütfen pozitif bir değer giriniz.")
           l=float(input("Boru boyunu (L)(metre) giriniz: "))
       v=float(input("Borudaki hızı (V)(m/sn) girin: "))
       if v<0:
           print("Lütfen pozitif bir değer giriniz.")
           v=float(input("Borudaki hızı (V)(m/sn) girin: "))
       q=float(input("Borudaki debiyi (Q)(m^3/sn) giriniz:"))
       if q<0:
           print("Lütfen pozitif bir değer giriniz.")
           q=float(input("Borudaki debiyi (Q)(m^3/sn) giriniz: "))
       f=float(input("Sürtünme katsayısını (f) giriniz: "))
       if f<0:
           print("Lütfen pozitif bir değer giriniz.")
           f=float(input("Sürtünme katsayısını (f) giriniz: "))

       print("Sonuçlar hesaplanıyor lütfen bekleyiniz...")
       time.sleep(1)
       d=float(1000*((4*q/(math.pi*v))**0.5))
       a=zb+(l*v**2*f)/((d/1000)*19.62)                         #ZA kotunu hesaplar
       print("ZB:", a ,"m")                                     #ZA kotunun çıktısı
       print("hk: ",(l*v**2*f)/((d/1000)*19.62),"m")            #hk çıktısı
       print("D: ", d ,"mm")                                    #Boru çapı (D) çıktısı




    if x==5:
        za=float(input("ZA değerini giriniz: "))
        if za<0:
            print("Lütfen pozitif bir değer giriniz.")
            za=float(input("ZA değerini giriniz: "))
        l=float(input("Boru boyunu (L)(metre) giriniz: "))
        if l<0:
            print("Lütfen pozitif bir değer giriniz.")
            l=float(input("Boru boyunu (L)(metre) giriniz: "))
        d=float(input("Boru çapını (D)(mm) giriniz: "))
        if d<0:
            print("Lütfen pozitif bir değer giriniz.")
            d=float(input("Boru çapını (D)(mm) giriniz: "))
        q=float(input("Borudaki debiyi (Q)(m^3/sn) giriniz:"))
        if q<0:
            print("Lütfen pozitif bir değer giriniz.")
            q=float(input("Borudaki debiyi (Q)(m^3/sn) giriniz: "))
        f=float(input("Sürtünme katsayısını (f) giriniz: "))
        if f<0:
            print("Lütfen pozitif bir değer giriniz.")
            f=float(input("Sürtünme katsayısını (f) giriniz: "))

        print("Sonuçlar hesaplanıyor lütfen bekleyiniz...")
        time.sleep(1)
        v=float(q/((math.pi*(d/1000)**2)/4))                     #Borudaki hızı (V) heaplar
        a=za-((l*v**2*f)/((d/1000)*19.62))                       #ZB kotunu hesaplar
        print("ZB:", a ,"m")                                     #ZB kotunun çıktısı
        print("hk: ",(l*v**2*f)/((d/1000)*19.62),"m")            #hk çıktısı
        print("V: ", v ,"m/sn")                                  #Boru hızı (V) çıktısı




    if x==6:
       zb=float(input("ZB (metre) değerini giriniz: "))
       if zb<0:
           print("Lütfen pozitif bir değer giriniz.")
           zb=float(input("ZB (metre) değerini giriniz: "))
       l=float(input("Boru boyunu (L)(metre) giriniz: "))
       if l<0:
           print("Lütfen pozitif bir değer giriniz.")
           l=float(input("Boru boyunu (L)(metre) giriniz: "))
       d=float(input("Boru çapını (D)(mm) giriniz: "))
       if d<0:
           print("Lütfen pozitif bir değer giriniz.")
           d=float(input("Boru çapını (D)(mm) giriniz: "))
       q=float(input("Borudaki debiyi (Q)(m^3/sn) giriniz: "))
       if q<0:
           print("Lütfen pozitif bir değer giriniz.")
           q=float(input("Borudaki debiyi (Q)(m^3/sn) giriniz: "))
       f=float(input("Sürtünme katsayısını (f) giriniz: "))
       if f<0:
           print("Lütfen pozitif bir değer giriniz.")
           f=float(input("Sürtünme katsayısını (f) giriniz: "))

       print("Sonuçlar hesaplanıyor lütfen bekleyiniz...")
       time.sleep(1)
       v=float(q/((math.pi*(d/1000)**2)/4))                         #Borudaki hızı (V) heaplar
       a=zb+((l*v**2*f)/((d/1000)*19.62) )                          #ZA kotunu hesaplar
       print("ZA:", a ,"m")                                         #ZA kotunun çıktısı
       print("hk: ",(l*v**2*f)/((d/1000)*19.62),"m")                #hk çıktısı
       print("V: ", v ,"m/s")                                       #Boru çapı (D) çıktısı




    if x==7:
        za=float(input("ZA (metre) değerini giriniz: "))
        if za<0:
            print("Lütfen pozitif bir değer giriniz.")
            za=float(input("ZA (metre) değerini giriniz: "))
        zb=float(input("ZB (metre) değerini giriniz: "))
        if zb<0 :
           print("Lütfen pozitif bir değer giriniz.")
           zb=float(input("ZB (metre) değerini giriniz: "))
        b=za-zb
        if b<0:
            print(za,"<",zb,"olduğu için ZA ve ZB değerlerini yeniden giriniz")
            za=float(input("ZA (metre) değerini giriniz: "))
            zb=float(input("ZB (metre) değerini giriniz: "))
        d=float(input("Boru çapını (D)(mm) giriniz: "))
        if d<0:
           print("Lütfen pozitif bir değer giriniz.")
           d=float(input("Boru çapını (D)(mm) giriniz: "))
        q=float(input("Borudaki debiyi (Q)(m^3/sn) giriniz: "))
        if q<0:
           print("Lütfen pozitif bir değer giriniz.")
           q=float(input("Borudaki debiyi (Q)(m^3/sn) giriniz: "))
        f=float(input("Sürtünme katsayısını (f) giriniz: "))
        if f<0:
           print("Lütfen pozitif bir değer giriniz.")
           f=float(input("Sürtünme katsayısını (f) giriniz: "))

        print("Sonuçlar hesaplanıyor lütfen bekleyiniz...")
        time.sleep(1)
        print("hk: ", b ,"m")                                                          #hk çıktısı
        print("V:", q/(math.pi*(d/1000)**2/4) ,"m/sn")                                 #V çıktısı
        print("L: ", (b*d*19.62)/((q/(math.pi*(d/1000)**2/4))**2*f*1000) , "m")        #L çıktısı



    if x==8:
        za=float(input( "ZA (metre) değerini giriniz: " ))
        if za<0:
            print("Lütfen pozitif bir değer giriniz.")
            za=float(input("ZA (metre) değerini giriniz: "))
        zb=float(input("ZB (metre) değerini giriniz: "))
        if zb<0 :
           print("Lütfen pozitif bir değer giriniz.")
           zb=float(input("ZB (metre) değerini giriniz: "))
        b=za-zb
        if b<0:
            print(za,"<",zb,"olduğu için ZA ve ZB değerlerini yeniden giriniz")
            za=float(input("ZA (metre) değerini giriniz: "))
            zb=float(input("ZB (metre) değerini giriniz: "))
        d=float(input("Boru çapını (D)(mm) giriniz: "))
        if d<0:
           print("Lütfen pozitif bir değer giriniz.")
           d=float(input("Boru çapını (D)(mm) giriniz: "))
        v=float(input("Borudaki hızı (V)(m/sn) girin: "))
        if v<0:
           print("Lütfen pozitif bir değer giriniz.")
           v=float(input("Borudaki hızı (V)(m/sn) girin: "))
        f=float(input("Sürtünme katsayısını (f) giriniz: "))
        if f<0:
           print("Lütfen pozitif bir değer giriniz.")
           f=float(input("Sürtünme katsayısını (f) giriniz: "))
        q=v*((math.pi*d**2)/4)
        print("Sonuçlar hesaplanıyor lütfen bekleyiniz...")
        time.sleep(1)
        print("hk: ",b,"m")                                                   #hk çıktısı
        print( "Q:" , v*(math.pi*(d/1000)**2/4), "m^3/sn" )                   #V çıktısı
        print( "L: " , (b*d*19.62)/(v**2*f*1000) )                            #L çıktısı



    if x==9:
        za=float(input("ZA (metre) değerini giriniz: "))
        if za<0:
            print("Lütfen pozitif bir değer giriniz.")
            za=float(input("ZA (metre) değerini giriniz: "))
        zb=float(input("ZB (metre) değerini giriniz: "))
        if zb<0 :
           print("Lütfen pozitif bir değer giriniz.")
           zb=float(input("ZB (metre) değerini giriniz: "))
        b=za-zb          #b diğer bir değişle hk yük kaybına eşit
        if b<0:
            print(za,"<",zb,"olduğu için ZA ve ZB değerlerini yeniden giriniz")
            za=float(input("ZA (metre) değerini giriniz: "))
            zb=float(input("ZB (metre) değerini giriniz: "))
        d=float(input("Boru çapını (D)(mm) giriniz: "))
        if d<0:
           print("Lütfen pozitif bir değer giriniz.")
           d=float(input("Boru çapını (D)(mm) giriniz: "))
        v=float(input("Borudaki hızı (V)(m/sn) girin: "))
        if v<0:
           print("Lütfen pozitif bir değer giriniz.")
           v=float(input("Borudaki hızı (V)(m/sn) girin: "))
        f=float(input("Sürtünme katsayısını (f) giriniz: "))
        if f<0:
           print("Lütfen pozitif bir değer giriniz.")
           f=float(input("Sürtünme katsayısını (f) giriniz: "))

        print("Sonuçlar hesaplanıyor lütfen bekleyiniz...")
        time.sleep(1)
        print("hk: ",b,"m")                                              #hk çıktısı
        print("Q:",v*((math.pi*(d/1000)**2)/4),"m^3/sn")                 #Q çıktısı
        print("L: ",(b*d*19.62)/(f*v**2*1000))                           #L çıktısı




















