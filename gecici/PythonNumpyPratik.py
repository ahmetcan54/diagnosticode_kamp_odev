import numpy as np

data_list = [1,2,3]

data_list

arr = np.array(data_list)

data_list2 = [[10,20,30],[40,50,60],[70,80,90]]

arr2 = np.array(data_list2)


arr2[0]

arr2[1,2]    

arr2[1][2]

arr3 = np.arange(10,20) #10 ile 20 arasındaki sayılaRLA bir matrix oluşturur 2 dahil değil

arr4 = np.arange(1,100,2) #1 ile 100 arasında 2 şer 2 şer atlayarak bir array oluşturur

arr5 = np.zeros(10) # 1o adet sıfır arrray oluşturur

arr6 = np.ones(15) # 15  adet 1 den oluşan array oluşturur

arr7 = np.zeros((2,2)) # 2 ye 2lik bir sıfır matrix oluşturur

arr8 = np.ones((3,3)) # 3e 3 lük bir bir matrix oluşturur

arr9 = np.linspace(1,500,10) #1 ile 500 arasını 10 adet parçaya bölerek bir array oluşturur

arr10 =np.linspace(0,1,5) #0 ile 1 arasını 5 adet parçaay bölerek bir array oluşturur

arr11 = np.eye(5) #birim matrix

arr12 = np.random.randint(0,50,5)  # 0 ile 50 arasından rastgele sayılar üreterek 5 lik bir array üretir

arr13 = np.random.rand(5) # 0 ile 1 arasında girdiğimiz değer kadar sayı üreterek array oluşturur

arr14 = np.arange(15)

arr14 = arr14.reshape(3,5) # verilen arrayi istediğniz boyutta matrixe dönüştürür

arr15 = np.random.randint(1,100,5)

arr15max = arr15.max() #arrayin içindeki en büyük değeri döner

arr15min = arr15.min() #arrayin içindeki en küçük değeri döner

arr15sum =arr15.sum() # arrayin içindeki değerlerin toplamını döner 

arr15mean = arr15.mean() # arrayin içindeki değerlerin ortalamasını döner

arr15argmax = arr15.argmax() # arrayin içindeki en büyük değerin hangi indexte olduğunu döner

arr15argmin =arr15.argmin() # arrayin içindeki en küçük değerin hangi indexte olduğunu döner

detArray = np.random.randint(1,100,(5,5)) # 5e 5 lik bir random matrix oluşturur 1 ile 100 arsında

detArrayHesabi = np.linalg.det(detArray) # içine alan matrixin determinant hesabını yapar

detArray2 = np.array([[1,5],[10,5]])

detArray2Hesabı = np.linalg.det(detArray2) # determinant hesabı

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

arr16 = np.arange(1,10)

arr16 = arr16.reshape(3,3)

arr16_1 = arr16[:,:2] # satırların hepsi gelicek fakat sutünların sadece ilk ikisi gelicek

arr17 = np.array([10,20,30,40,50,60])
arr18 = np.array([14,15,12,36,52,85])

arrToplam =arr17+arr18

arrFark = arr17 -arr18

arr19 = np.array([1,4,9,16,25,36,49,64,81,100])
arrKok = np.sqrt(arr19)











