

#1.soru
#print("merhaba yapay zeka!")



#2.soru
#isim = input("kullanici adiniz lutfen : ")
#print(f"merhaba ,{isim}! python ogrenmeye hosgeldin ")



#3.soru
# isim = "ahmet"
# sınav1 = 80
# sınav2 = 75
# ort = 77.5
# durum = True




#4.soru
# sayi1 = int(input("birinci sayisi giriniz : "))
# sayi2 = int(input("ikinci sayisi giriniz : "))
#
# def cokluhesaplama(sayi1,sayi2):
#     toplam = sayi1+sayi2
#     fark = abs(sayi1-sayi2)
#     carpim = sayi1*sayi2
#     print(f"sonuclar : toplam = {toplam}, fark = {fark}, carpim = {carpim}")
#
# cokluhesaplama(sayi1,sayi2)




#5.soru
# sayi1 = 50.5
# int(sayi1)
# print(type(sayi1))
#

# sayi2 = "54"
# int(sayi2)
# print(type(sayi2))




#6.soru
# cumle = input("cumlenizi giris yapiniz : ")
# print(cumle)
# cumle = cumle.upper()
# print(cumle)

#7.soru
# sepetiniz = []
# def urun_ekle():
#     urun = input("urun adi giriniz : ")
#     sepetiniz.append(urun)
# def urun_sil():
#     silinecek_urun = input("silinecek urun adini giriniz :")
#     sepetiniz.remove(silinecek_urun)
# def sepet_listele():
#     print(sepetiniz)
#
# urun_ekle()
# urun_ekle()
# urun_ekle()
# urun_sil()
# sepet_listele()



#8.soru
# yas = int(input("lutfen yasinizi giriniz :"))
#
# if yas >= 18:
#     print("ehliyet alabilirsiniz...")
# else:
#     print("ehliyet alamazsiniz...")






#9.soru
# import random
#
# rastgele_sayi = random.randint(1,10)
# print("5 TAHMIN HAKKINIZ VARDIR")
# hak = 5
#
# while hak > 0:
#     tahmin_edilen_sayi = int(input("1-10 arasinda bir sayi tahmin ediniz : "))
#     if rastgele_sayi == tahmin_edilen_sayi:
#         print("tahmininiz dogru TEBRİKLERR...")
#         break
#     elif rastgele_sayi < tahmin_edilen_sayi:
#         print("daha asagida tahmin ediniz...")
#         hak = hak - 1
#     else:
#         print("daha yukarida tahmin ediniz...")
#         hak = hak - 1





#10.soru
# import random
#
# tahta = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# for i in tahta:
#     print(i)
# print("----------------------------------")
# rastgele_konum_x = random.randint(1,5)
# rastgele_konum_y = random.randint(1,5)
#
# tahta[rastgele_konum_x][rastgele_konum_y] = 1
#
# print("Amiral Battı Oyununa Hoş Geldiniz!")
# print("5x5 bir tahtada geminin yerini bulmaya çalışın.")
# hak = 5
# while hak > 0:
#     tahmin_edilen_konum_x = int(input("Satır seçin (1-5):"))
#     tahmin_edilen_konum_y = int(input("Sütun seçin (1-5):"))
#     if tahmin_edilen_konum_x == rastgele_konum_x and tahmin_edilen_konum_y == rastgele_konum_y:
#         print("tebrikler gemiyi vurdunuz!")
#         break
#     else:
#         hak= hak-1
#         print("yanlis tahmin tekrar deneyiniz...")
#         print(f"kalan hakkiniz : {hak}")
# print(f"geminizin konumu : {rastgele_konum_x},{rastgele_konum_y}")