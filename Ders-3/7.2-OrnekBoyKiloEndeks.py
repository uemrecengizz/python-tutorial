"""
Kategori	BOY KİLO ENDEKSİ - kg/m2
İdeal Kilonun Altı	< 18,49
İdeal Kilo	18.5 - 24,99
İdeal Kilonun Üzeri	25 - 29,99
İdeal Kilonun Çok Üzeri	> 30
"""

boy = float(input("Boyunuzu Yazınız (Örn. 1.70): "))
kilo= int(input("Kilonuzu Yazınız : "))
endeks= kilo/(boy**2)

print(endeks)