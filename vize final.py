"""

   İbrahim BAYRAMLI tarafından yazılmıştır
   https://sites.google.com/view/ibrahim-bayramli
   
 """

while True:
    a=float(input("Vize Notunuzu Giriniz: "))

    while a<0 or a>100:
        print("0-100 arasında bir not giriniz...")
        a=float(input("Vize Notunuzu Giriniz: "))

    b=float(input("Final Notunuzu Giriniz: "))

    while b<0 or b>100:
        print("0-100 arasında bir not giriniz...")
        b=float(input("Final Notunuzu Giriniz: "))

    c=0.4*a+0.6*b

    if b<50:
        print("Notunuz: ",c," FF")
    elif 45<=c<=49.9:
        print("Notunuz: ",c," DD")
    elif 50<=c<=54.9:
        print("Notunuz: ",c," DC")
    elif 55<=c<=59.9:
        print("Notunuz: ",c," CC")
    elif 60<=c<=64.9:
        print("Notunuz: ",c," CB")
    elif 65<=c<=69.9:
        print("Notunuz: ",c," BB")
    elif 70<=c<=79.9:
        print("Notunuz: ",c," BA")
    elif 80<=c:
        print("Notunuz: ",c," AA")
    else:
        print("Notunuz: ",c," FF")
