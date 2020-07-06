#İbrahim BAYRAMLI
#Manning denklemine göre debi hesaplayıcı.
#Çeşit kenar trapez kesitte hesap yapılırken d1 soldaki açı d2 ise sağdaki açıdır.

import math

print("1- Çeşit Kenar Trapez Kesit")
print("2- İkiz Kenar Trapez Kesit")
print("3- Dairesel Kesit")
print("4- Dikdörtgen Kesit")

a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
while not (a==1 and a==2 and a==3 and a==4):
    print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
    print("1- Çeşit Kenar Trapez Kesit")
    print("2- İkiz Kenar Trapez Kesit")
    print("3- Dairesel Kesit")
    print("4- Dikdörtgen Kesit")
    a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))

    while (a == 1 or a == 2 or a == 3 or a == 4):

        if a == 1:                                                                                                       # çeşit kenar trapez için
            print("Çeşit Kenar Trapez Kesit Seçtiniz.")
            d1=float(input("D1 Şev eğimini giriniz (Derece):"))
            while (d1<0 or d1>360):
                print("0-360 Derece Arasında Bir Açı Giriniz.")
                d1 = float(input("D1 Şev eğimini giriniz (Derece):"))
            d2 = float(input("D2 Şev eğimini giriniz (Derece):"))
            while (d2<0 or d2>360):
                print("0-360 Derece Arasında Bir Açı Giriniz.")
                d2 = float(input("D2 Şev eğimini giriniz (Derece):"))
            if (d1>90 and d2>90):
                B = float(input("Taban Genişliği Girin(Metre):"))                                                        # taban genişliği metre
                h = float(input("Yüksekliği Girin(Metre):"))                                                             # yükseklik metre
                S0 = float(input("Taban Eğimini Girin:"))                                                                # taban eğimi
                n = float(input("Manning Prüzlülük Katsayısını Giriniz:"))                                               # manning prüzlülük katsayısı
                A=float(B*h-0.5*(((h**2)*(math.tan((d1-90)*math.pi/180)))+((h**2)*(math.tan((d2-90)*math.pi/180)))))     # ıslak alan m^2
                print("Islak Alan:", A ,"m^2")
                P=float(B+((((h**2)+(h*math.tan((d1-90)*math.pi/180)))**0.5)+(((h**2)+(h*math.tan((d2-90)*math.pi/180)))**0.5)))    # ıslak çevre m
                print("Islak Çevre:",P,"m")
                Q = float(((1 / n) * (((A) ** (5 / 3)) / (P / (2 / 3))) * ((S0) ** (0.5))))                              # debi m^3/sn
                q = float(Q / B)                                                                                         # brim genişlikten geçen debi m^3/sn/m
                print("Brim Genişlikten Geçen Debi:", q, "m^3/sn/m")
                hkr = float(((q ** 2) / 9.81)**(1 / 3))                                                                  # kritik yükseklik metre
                print("Kritik Yükseklik:", hkr, "m")

                a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
                while not (a == 1 or a == 2 or a == 3 or a == 4):
                    print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
                    print("1- Çeşit Kenar Trapez Kesit")
                    print("2- İkiz Kenar Trapez Kesit")
                    print("3- Dairesel Kesit")
                    print("4- Dikdörtgen Kesit")
                    a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))

            elif (d1>90 and d2==90):
                B = float(input("Taban Genişliği Girin(Metre):"))                                                        # taban genişliği metre
                h = float(input("Yüksekliği Girin(Metre):"))                                                             # yükseklik metre
                S0 = float(input("Taban Eğimini Girin:"))                                                                # taban eğimi
                n = float(input("Manning Prüzlülük Katsayısını Giriniz:"))                                               # manning prüzlülük katsayısı
                A=float(B*h+0.5*((h**2)*(math.tan((d1-90)*math.pi/180))))                                                # ıslak alan m^2
                print("Islak Alan:",A,"m^2")
                P= float(B+h+(((h**2)+(h*math.tan((d1-90)*math.pi/180))**2)**0.5))                                       # ıslak çevre m
                print("Islak Çevre:",P,"m")
                Q = float(((1 / n) * (((A) ** (5 / 3)) / (P / (2 / 3))) * ((S0) ** (0.5))))                              # debi m^3/sn
                q = float(Q / B)                                                                                         # brim genişlikten geçen debi m^3/sn/m
                print("Brim Genişlikten Geçen Debi:", q, "m^3/sn/m")
                hkr = float((q ** 2 / 9.81) ** (1 / 3))                                                                  # kritik yükseklik metre
                print("Kritik Yükseklik:", hkr, "m")

                a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
                while not (a == 1 or a == 2 or a == 3 or a == 4):
                    print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
                    print("1- Çeşit Kenar Trapez Kesit")
                    print("2- İkiz Kenar Trapez Kesit")
                    print("3- Dairesel Kesit")
                    print("4- Dikdörtgen Kesit")
                    a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))

            elif (d2 > 90 and d1 == 90):
                B = float(input("Taban Genişliği Girin(Metre):"))                                                        # taban genişliği metre
                h = float(input("Yüksekliği Girin(Metre):"))                                                             # yükseklik metre
                S0 = float(input("Taban Eğimini Girin:"))                                                                # taban eğimi
                n = float(input("Manning Prüzlülük Katsayısını Giriniz:"))                                               # manning prüzlülük katsayısı
                A = float(B * h + 0.5 * ((h ** 2) * (math.tan((d2-90) * math.pi / 180))))                                # ıslak alan m^2
                print("Islak Alan:", A, "m^2")
                P = float(B + h + (((h ** 2) + (h * math.tan((d2-90) * math.pi / 180)) ** 2) ** 0.5))                    # ıslak çevre m
                print("Islak Çevre:", P, "m")
                Q = float(((1 / n) * (((A) ** (5 / 3)) / (P / (2 / 3))) * ((S0) ** (0.5))))                              # debi m^3/sn
                q = float(Q / B)                                                                                         # brim genişlikten geçen debi m^3/sn/m
                print("Brim Genişlikten Geçen Debi:", q, "m^3/sn/m")
                hkr = float((q ** 2 / 9.81) ** (1 / 3))                                                                  # kritik yükseklik metre
                print("Kritik Yükseklik:", hkr, "m")

                a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
                while not (a == 1 or a == 2 or a == 3 or a == 4):
                    print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
                    print("1- Çeşit Kenar Trapez Kesit")
                    print("2- İkiz Kenar Trapez Kesit")
                    print("3- Dairesel Kesit")
                    print("4- Dikdörtgen Kesit")
                    a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))

            elif (d1<90 and d2<90):
                B = float(input("Taban Genişliği Girin(Metre):"))                                                        # taban genişliği metre
                h = float(input("Yüksekliği Girin(Metre):"))                                                             # yükseklik metre
                S0 = float(input("Taban Eğimini Girin:"))                                                                # taban eğimi
                n = float(input("Manning Prüzlülük Katsayısını Giriniz:"))                                               # manning prüzlülük katsayısı
                A=float(B*h+0.5((h**2)/(math.tan((d1)*math.pi/180)+math.tan((d2)*math.pi/180))))                         # ıslak alan m^2
                print("Islak Alan:",A,"m^2")
                P=float(B+(((h**2)+(h/math.tan((d1)*math.pi/180))**2)**0.5)+(((h**2)+(h*math.tan((d2)*math.pi/180))**2)**0.5))    # ıslak çevre m
                print("Islak Çevre:",P,"m")
                Q = float(((1 / n) * (((A) ** (5 / 3)) / (P / (2 / 3))) * ((S0) ** (0.5))))                              # debi m^3/sn
                q = float(Q / B)                                                                                         # brim genişlikten geçen debi m^3/sn/m
                print("Brim Genişlikten Geçen Debi:", q, "m^3/sn/m")
                hkr = float((q ** 2 / 9.81) ** (1 / 3))                                                                  # kritik yükseklik metre
                print("Kritik Yükseklik:", hkr, "m")

                a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
                while not (a == 1 or a == 2 or a == 3 or a == 4):
                    print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
                    print("1- Çeşit Kenar Trapez Kesit")
                    print("2- İkiz Kenar Trapez Kesit")
                    print("3- Dairesel Kesit")
                    print("4- Dikdörtgen Kesit")
                    a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
            elif (d1==90 and d2<90):
                B = float(input("Taban Genişliği Girin(Metre):"))                                                        # taban genişliği metre
                h = float(input("Yüksekliği Girin(Metre):"))                                                             # yükseklik metre
                S0 = float(input("Taban Eğimini Girin:"))                                                                # taban eğimi
                n = float(input("Manning Prüzlülük Katsayısını Giriniz:"))                                               # manning prüzlülük katsayısı
                A = float(B*h-(0.5*(h*math.tan((d2)*math.pi/180))**2))                                                # ıslak alan m^2
                print("Islak Alan:",A,"m^2")
                P=float(B+h+(((h**2)+(h/math.tan((d2)*math.pi/180)))**0.5))                                           # ıslak çevre m
                print("Islak Çevre:",P,"m")
                Q = float(((1 / n) * (((A) ** (5 / 3)) / (P / (2 / 3))) * ((S0) ** (0.5))))                              # debi m^3/sn
                q = float(Q / B)                                                                                         # brim genişlikten geçen debi m^3/sn/m
                print("Brim Genişlikten Geçen Debi:", q, "m^3/sn/m")
                hkr = float((q ** 2 / 9.81) ** (1 / 3))                                                                  # kritik yükseklik metre
                print("Kritik Yükseklik:", hkr, "m")
                a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
                while not (a == 1 or a == 2 or a == 3 or a == 4):
                    print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
                    print("1- Çeşit Kenar Trapez Kesit")
                    print("2- İkiz Kenar Trapez Kesit")
                    print("3- Dairesel Kesit")
                    print("4- Dikdörtgen Kesit")
                    a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
            elif (d2==90 and d1<90):
                B = float(input("Taban Genişliği Girin(Metre):"))                                                        # taban genişliği metre
                h = float(input("Yüksekliği Girin(Metre):"))                                                             # yükseklik metre
                S0 = float(input("Taban Eğimini Girin:"))                                                                # taban eğimi
                n = float(input("Manning Prüzlülük Katsayısını Giriniz:"))                                               # manning prüzlülük katsayısı
                A = float(B * h - (0.5 * (h * math.tan((d2) * math.pi / 180)) ** 2))                                     # ıslak alan m^2
                print("Islak Alan:", A, "m^2")
                P = float(B + h + (((h ** 2) + (h / math.tan((d2) * math.pi / 180))) ** 0.5))                            # ıslak çevre m
                print("Islak Çevre:", P, "m")
                Q = float(((1 / n) * (((A) ** (5 / 3)) / (P / (2 / 3))) * ((S0) ** (0.5))))                              # debi m^3/sn
                q = float(Q / B)                                                                                         # brim genişlikten geçen debi m^3/sn/m
                print("Brim Genişlikten Geçen Debi:", q, "m^3/sn/m")
                hkr = float((q ** 2 / 9.81) ** (1 / 3))                                                                  # kritik yükseklik metre
                print("Kritik Yükseklik:", hkr, "m")
                a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
                while not (a == 1 or a == 2 or a == 3 or a == 4):
                    print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
                    print("1- Çeşit Kenar Trapez Kesit")
                    print("2- İkiz Kenar Trapez Kesit")
                    print("3- Dairesel Kesit")
                    print("4- Dikdörtgen Kesit")
                    a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))

            elif (d1==90 and d2==90):
                B = float(input("Taban Genişliği Girin(Metre):"))                                                        # taban genişliği metre
                h = float(input("Yüksekliği Girin(Metre):"))                                                             # yükseklik metre
                S0 = float(input("Taban Eğimini Girin:"))                                                                # taban eğimi
                n = float(input("Manning Prüzlülük Katsayısını Giriniz:"))                                               # manning prüzlülük katsayısı
                A = float(B * h)                                                                                         # ıslak alan m^2
                P = float(B + 2 * h)                                                                                     # ıslak çevre m
                print("Islak Alan:", A, "m^2")
                print("Islak Çevre:", P, "m")
                Q = float(((1 / n) * (((A) ** (5 / 3)) / (P / (2 / 3))) * ((S0) ** (0.5))))                              # debi m^3/sn
                print("Debi:", Q, "m^3/sn")
                q = float(Q / B)                                                                                         # birim genişlikten geçen debi m^3/sn/m
                print("Birim Genişlikten Geçen Debi:", q, "m^3/sn/m")
                hkr = float((q ** 2 / 9.81) ** (1 / 3))                                                                  # kritik yükseklik metre
                print("Kritik Yükseklik:", hkr, "m")

                a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
                while not (a == 1 or a == 2 or a == 3 or a == 4):
                    print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
                    print("1- Çeşit Kenar Trapez Kesit")
                    print("2- İkiz Kenar Trapez Kesit")
                    print("3- Dairesel Kesit")
                    print("4- Dikdörtgen Kesit")
                    a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
            elif (d1<90 and d2>90):
                B = float(input("Taban Genişliği Girin(Metre):"))                                                        # taban genişliği metre
                h = float(input("Yüksekliği Girin(Metre):"))                                                             # yükseklik metre
                S0 = float(input("Taban Eğimini Girin:"))                                                                # taban eğimi
                n = float(input("Manning Prüzlülük Katsayısını Giriniz:"))                                               # manning prüzlülük katsayısı
                A=float(B*h+0.5((h**2)*math.tan(d2*math.pi/180)-(h**2)*math.tan((d2-90)*math.pi/180)))




        elif a == 2:                                                                                                     # trapez kesit
            print("Trapez Kesit Seçtiniz.")
            d = float(input("Şev Eğim Derecesini Seçin(Derece):"))
            while (d<0 or d>360):
                print("0-360 Derece Arasında Bir Açı Giriniz.")
                d = float(input("Şev Eğim Derecesini Seçin(Derece):"))

            if d > 90:
                B = float(input("Taban Genişliği Girin(Metre):"))                                                        # taban genişliği metre
                h = float(input("Yüksekliği Girin(Metre):"))                                                             # yükseklik metre
                S0 = float(input("Taban Eğimini Girin:"))                                                                # taban eğimi
                n = float(input("Manning Prüzlülük Katsayısını Giriniz:"))                                               # manning prüzlülük katsayısı
                A = float(B * h + 2 * (0.5 * (h * (h / math.tan((d-90) * math.pi / 180)))))                              # ıslak alan
                print("Islak Alan:", A, "m^2")
                P = float(B + ((h ** 2) + ((h / math.tan((d-90) * math.pi / 180)) ** 2)) ** 0.5)
                print("Islak Çevre:", P, "m")
                Q = float(((1 / n) * (((A) ** (5 / 3)) / (P / (2 / 3))) * ((S0) ** (0.5))))                              # debi m^3/sn
                q = float(Q / B)                                                                                         # brim genişlikten geçen debi m^3/sn/m
                print("Brim Genişlikten Geçen Debi:", q, "m^3/sn/m")
                hkr = float((q ** 2 / 9.81) ** (1 / 3))                                                                  # kritik yükseklik metre
                print("Kritik Yükseklik:", hkr, "m")

                a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
                while not (a == 1 or a == 2 or a == 3 or a == 4):
                    print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
                    print("1- Çeşit Kenar Trapez Kesit")
                    print("2- İkiz Kenar Trapez Kesit")
                    print("3- Dairesel Kesit")
                    print("4- Dikdörtgen Kesit")
                    a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))

            elif d == 90:
                B = float(input("Taban Genişliği Girin(Metre):"))                                                        # taban genişliği metre
                h = float(input("Yüksekliği Girin(Metre):"))                                                             # yükseklik metre
                S0 = float(input("Taban Eğimini Girin:"))                                                                # taban eğimi
                n = float(input("Manning Prüzlülük Katsayısını Giriniz:"))                                               # manning prüzlülük katsayısı
                A = float(B * h)                                                                                         # ıslak alan m^2
                P = float(B + 2 * h)                                                                                     # ıslak çevre m
                print("Islak Alan:", A, "m^2")
                print("Islak Çevre:", P, "m")
                Q = float(((1 / n) * (((A) ** (5 / 3)) / (P / (2 / 3))) * ((S0) ** (0.5))))                              # debi m^3/sn
                print("Debi:", Q, "m^3/sn")
                q = float(Q / B)                                                                                         # birim genişlikten geçen debi m^3/sn/m
                print("Birim Genişlikten Geçen Debi:", q, "m^3/sn/m")
                hkr = float((q ** 2 / 9.81) ** (1 / 3))                                                                  # kritik yükseklik metre
                print("Kritik Yükseklik:", hkr, "m")
                a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))

                while not (a == 1 or a == 2 or a == 3 or a == 4):
                    print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
                    print("1- Çeşit Kenar Trapez Kesit")
                    print("2- İkiz Kenar Trapez Kesit")
                    print("3- Dairesel Kesit")
                    print("4- Dikdörtgen Kesit")
                    a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))

            elif d<90:
                B = float(input("Taban Genişliği Girin(Metre):"))                                                        # taban genişliği metre
                h = float(input("Yüksekliği Girin(Metre):"))                                                             # yükseklik metre
                S0 = float(input("Taban Eğimini Girin:"))                                                                # taban eğimi
                n = float(input("Manning Prüzlülük Katsayısını Giriniz:"))                                               # manning prüzlülük katsayısı
                A = float(B * h - (((h ** 2) + (h / math.tan(d * math.pi / 180)) ** 2) ** 0.5))                          # ıslak alan m^2
                print("Islak Alan:", A, "m^2")
                P = float(B + 2 * (((h ** 2) + (h / math.tan(d * math.pi / 180)) ** 2) ** 0.5))                          # ıslak çevre
                print("Islak Çevre:", P, "m")
                Q = float(((1 / n) * (((A) ** (5 / 3)) / (P / (2 / 3))) * ((S0) ** (0.5))))                              # debi m^3/sn
                print("Debi:", Q, "m^3/sn")
                q = float(Q / B)                                                                                         # brim genişlikten geçen debi m^3/sn/m
                print("Brim Genişlikten Geçen Debi:", q, "m^3/sn/m")
                hkr = float((q ** 2 / 9.81) ** (1 / 3))                                                                  # kritik yükseklik metre
                print("Kritik Yükseklik:", q, "m")

                a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
                while not (a == 1 or a == 2 or a == 3 or a == 4):
                    print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
                    print("1- Çeşit Kenar Trapez Kesit")
                    print("2- İkiz Kenar Trapez Kesit")
                    print("3- Dairesel Kesit")
                    print("4- Dikdörtgen Kesit")
                    a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))

        elif a == 3:                                                                                                     # dairesel kesit
            """dairesel kesit için kritik derinliğin nasıl bulunacağını öğren!
            birim genişlik debisinin nasıl bulunacağını öğren!"""

            print("Dairesel Kesit Seçtiniz.")
            r = float(input("Yarıçap Girin (m):"))                                                                       # yarıçap m
            h = float(input("Yüksekliği Girin (m):"))                                                                    # yükseklik m
            while h >= 2 * r:
                print("Uygunsuz Kesit Tekrar Giriş Yapın:")
                r = float(input("Yarıçap Girin (m):"))
                h = float(input("Yüksekliği Girin (m):"))

            if h == r:
                n = float(input("Manning Prüzlülük Katsayısını Girin:"))                                                 # manning prüzlülük katsayısı
                S0 = float(input("Taban Eğimini Girin"))                                                                 # taban eğimi
                A = float(math.pi * (r ** 2) * 0.5)                                                                      # ıslak alan m^2
                print("Islak Alan:", A, "m^2")
                P = float(math.pi * 2 * r * 0.5)                                                                         # ıslak çevre metre
                print("Islak Çevre:", P, "m")
                Q = float(((1 / n) * (((A) ** (5 / 3)) / (P / (2 / 3))) * ((S0) ** (0.5))))                              # debi m^3/sn
                print("Debi:", Q, "m^3/sn")

                a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
                while not (a == 1 or a == 2 or a == 3 or a == 4):
                    print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
                    print("1- Çeşit Kenar Trapez Kesit")
                    print("2- İkiz Kenar Trapez Kesit")
                    print("3- Dairesel Kesit")
                    print("4- Dikdörtgen Kesit")
                    a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))

            elif h < r:
                alfa = float(math.acos((h - r) / r))
                n = float(input("Manning Prüzlülük Katsayısını Girin:"))
                S0 = float(input("Taban Eğimini Girin:"))
                A = float(((math.pi * (r ** 2) * 2 * alfa) - 0.5 * (r ** 2) * math.sin(2 * alfa)))                       # ıslak alan m^2
                print("Islak Alan:", A, "m^2")
                P = float((2 * math.pi * r * 2 * alfa) / (2 * math.pi))                                                  # ıslak çevre metre
                print("Islak Çevre:", P, "m")
                Q = float(((1 / n) * (((A) ** (5 / 3)) / (P / (2 / 3))) * ((S0) ** (0.5))))                              # debi m^3/sn
                print("Debi:", Q, "m^3/sn")

                a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
                while not (a == 1 or a == 2 or a == 3 or a == 4):
                    print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
                    print("1- Çeşit Kenar Trapez Kesit")
                    print("2- İkiz Kenar Trapez Kesit")
                    print("3- Dairesel Kesit")
                    print("4- Dikdörtgen Kesit")
                    a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))

            elif h > r:
                alfa = float(math.acos((h-r) / r))
                n = float(input("Manning Prüzlülük Katsayısını Girin:"))
                S0 = float(input("Taban Eğimini Girin:"))
                A = float(((math.pi * (r ** 2)) - (((math.pi * (r ** 2) * 2 * alfa) / (math.pi * 2)) - 0.5 * (r ** 2) * math.sin(2 * alfa))))  # ıslak alan m^2
                print("Islak Alan:", A, "m^2")
                P = float((2 * math.pi * r) - ((2 * math.pi * r * 2 * alfa) / (2 * math.pi)))                            # ıslak çevre metre
                print("Islak Çevre:", P, "m")
                Q = float(((1 / n) * (((A) ** (5 / 3)) / (P / (2 / 3))) * ((S0) ** (0.5))))                              # debi m^3/sn
                print("Debi:", Q, "m^3/sn")

                a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
                while not (a == 1 or a == 2 or a == 3 or a == 4):
                    print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
                    print("1- Çeşit Kenar Trapez Kesit")
                    print("2- İkiz Kenar Trapez Kesit")
                    print("3- Dairesel Kesit")
                    print("4- Dikdörtgen Kesit")
                    a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))

        elif a == 4:                                                                                                     #dikdörtgen kesit
            print("Dikdörtgen Kesit Seçtiniz.")
            B = float(input("Taban Genişliği Girin(Metre):"))                                                            # taban genişliği metre
            h = float(input("Yüksekliği Girin(Metre):"))                                                                 # yükseklik metre
            S0 = float(input("Taban Eğimini Girin:"))                                                                    # taban eğimi
            n = float(input("Manning Prüzlülük Katsayısını Giriniz:"))                                                   # manning prüzlülük katsayısı
            A = float(B * h)                                                                                             # ıslak alan m^2
            P = float(B + 2 * h)                                                                                         # ıslak çevre m
            print("Islak Alan:", A, "m^2")
            print("Islak Çevre:", P, "m")
            Q = float(((1 / n) * (((A) ** (5 / 3)) / (P / (2 / 3))) * ((S0) ** (0.5))))                                  # debi m^3/sn
            print("Debi:", Q, "m^3/sn")
            q = float(Q / B)                                                                                             # birim genişlikten geçen debi m^3/sn/m
            print("Birim Genişlikten Geçen Debi:", q, "m^3/sn/m")
            hkr = float((q ** 2 / 9.81) ** (1 / 3))                                                                      # kritik yükseklik metre
            print("Kritik Yükseklik:", hkr, "m")

            a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
            while not (a == 1 or a == 2 or a == 3 or a == 4):
                print("Geçersiz Seçim Geçerli Bir Kesit Seçin!")
                print("1- Çeşit Kenar Trapez Kesit")
                print("2- İkiz Kenar Trapez Kesit")
                print("3- Dairesel Kesit")
                print("4- Dikdörtgen Kesit")
                a = int(input("Lütfen işlem yapmak istediğiniz kesiti seçin:"))
