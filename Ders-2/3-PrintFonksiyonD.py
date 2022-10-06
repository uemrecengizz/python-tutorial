#SEP , print fonksiyonundaki boşlukları değiştirir.

print("www","google","com",sep="")
print("T","C",sep=".")

#Kendin Yap!
 # 1- Şehirler yazıp aralarına "-" koydurun. 
 # 2- Rakam yazdırıp aralarına "mumdur yazdırın." 

#-------------------------------------------------
#END (\n) , satır sonu demektir. Nereye yazılırsa sonrasındaki yazıları alt satıra atar.

print("Elma \nArmut \nKiraz \nVişne")
print("Birinci satır,\nİkinci satır,\nÜçüncü satır,")

#--------------------------------------------------
#FİLE

dosya=open("test.txt","w") #dosya diye değişken tanımladık . 
#Open komutunun oluşturacağı txt dosyasının adını yazdık.
#Ek olarak W ilede write yani dosyaya yazı yazılacak şeklinde ayar yaptık.
print("Bu yazı notepade yazılması için ayarlandı.",file=dosya)
print("Emre",file=dosya)
print("Doğum Tarihi : 17.09.1993",file=dosya)
print
#Bu kısımda txt dosyasının içerisine yazılacak yazıyı yazdık. 
#2. olarak file komutu ile hangi TXT dosyası olduğunu söyledik.
dosya.close() #işlemler bitti. TXT dosyasını kapat dedik.
