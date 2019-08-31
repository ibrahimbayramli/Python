"""
İbrahim BAYRAMLI
https://sites.google.com/view/ibrahim-bayramli
"""


import math
while True:

    a=float(input("A kenarının uzunluğunu girin: "))
    b=float(input("B kenarının uzunluğunu girin: "))
    c=float(input("C kenarının uzunluğunu girin: "))

    while True :





        if abs((a-b))>c or (a+b)<c :

            print("Böyle bir üçgen oluşturulamaz. Oluşturulabilecek bir üçgen seçiniz.")
            a=float(input("A kenarının uzunluğunu girin: "))
            b=float(input("B kenarının uzunluğunu girin: "))
            c=float(input("C kenarının uzunluğunu girin: "))

        if abs((a-c))>b or (a+c)<b :

            print("Böyle bir üçgen oluşturulamaz. Oluşturulabilecek bir üçgen seçiniz.")
            a=float(input("A kenarının uzunluğunu girin: "))
            b=float(input("B kenarının uzunluğunu girin: "))
            c=float(input("C kenarının uzunluğunu girin: "))

        if abs((b-c))>a or (b+c)<a :

            print("Böyle bir üçgen oluşturulamaz. Oluşturulabilecek bir üçgen seçiniz.")
            a=float(input("A kenarının uzunluğunu girin: "))
            b=float(input("B kenarının uzunluğunu girin: "))
            c=float(input("C kenarının uzunluğunu girin: "))
        else :
            u=(a+b+c)/2
            alan= (u*(u-a)*(u-b)*(u-c))**0.5
            print("Hesaplanan alan : ",alan)
            break


