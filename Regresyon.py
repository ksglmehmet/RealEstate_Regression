# Get-Command pip
# Which Pip'in powershelldeki windowsdaki karşılığı.
# Which linux sistemlerde çalışıyor.
# 2018-23 Yılları Arasında veriye sahibim, bunları import edip, pandas.concat ile birleştiricem.
import pandas as pd
import openpyxl

# Bilimsel gösterimi kapat, sayıları tam göster
pd.set_option('display.float_format', '{:.2f}'.format)

# Aşağıdaki path'leri ofis-pc ye göre değiştir.
# Ofisteki PC PATH
path_2018 = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/2018 Apartman Satılık.csv"
path_2019 = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/2019 Apartman Satılık.csv"
path_2020 = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/2020 Apartman Satılık.csv"
path_2021 = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/2021 Apartman Satılık.csv"
path_2022 = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/2022 Apartman Satılık.csv"
path_2023 = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/2023 Apartman Satılık.csv"

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
path_tuik_Ofis = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/yi_ufe.csv"
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
df_Ankara.info()

# BuildDate değişkeni, binanın yapım yılı
# 1 - Güncel yıl - Yapım Yılı yapıp yaşını bulacağım.
# 2 - Bu yaş değişkenilerini gruplayacağım 0-3, 4-7, 8-11, 12-15, 16-19, 20-23, 24-27, 28-31, 32-35, 36-39, 40+ şeklinde gruplandıracağım. 
# 3 - Bu yaş değişkenini de category yapacağım.
# 4 - Çalışmanın sonunda bir farklılık yaratacak mı diye numeric yapıp bakacağım.
# Sahip olduğum data 2018 - 23 yılları arasında olduğu için 2025 değilde 2023 den çıkardım.
df_Ankara["BinaYasi"] = 2023 - df_Ankara["BuildDate"]
if df_Ankara["BinaYasi"] <= 3:
    df_Ankara["BinaYasi_Grup"] = 0


df_Ankara["Old_Endex"] = 0
i = 4
for i in range(len(df_Ankara)):
    if df_Ankara["ListMonth"][i] == 1 & df_Ankara["ListYear"][i] == :
        df_Ankara["Old_Endex"][i] = tuik.iloc[17,1]
    elif df_Ankara["ListMonth"][i] == 2:
        df_Ankara["Old_Endex"][i] = tuik.iloc[17,2]
    elif df_Ankara["ListMonth"][i] == 3:
        df_Ankara["Old_Endex"][i] = tuik.iloc[17,3]
    elif df_Ankara["ListMonth"][i] == 4:
        df_Ankara["Old_Endex"][i] = tuik.iloc[17,4]
