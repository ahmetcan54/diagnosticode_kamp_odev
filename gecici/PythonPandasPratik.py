import numpy as np
import pandas as pd

from numpy.random  import randn

label_list =["mustafa","kemal","murat","ahmet","kadir"]

data_list = [10,20,30,40,50]

seri = pd.Series(data = data_list, index = label_list) #pandas kütüphanesini kullanarak seri oluşturuldu

seri1 = pd.Series(data = data_list) #yukarıdaki ile aynı bu sefer indix değeri verimediği için default değeri atandı

array = np.array([10,20,30,40,50])

seri2 = pd.Series(array)

seri3 = pd.Series(data = array,index =["a","b","c","d","e"])

dataDict = {"kadir ": 30,"kemal":80,"kamuran":60}

seri4 = pd.Series(data = dataDict)

ser2017 = pd.Series([5,10,14,20],["buğday","mısır","kiraz","erik"])

ser2018 = pd.Series([2,20,15,10],["buğday","mısır","çilek","erik"])

serToplam = ser2017+ser2018

serToplam["mısır"] #mısır değerini bize döndürür

df =pd.DataFrame(data = randn(3,3),index = ["A","B","C"],columns=["column1","column2","column3"]) #3e 3 lük bir dataframe oluşturuldu ve bu matrix tir

column1 = df["column1"]    #COLUMN1 cağırıyoruz

column2 = df["column2"]  # column2 cağırıyoruz

column3 = df["column3"]  # column3 cağırıyoruz

A = df.loc["A"]   # A indixine ait değerleri çagırıyoryz

B = df.loc["B"]    # B indixine ait değerleri çagırıyoryz
 
C = df.loc["C"]     # C  indixine ait değerleri çagırıyoryz

column13 = df[["column1","column3"]] # burada iki columnu bir arada çağırıyoruz

df["column4"] = pd.Series(randn(3),["A","B","C"]) #burada df yeni bir column ekleme yapıyoruz aynı sayıda veri girilmesi gerekiyor

df["column5"] = df["column1"]+df["column2"]+df["column3"] # 1. ,2. ve 3. columnların toplamı ile 5. column oluşturularak ekleniyor

df.drop("column5",axis=1,inplace = True)  # burada ilk önce silinecek yeri giriyoruz sonra ise axis değerini giriyoruz 1 girersek columns ,0 girersek indexlerde silme işlemi yapar  .
# inplace değeri ise true ise df da etkilicek şekilde değişiklik yapar default değeri false dır bu yüzden ellemzsek ana dfmizde değişiklik olmaz

df.iloc[0] # df.loc["A"] aynı işlemdir

df.loc["A","column2"] # A indixindeki column2 columnundaki değeri getirir

df1 = pd.DataFrame(randn(4,3),["A","B","C","D"],["column1","column2","column3"])

df1 > 1  # değerlerin içinden 1 den büyük olanlar true küçük olanlar false

booleanDf = df1 >0

df1["column1"] > 0

df1[df1["column1"] > 0] 

df1[df1["column2"]>0]

df1[(df1["column1"] > 0)  & (df1["column2"] > 0)]

df1[(df1["column1"] > 0 ) | (df1["column2"] > 0)]











