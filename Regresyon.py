# Get-Command pip
# Which Pip'in powershelldeki windowsdaki karşılığı.
# Which linux sistemlerde çalışıyor.
# 2018-23 Yılları Arasında veriye sahibim, bunları import edip, pandas.concat ile birleştiricem.
import pandas as pd
import openpyxl

# Aşağıdaki path'leri kendi bilgisayarınıza göre değiştirin.

path_2023 = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/2023 Apartman Satılık.csv"
path_2022 = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/2022 Apartman Satılık.csv"
path_2021 = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/2021 Apartman Satılık.csv"
path_2020 = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/2020 Apartman Satılık.csv"
path_2019 = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/2019 Apartman Satılık.csv"
path_2018 = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/2018 Apartman Satılık.csv"
# base_path = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/OneDrive - Torunlar Enerji Sanayi ve Ticaret Anonim Şirketi/Gayrimenkul Pazar Analizi/Odev_Regresyon/Data"
# years = ["2023", "2022", "2021", "2020", "2019", "2018"]

usecols = ["CityName", "CountyName", "DistrictName", "ComparableArea", "BrutArea", "AdjustedPrice", 
"RealtyPrice", "Room", "LivingRoom", "Bahtroom", "FloorCount", "FloorNumber", 
"BuildDate", "FrontageNorth", "FrontageSouth", "FrontageEast", "FrontageWest", 
"AttributeMainRoad", "AttributeWideRoad", "AttributeSportComplex",
"AttributePlayGround", "AttributeElevator", "AttributeGenerator", 
"AttributeGateKeeper", "AttributeSecurity", "AttributeParkingAreaOutdoor",
"AttributeParkingAreaIndoor", "AttributeSwimmingPoolOutdoor", 
"AttributeSwimmingPoolIndoor", "AttributeHeatIsolation", "AttributeAirCondition",
"ViewCity", "ViewNature", "ListMonth", "ListYear"]


data_2023 = pd.read_csv(path_2023, sep = ";", usecols = usecols)
data_2022 = pd.read_csv(path_2022, sep = ";", usecols = usecols, encoding = "ISO-8859-9")
data_2021 = pd.read_csv(path_2021, sep = ";", usecols = usecols, encoding = "ISO-8859-9")
data_2020 = pd.read_csv(path_2020, sep = ";", usecols = usecols, encoding = "ISO-8859-9")
data_2019 = pd.read_csv(path_2019, sep = ";", usecols = usecols, encoding = "ISO-8859-9")
data_2018 = pd.read_csv(path_2018, sep = ";", usecols = usecols, encoding = "ISO-8859-9")

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
path_tuik = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/yi_ufe.csv"
tuik = pd.read_csv(path_tuik, sep = ";", encoding = "ISO-8859-9")

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
