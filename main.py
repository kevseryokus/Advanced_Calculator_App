
print("""
[1] Toplama
[2] Çıkarma
[3] Çarpma
[4] Bölme
[5] Üs Alma
[Q] Çıkış

    """)



giris = input("Hangi işlemi yaptırmak istiyorsunuz: ")
if giris =="1":
    x =input("ilk sayı   : ")
    x=float(x)
    y =input("ikinci sayı: ")
    y = float(y)
    print("İşlem sonucu: ",x+y)


elif giris =="2":
    x =input("ilk sayı   : ")
    x=float(x)
    y =input("ikinci sayı: ")
    y = float(y)
    print("İşlem sonucu: ",x-y)


elif giris =="3":
    x =input("ilk sayı   : ")
    x=float(x)
    y =input("ikinci sayı: ")
    y = float(y)
    print("İşlem sonucu: ",x*y)


elif giris =="4":
    x =input("ilk sayı   : ")
    x=float(x)
    y =input("ikinci sayı: ")
    y = float(y)
    print("İşlem sonucu: ",x/y)


elif giris =="5":
    x =input("Taban   : ")
    x = float(x)
    y =input("Kuvvet= ")
    y = int(y)
    print("İşlem sonucu: ",x**y)

elif giris =="q" or giris =="Q":
    print("Çıkılıyor...")
    quit()

else:
    print("Hatalı girdiniz...")
    quit()

#Notlarım:
#if/else yaptığımızda hata aldık. çünkü en sondaki else bir önceki if'e aitti. Bunu engellemek için 1.yi if ortadakileri elif en sondakini else ile değiştiridik.
#elif else ile if'in birleşimidir. Örneğin 1 değilse ve 2 ise demek. Biri gerçekleştiğinde diğer hiçbiri sorgulanmayacak. İF İF yazsaydık gerçekleşse bile tek tek okunurdu. işlem hızı kazandırdı.
#elif ile elene elene sona gidecektir. En sonda else ile karşılaştığında bir üsttekine bakacak. Hepsi elendi sonuncu da değilse else mesajını ekrana yansıtır.