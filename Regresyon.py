# Get-Command pip
# Which Pip'in powershelldeki windowsdaki karşılığı.
# Which linux sistemlerde çalışıyor.
# 2018-23 Yılları Arasında veriye sahibim, bunları import edip, pandas.concat ile birleştiricem.
import pandas as pd
import openpyxl
import stats
import seaborn as sns
import matplotlib.pyplot as plt

# Bilimsel gösterimi kapat, sayıları tam göster
pd.set_option('display.float_format', '{:.2f}'.format)

# Aşağıdaki path'leri ofis-pc ye göre değiştir.
# Ofisteki PC PATH
# path_2018 = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/2018 Apartman Satılık.csv"
# path_2019 = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/2019 Apartman Satılık.csv"
# path_2020 = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/2020 Apartman Satılık.csv"
# path_2021 = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/2021 Apartman Satılık.csv"
# path_2022 = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/2022 Apartman Satılık.csv"
# path_2023 = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/2023 Apartman Satılık.csv"

# Evdeki PC PATH
path_2018 = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/2018 Apartman Satılık.csv"
path_2019 = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/2019 Apartman Satılık.csv"
path_2020 = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/2020 Apartman Satılık.csv"
path_2021 = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/2021 Apartman Satılık.csv"
path_2022 = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/2022 Apartman Satılık.csv"
path_2023 = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/2023 Apartman Satılık.csv"

# base_path = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/OneDrive - Torunlar Enerji Sanayi ve Ticaret Anonim Şirketi/Gayrimenkul Pazar Analizi/Odev_Regresyon/Data"
# years = ["2023", "2022", "2021", "2020", "2019", "2018"]

usecols = ["CityName", "CountyName", "DistrictName", "ComparableArea", "BrutArea", "AdjustedPrice",
"RealtyPrice", "Room", "LivingRoom", "Bahtroom", "FloorNumber", "BuildDate", "FrontageNorth", "FrontageSouth", "FrontageEast", "FrontageWest", 
"AttributeMainRoad", "AttributeWideRoad", "AttributeSportComplex", "AttributePlayGround", "AttributeElevator", "AttributeGenerator", 
"AttributeGateKeeper", "AttributeSecurity", "AttributeParkingAreaOutdoor", "AttributeParkingAreaIndoor", "AttributeSwimmingPoolOutdoor", 
"AttributeSwimmingPoolIndoor", "AttributeHeatIsolation", "AttributeAirCondition", "ViewCity", "ViewNature", "ListMonth", "ListYear"]


data_2018 = pd.read_csv(path_2018, sep = ";", usecols = usecols, encoding = "ISO-8859-9")
data_2019 = pd.read_csv(path_2019, sep = ";", usecols = usecols, encoding = "ISO-8859-9")
data_2020 = pd.read_csv(path_2020, sep = ";", usecols = usecols, encoding = "ISO-8859-9")
data_2021 = pd.read_csv(path_2021, sep = ";", usecols = usecols, encoding = "ISO-8859-9")
data_2022 = pd.read_csv(path_2022, sep = ";", usecols = usecols, encoding = "ISO-8859-9")
data_2023 = pd.read_csv(path_2023, sep = ";", usecols = usecols)

# import ettiklerimizi concat ile birleştirelim.
data = pd.concat([data_2023, data_2022, data_2021, data_2020, data_2019, data_2018])

del data, data_2018, data_2019, data_2020, data_2021, data_2022, data_2023 # Siliyorum, rami gereksiz çok şişiriyor.


# Veriden Ankara - Çankaya - İlgili Mahalleleri Filtreleyelim. Onları Alalım.
# Ana Data'nın kopyasını oluşturuyorum.
df = data.copy()
districts = ["Büyükesat", "Kazım Özalp", "100.yıl", "100. Yıl", "Murat", "Bayraktar",
              "Bağcılar", "Kırkkonaklar", "Birlik", "Umut", "Aşıkpaşa", "Sancak", "Yıldızevler",
              "Çankaya", "Gaziosmanpaşa", "Barbaros", "Muhsin Ertuğrul", "Küçükesat", "Metin Oktay", "Doğuş",
              "Esatoğlu", "Tınaztepe"]
df_Ankara = df[(df["CityName"] == "Ankara") 
               & (df["CountyName"] == "Çankaya") 
               & (df["DistrictName"].isin(districts))]

df_Ankara = df_Ankara.reset_index(drop = True) # drop = True, index kolonun silsin diye.

# Buraya kadar olan kısımı xlsx olarak dışarı alıp hocaya atıyorum. Derste istedi.
# df_Ankara.to_excel("cikti.xlsx")

# Geçmiş tarihli fiyat verisini, Yİ-ÜFE ile bugüne getirelim. En güncel Yİ-ÜFE verisi 2025-Nisan'a ait.
# path_tuik_Ofis = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/yi_ufe.csv"
path_tuik_Ev = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/yi_ufe.csv"

tuik = pd.read_csv(path_tuik_Ev, sep = ";", encoding = "ISO-8859-9")

# Veri Tiplerini Düzenleyelim.
df_Ankara.info()
float_to_int = ["Room", "LivingRoom", "Bahtroom"]
df_Ankara[float_to_int] = df_Ankara[float_to_int].astype(int)
# 66. satırda hata veriyor. FloorCountta nan olan değerler var. Onları fillna ile doldurup ortalamayı basacağım
# df_Ankara["FloorCount"] = df_Ankara["FloorCount"].fillna(df_Ankara["FloorCount"].mean()).astype(int)
df_Ankara["BuildDate"] = df_Ankara["BuildDate"].fillna(df_Ankara["BuildDate"].mean()).astype(int)
# df_Ankara["AdjustedPrice"] = df_Ankara["AdjustedPrice"].astype(int)
# Ondalıklar virgül ile ayrılmış. Noktaya çevirip int yapabiliriz.
df_Ankara["RealtyPrice"] = df_Ankara["RealtyPrice"].astype(int)
df_Ankara.info()

# Kullanmayacağım kolonları dropluyorum.
ise_yaramaz = ["CityName", "CountyName", "AdjustedPrice"]
df_Ankara = df_Ankara.drop(ise_yaramaz, axis = 1)
df_Ankara.info()
# Sayısal değişkenleri ve kategorik değişkenleri ayırıyorum.
# Sayısal değişkenleri alıp, describe ile genel bakış atacağım sonra büyük ihtimalle bathroom room gibi bunlarıda category yapacağım.
Numeric_Variables = ["ComparableArea", "BrutArea", "RealtyPrice", "Room", "LivingRoom", "Bahtroom", "FloorNumber", "BuildDate"]
df_Ankara[Numeric_Variables].describe()
# Bu çıktıya göre Room + Living Room yapıp Total Oda Sayısı değişkeni oluşturacağım.
# Bathroom ve floornumberı category yapacağım. Çalışmanın sonunda bir farklılık yaratacak mı diye numeric yapıp bakacağım.
df_Ankara["TotalRoom"] = df_Ankara["Room"] + df_Ankara["LivingRoom"]

Categorical_Variables = ["Bahtroom","FrontageNorth", "FrontageSouth", "FrontageEast", "FrontageWest", 
"AttributeMainRoad", "AttributeWideRoad", "AttributeSportComplex", "AttributePlayGround", "AttributeElevator", "AttributeGenerator", 
"AttributeGateKeeper", "AttributeSecurity", "AttributeParkingAreaOutdoor", "AttributeParkingAreaIndoor", "AttributeSwimmingPoolOutdoor", 
"AttributeSwimmingPoolIndoor", "AttributeHeatIsolation", "AttributeAirCondition", "ViewCity", "ViewNature"]
df_Ankara[Categorical_Variables] = df_Ankara[Categorical_Variables].astype("category")

# BuildDate değişkeni, binanın yapım yılı
# 1 - Güncel yıl - Yapım Yılı yapıp yaşını bulacağım.
# 2 - Bu yaş değişkenilerini gruplayacağım 0-3, 4-7, 8-11, 12-15, 16-19, 20-23, 24-27, 28-31, 32-35, 36-39, 40+ şeklinde gruplandıracağım. 
# 3 - Bu yaş değişkenini de category yapacağım.
# 4 - Çalışmanın sonunda bir farklılık yaratacak mı diye numeric yapıp bakacağım.
# Sahip olduğum data 2018 - 23 yılları arasında olduğu için 2025 değilde 2023 den çıkardım.
df_Ankara["BinaYasi"] = 2023 - df_Ankara["BuildDate"]
df_Ankara["BinaYasi_Grup"] = 0
df_Ankara.info()

def bina_yas_grubu(BinaYasi):
    if BinaYasi <= 3:
        return 0
    elif BinaYasi <= 7:
        return 1
    elif BinaYasi <= 11:
        return 2
    elif BinaYasi <= 15:
        return 3
    elif BinaYasi <= 19:
        return 4
    elif BinaYasi <= 23:
        return 5
    elif BinaYasi <= 27:
        return 6
    else:
        return 7

df_Ankara["BinaYasi_Grup"] = df_Ankara["BinaYasi"].apply(bina_yas_grubu)
df_Ankara["BinaYasi_Grup"] = df_Ankara["BinaYasi_Grup"].astype("category")

# Tüik Yİ-ÜFE verisini alıp, 2018-2023 yılları arasındaki fiyatları güncelleyeceğim.
# df_Ankara["Old_Endex"] = 0
# df_Ankara.drop("Old_Endex", axis = 1, inplace = True)

# İlk olarak Gayrimenkul İlanlarının Ay ve Tarihlerine Göre Tüik Enflasyon Endeksini Yazdıracağım.
# Wide -> Long: Aylar tek sütun, enflasyon değerleri tek sütun olacak
tuik_long = tuik.melt(id_vars=["Yıl"], 
                      var_name="Ay", 
                      value_name="Endeks")

# Ay adlarını Türkçe'den sayıya çevirme
ay_map = {
    "Ocak": 1, "Şubat": 2, "Mart": 3, "Nisan": 4,
    "Mayıs": 5, "Haziran": 6, "Temmuz": 7, "Ağustos": 8,
    "Eylül": 9, "Ekim": 10, "Kasım": 11, "Aralık": 12
}
tuik_long["Ay"] = tuik_long["Ay"].map(ay_map)

df_Ankara = df_Ankara.merge(
    tuik_long.rename(columns={"Endeks": "Old_Endex"}),
    how = "left",
    left_on = ["ListMonth", "ListYear"],
    right_on = ["Ay", "Yıl"]
)

df_Ankara.drop(["Yıl", "Ay"], axis = 1, inplace = True)

# Şimdi güncel 2025-Nisan Yİ-ÜFE verisini New_Endex olarak tabloya yazdıracağım. Fiyatı Güncellemiş, bugüne getirmiş olacağım.
New_Endex = tuik_long.sort_values(["Yıl", "Ay"], ascending = True).iloc[-9]["Endeks"]
df_Ankara["New_Endex"] = New_Endex

# Old_Endex ile New_Endex object olarak gözüküyor. Bunlar floata. Çevirelim
df_Ankara["Old_Endex"] = df_Ankara["Old_Endex"].str.replace(",",".").astype(float)
df_Ankara["New_Endex"] = df_Ankara["New_Endex"].str.replace(",", ".").astype(float)

df_Ankara["Guncel_Fiyat"] = df_Ankara["RealtyPrice"] * ((df_Ankara["New_Endex"] / df_Ankara["Old_Endex"]))
df_Ankara["Guncel_Fiyat"] = round(df_Ankara["Guncel_Fiyat"], 0).astype(int)
# df_Ankara.to_excel("cikti.xlsx")

# Temel İstatistiki Sonuçlara Bakalım
# Numeric Data
df_Ankara.describe().T

# Çarpıklık ve basıklık değerlerine bakalım
# İlk olarak histogram çiziyorum.
sns.displot(data = df_Ankara["Guncel_Fiyat"], kde=True)
# Histogramu incelediğimizde, verinin sağa çarpık olduğunu görüyoruz. Ancak çok net değil. Boxplot yapıyorum.
sns.boxplot(data = df_Ankara, x = "Guncel_Fiyat")
plt.title("Guncel_Fiyat - Boxplot (Aykırı Değerlerle)")
plt.show()

sns.boxplot(data = df_Ankara, y = "Guncel_Fiyat") 
plt.title("Guncel_Fiyat - Boxplot (Aykırı Değerlerle)")
plt.show()

skewness = df_Ankara["Guncel_Fiyat"].skew()
skewness # 98.80428204987487

kurtosis = df_Ankara["Guncel_Fiyat"].kurtosis()
kurtosis # 10465.75302276866
# Çarpıklık ve basıklık değerleri çok yüksek. Normal dağılıma uymuyor. 
# Çarpıklık ve basıklık 0'a yakın olmalı ve genelde, -2 2 arasında olması beklenmektedir.

# Aykırı değer analizi yapalım.
# IQR yöntemini kullanacağım.
Q1 = df_Ankara["Guncel_Fiyat"].quantile(0.25)
Q3 = df_Ankara["Guncel_Fiyat"].quantile(0.75)
IQR = Q3 - Q1

# Aşağıdaki sınırlar dışında olanlar aykırı gözlemdir.
Minimum = Q1 - 1.5 * IQR # -1643695.0 
Maximum = Q3 + 1.5 * IQR # 9.809.265.0

df_Ankara_aykiri = df_Ankara[(df_Ankara["Guncel_Fiyat"] < Minimum) | (df_Ankara["Guncel_Fiyat"] > Maximum)]
df_Ankara_clean = df_Ankara[(df_Ankara["Guncel_Fiyat"] >= Minimum) & (df_Ankara["Guncel_Fiyat"] <= Maximum)]

# df_Ankara_clean ile aykırı değerleri temizledik. Şimdi bidaha Skewness - Kurtosis ve histogram yapalım.
sns.displot(data = df_Ankara_clean["Guncel_Fiyat"], kde=True)

df_Ankara_clean["Guncel_Fiyat"].skew()
df_Ankara_clean["Guncel_Fiyat"].kurtosis()
# Sıfıra oldukça yakın hale geldi.
# Yinede normallik testi yapacağım.
