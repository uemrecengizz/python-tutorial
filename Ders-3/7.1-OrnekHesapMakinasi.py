#Basit hesap makinası

gSayi= int(input("Lütfen ilk sayınızı yazınız."))
gSayi2=int(input("Lütfen ikinci sayınızı yazınız"))

toplam = gSayi+gSayi2
cikarma= gSayi-gSayi2
carpma= gSayi*gSayi2
bolme=gSayi/gSayi2
bKalan=gSayi%gSayi2
ussu=(gSayi+gSayi2)**2
bTamsayi=gSayi//gSayi2

print("Toplama işlemi : ", toplam)
print("Çıkarma işlemi : ", cikarma)
print("Çarpma işlemi : ", carpma)
print("Bölme işlemi : ", bolme)
print("Bölümün tam sayı sonucu : ", bTamsayi)
print("Bölümden Kalan : " ,bKalan)
print("Üssü ( 2 sayının toplamının karesini alır ) işlemi : ", ussu)