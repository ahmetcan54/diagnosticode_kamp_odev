# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 13:29:43 2025

@author: Ahmet Can
"""

import cv2

###### ÖDEV 1

### 1. soru

# img = cv2.imread("kedi_resmi.webp") # resmimizi okuduk
# img_2 = cv2.imread("kedi_resmi.webp",0) # resmimizin gri tonlu hali

# cv2.imshow("kedi resim", img) # resmimizi pencere içinde gösterdik
# cv2.imshow("kedi resmi gri", img_2)

# cv2.imwrite("kedi_resmi_gri.jpg", img_2) # resmimizn adını ve hangi resim olduğunu belirttik ve kaydettik
# cv2.waitKey(0) # resmin biz bir komut vermeden gitmemesi için 0 değerini verdik

# cv2.destroyAllWindows() # tüm pencereleri kapattık


### 2.soru

# img = cv2.imread("kedi_resmi.webp") 

# # img.shape = (400,900,3)

# new_img = cv2.resize(img, (200,450)) # yeni boyutumuz (200,450) yaptık

# new_rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # resmimizi saaat yönünde 90 derece döndürdük

# cv2.putText(img, "selamlar", (20,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (242,25,85)) # BURADA YAZIMIZIN HANGİ RESME KOYULACAĞI,İÇERİĞİNİN NE OLACAĞI,HANGİ KORDİNATLARDA OLACAĞI,YAZI TİPİ VE HANGİ RENKTE OLACAĞINI SEÇİYORUZ


# cv2.imshow("new_rotated_90", new_rotated_90)
# cv2.imshow("yeni kedi resmi", new_img) # burada ise gsöterdik
# cv2.imshow("kedi resmi", img)


### 3.soru

# img = cv2.imread("kedi_resmi.webp") 
# new_img = cv2.GaussianBlur(img, (5, 5), 0) # burada resmimizi  blurluyoryuz

# cv2.imshow("Gaussian Blurred kedi resmi", new_img)
# cv2.imshow("kedi resmi",img)


# # Canny kenar tespiti (alt eşik: 100, üst eşik: 200)
# new_img2 = cv2.Canny(img, 100, 200)

# cv2.imshow("kenar tespit", new_img2)


###### ÖDEV2

### BU BİRAZ YARDIMLI OLDU :))

# # Haar Cascade sınıflandırıcısını yükleme
# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# # Kamerayı başlatma
# cap = cv2.VideoCapture(0)

# while True:
#     # Kameradan görüntü alma
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Yüzleri tespit etme
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     # Tespit edilen yüzlerin etrafına dikdörtgen çizme
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

#     # Sonucu gösterme
#     cv2.imshow("Face Detection", frame)

#     # Çıkmak için 'q' tuşuna basın
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Kaynakları serbest bırakma
# cap.release()
# cv2.destroyAllWindows()













