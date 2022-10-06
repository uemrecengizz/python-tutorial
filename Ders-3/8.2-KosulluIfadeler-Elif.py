#elif
#Syntax'ı
"""
if koşul:
    yapılacak işlem:
elif koşul2:
    yapılacak işlem
elif koşul3:
    yapılacak işlem
.
.
.
.
.
.
elif koşulX:
    yapılacak işlem
"""
boy = int(input("Boyunuzu yazınız..."))
if boy<160:
    print("Boyunuz kısa...")
elif boy<170:
    print("Boyunuz normal...")
elif boy<180:
    print("Boyunuz uzun")
else:
    print("Hay Maşallah.")