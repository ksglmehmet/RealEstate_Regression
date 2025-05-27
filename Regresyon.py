######################################################################################################
# Creator  : Mehmet Akif KÖSOĞLU
# StartDay : 20.05.2025
######################################################################################################
import pandas as pd
import openpyxl
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Veri Bilimi ve İstatistiksel Analiz için gerekli kütüphaneleri import ettik.

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

del data, data_2018, data_2019, data_2020, data_2021, data_2022, data_2023 # Siliyorum, rami gereksiz çok şişiriyor.

# df_Ankara = df_Ankara.reset_index(drop = True) # drop = True, index kolonun silsin diye.
df_Ankara.index = range(1, len(df_Ankara) + 1)

# Geçmiş tarihli fiyat verisini, Yİ-ÜFE ile bugüne getirelim. En güncel Yİ-ÜFE verisi 2025-Nisan'a ait.
# path_tuik_Ofis = "C:/Users/mehmetakifkosoglu.TORUNLARENERJI/Desktop/Personel_Workspace/RealEstate_Regression/Data/yi_ufe.csv"
path_tuik_Ev = "C:/Users/Makkos/Desktop/Personel_Workspace/RealEstate_Regression/Data/yi_ufe.csv"

tuik = pd.read_csv(path_tuik_Ev, sep = ";", encoding = "ISO-8859-9")

# Veri Tiplerini Düzenleyelim.
df_Ankara.info()
# Ondalıklar virgül ile ayrılmış. Noktaya çevirip int yapabiliriz.
to_int = ["Room", "LivingRoom", "Bahtroom", "RealtyPrice"]
df_Ankara[to_int] = df_Ankara[to_int].astype(int)
# 66. satırda hata veriyor. FloorCountta nan olan değerler var. Onları fillna ile doldurup ortalamayı basacağım
# df_Ankara["FloorCount"] = df_Ankara["FloorCount"].fillna(df_Ankara["FloorCount"].mean()).astype(int)
df_Ankara["BuildDate"] = df_Ankara["BuildDate"].fillna(df_Ankara["BuildDate"].mean()).astype(int)
df_Ankara.info()

# Kullanmayacağım kolonları dropluyorum.
ise_yaramaz = ["CityName", "CountyName", "AdjustedPrice"]
df_Ankara = df_Ankara.drop(ise_yaramaz, axis = 1)
df_Ankara.info()
# Sayısal değişkenleri ve kategorik değişkenleri ayırıyorum.
# Sayısal değişkenleri alıp, describe ile genel bakış atacağım sonra büyük ihtimalle bathroom room gibi bunlarıda category yapacağım.
Numeric_Variables = ["ComparableArea", "BrutArea", "RealtyPrice", "Room", "LivingRoom", "Bahtroom", "FloorNumber", "BuildDate"]
df_Ankara[Numeric_Variables].describe().T
# Bu çıktıya göre Room + Living Room yapıp Total Oda Sayısı değişkeni oluşturacağım.
# Bathroom ve floornumberı category yapacağım. Çalışmanın sonunda bir farklılık yaratacak mı diye numeric yapıp bakacağım.
df_Ankara["TotalRoom"] = df_Ankara["Room"] + df_Ankara["LivingRoom"]
df_Ankara.info()

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
df_Ankara["BinaYasi_Grup"] = 0
df_Ankara.info()
df_Ankara

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
df_Ankara
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

# df_Ankara ile tuik_long'da yer alan ListYear = Yıl değişkenleri aynı data tipinde değil.
# int - object
# Endeks içinde virgül var ise nokta ile değiştirip float yapacağım.
tuik_long["Endeks"] = tuik_long["Endeks"].astype(str).str.replace(",", ".").astype(float)

df_Ankara = df_Ankara.merge(
    tuik_long.rename(columns={"Endeks": "Old_Endex"}),
    how = "left",
    left_on = ["ListMonth", "ListYear"],
    right_on = ["Ay", "Yıl"]
)

df_Ankara.info()
df_Ankara.drop(["Yıl", "Ay"], axis = 1, inplace = True)
df_Ankara.info()
# Şimdi güncel 2025-Nisan Yİ-ÜFE verisini New_Endex olarak tabloya yazdıracağım. Fiyatı Güncellemiş, bugüne getirmiş olacağım.
New_Endex = tuik_long.sort_values(["Yıl", "Ay"], ascending = True).iloc[-9]["Endeks"]
df_Ankara["New_Endex"] = New_Endex

# Old_Endex ile New_Endex object olarak gözüküyor. Bunlar floata. Çevirelim
# df_Ankara["Old_Endex"] = df_Ankara["Old_Endex"].str.replace(",",".").astype(float)
# df_Ankara["New_Endex"] = df_Ankara["New_Endex"].str.replace(",", ".").astype(float)

df_Ankara["Guncel_Fiyat"] = df_Ankara["RealtyPrice"] * ((df_Ankara["New_Endex"] / df_Ankara["Old_Endex"]))
df_Ankara["Guncel_Fiyat"] = round(df_Ankara["Guncel_Fiyat"], 0).astype(int)
df_Ankara.info()

# Temel İstatistiki Sonuçlara Bakalım
# Numeric Data
df_Ankara.describe().T

# Bağımlı değişkenimiz Guncel_Fiyat ve Biz bu bağımlı değişkenimizi Yİ-ÜFE ye göre bugüne getirdik.
# Tekrar, Kullanacağım değişkenleri alalım.

ise_yaramaz = ["DistrictName", "ComparableArea", "Room", "LivingRoom", "BuildDate", "ListMonth", "ListYear",
               "Old_Endex", "New_Endex", "RealtyPrice"]

data = df_Ankara.drop(ise_yaramaz, axis = 1)
######################################################################################################
# Veri Hazırlama Bitti, İstatistiksel Analiz Kısmına Geçelim. Aykırı Değer Analizi Vs Yapalım.
######################################################################################################

# Çarpıklık ve basıklık değerlerine bakalım
# İlk olarak histogram çiziyorum.
sns.displot(data = data["Guncel_Fiyat"], kde=True) # type: ignore

data["Guncel_Fiyat"].skew()
data["Guncel_Fiyat"].kurtosis()

# Çarpıklık ve basıklık değerleri çok yüksek. Normal dağılıma uymuyor. 
# Çarpıklık ve basıklık 0'a yakın olmalı ve genelde, -2 2 arasında olması beklenmektedir.

######################################################################################################
# Numeric Datalar İçin Aykırı Değer Analizi
######################################################################################################
# Aykırı değer analizi yapalım.
# IQR yöntemini kullanacağım.
# Amacım her int ve float değişken için IQR değerini hesaplayıp, alt ve üst sınırları belirlemek.
def iqr_outlier_analysis(data, columns):
    """
    Belirtilen sütunlar için IQR yöntemi ile aykırı değer analizi yapar.

    Parametreler:
    data (pd.DataFrame): Aykırı değer analizi yapılacak DataFrame.
    columns (list): Aykırı değer analizi yapılacak sütunların listesi.

    Dönüş Değeri:
    pd.DataFrame: Aykırı değerlerin temizlendiği yeni DataFrame.
    """
    df_cleaned = data.copy()
    
    # Tek sütun string olarak verildiyse listeye çevir
    
    if isinstance(columns, str):
        columns = [columns]
        
    # Sütunların DataFrame'de olup olmadığını kontrol et
    for i in columns:
        if i not in df_cleaned.columns:
            print(f"Uyarı: '{i}' sütunu DataFrame'de bulunamadı.")
            continue
        
        Q1 = df_cleaned[i].quantile(0.25)
        Q3 = df_cleaned[i].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = round(Q1 - 1.5 * IQR, 0)
        upper_bound = round(Q3 + 1.5 * IQR, 0)
        # Alt sınırı 1.000.000 TL olarak sabitliyorum. Eksili değerler olmasın.
        # Yalnızca Guncel_Fiyat için alt sınırı 1.000.000 TL olarak sabitliyorum.
        # Diğer sütunlar için alt sınır sabitlenmeyecek.
        if i == "Guncel_Fiyat":
            lower_bound_fixed = max(1750000, lower_bound) 
            num_outliers = df_cleaned[(df_cleaned[i] < lower_bound_fixed) | (df_cleaned[i] > upper_bound)].shape[0]
            df_cleaned = df_cleaned[(df_cleaned[i] >= lower_bound_fixed) & (df_cleaned[i] <= upper_bound)]
            print(f"\n{i} sütunu için IQR: {IQR:.2f}, Alt sınır: {lower_bound_fixed:.2f}, Üst sınır: {upper_bound:.2f}")
            print(f"{i} sütununda {num_outliers} aykırı değer temizlendi.")
        elif i == "BrutArea":
            # BrutArea için alt sınırı 35 m2 olarak sabitliyorum.
            lower_bound_fixed = max(35, lower_bound)
            num_outliers = df_cleaned[(df_cleaned[i] < lower_bound_fixed) | (df_cleaned[i] > upper_bound)].shape[0]
            df_cleaned = df_cleaned[(df_cleaned[i] >= lower_bound_fixed) & (df_cleaned[i] <= upper_bound)]
            print(f"\n{i} sütunu için IQR: {IQR:.2f}, Alt sınır: {lower_bound_fixed:.2f}, Üst sınır: {upper_bound:.2f}")
            print(f"{i} sütununda {num_outliers} aykırı değer temizlendi.")
        elif i == "TotalRoom":
            # TotalRoom için alt sınırı 1 olarak sabitliyorum.
            lower_bound_fixed = 1
            num_outliers = df_cleaned[(df_cleaned[i] < lower_bound_fixed) | (df_cleaned[i] > upper_bound)].shape[0]
            df_cleaned = df_cleaned[(df_cleaned[i] >= lower_bound_fixed) & (df_cleaned[i] <= upper_bound)]
            print(f"\n{i} sütunu için IQR: {IQR:.2f}, Alt sınır: {lower_bound_fixed:.2f}, Üst sınır: {upper_bound:.2f}")
            print(f"{i} sütununda {num_outliers} aykırı değer temizlendi.")
        elif i == "BinaYasi":
            # BinaYasi için alt sınırı 0 olarak sabitliyorum.
            lower_bound_fixed = max(0, lower_bound)
            upper_bound_fixed = min(50, upper_bound)  # Bina yaşı 40'tan fazla olamaz.
            num_outliers = df_cleaned[(df_cleaned[i] < lower_bound_fixed) | (df_cleaned[i] > upper_bound_fixed)].shape[0]
            df_cleaned = df_cleaned[(df_cleaned[i] >= lower_bound_fixed) & (df_cleaned[i] <= upper_bound_fixed)]
            print(f"\n{i} sütunu için IQR: {IQR:.2f}, Alt sınır: {lower_bound_fixed:.2f}, Üst sınır: {upper_bound_fixed:.2f}")
            print(f"{i} sütununda {num_outliers} aykırı değer temizlendi.")
        else:
            # Aykırı değerleri temizle
            num_outliers = df_cleaned[(df_cleaned[i] < lower_bound) | (df_cleaned[i] > upper_bound)].shape[0]
            df_cleaned = df_cleaned[(df_cleaned[i] >= lower_bound) & (df_cleaned[i] <= upper_bound)]
            print(f"\n{i} sütunu için IQR: {IQR:.2f}, Alt sınır: {lower_bound:.2f}, Üst sınır: {upper_bound:.2f}")
            print(f"{i} sütununda {num_outliers} aykırı değer temizlendi.")
    
    return df_cleaned

df_cleaned = iqr_outlier_analysis(data, data.select_dtypes(include = "int64").columns)

sns.displot(data = df_cleaned["Guncel_Fiyat"], kde=True) # type: ignore

df_cleaned["Guncel_Fiyat"].skew()
df_cleaned["Guncel_Fiyat"].kurtosis()
############################################ Fonksiyon yaz, Shapiro testi ve kolmogorov yapsın
# jarque_bera testi yap, 3 testi yapsın, if 0.05 den büyükse normal dağılıma sahiptir desin.
# Shapiro Testi
stats.shapiro(df_cleaned["Guncel_Fiyat"])
f"T-Statistic : {stats.shapiro(df_cleaned["Guncel_Fiyat"])[0]:.5f}"
f"P-Value : {stats.shapiro(df_cleaned["Guncel_Fiyat"])[1]:.5f}"

# Kolmogorov-Smirnov Test
stats.kstest(df_cleaned["Guncel_Fiyat"], 'norm')
f"T-Statistic : {stats.kstest(df_cleaned["Guncel_Fiyat"], 'norm')[0]:.4f}"
f"P-Value : {stats.kstest(df_cleaned["Guncel_Fiyat"], 'norm')[1]:.4f}"

######################################################################################################
# Categorical Datalar İçin Aykırı Değer Analizi
######################################################################################################
for i in df_cleaned.select_dtypes(include="category").columns:
    print(f"\n{i} değişkeninin frekans dağılımı: \n")
    print(df_cleaned[i].value_counts())
    print("-" * 50)

for i in df_cleaned.select_dtypes(include="category").columns:
    print(f"\n{i} değişkeninin frekans dağılımı (%):")
    print(df_cleaned[i].value_counts(normalize=True).mul(100).round(2))
    print("-" * 50)

def clean_rare_categories(df_cleaned, columns, threshold=0.05):
    """
    Belirtilen sütundaki frekansı belirli bir eşiğin altında olan kategorileri temizler.

    Parametreler:
    df (pd.DataFrame): Temizlenecek DataFrame.
    column (str): Frekans analizi yapılacak kategorik sütunun adı.
    threshold (float): Bir kategorinin aykırı kabul edilmesi için minimum frekans (örneğin, 0.05 = %5).

    Dönüş Değeri:
    pd.DataFrame: Temizlenmiş yeni DataFrame.
    """
    # df_cleaned = data.copy()

   # Tek sütun string olarak verildiyse listeye çevir
    if isinstance(columns, str):
        columns = [columns]
    
    for i in columns:
        # Sütunun DataFrame'de olup olmadığını kontrol et
        if i not in df_cleaned.columns:
            print(f"Uyarı: '{i}' sütunu DataFrame'de bulunamadı.")
            continue

        # Frekans hesapla ve nadir kategorileri bul
        value_counts = df_cleaned[i].value_counts(normalize=True)
        rare_categories = value_counts[value_counts < threshold].index.tolist()

        # Nadir kategorileri temizle
        if rare_categories:
            num_removed_rows = df_cleaned[df_cleaned[i].isin(rare_categories)].shape[0]
            df_cleaned = df_cleaned[~df_cleaned[i].isin(rare_categories)]
            print(f"'{i}' sütununda frekansı %{threshold*100:.2f}'den az olan {len(rare_categories)} kategori temizlendi.")
            print(f"Silinen satır sayısı: {num_removed_rows}")
            print(f"Silinen kategoriler: {rare_categories}")
        else:
            print(f"\n'{i}' sütununda frekansı %{threshold*100:.2f}'den az kategori bulunamadı.")
            print("-" * 50)
    return df_cleaned


# Sıfıra oldukça yakın hale geldi.
# Yinede normallik testi yapacağım.
# Hipotez Kuralım.
# H0 : Bağımlı değişken (Guncel_Fiyat) normal dağılıma sahiptir. (p-value > 0.05)
# H1 : Bağımlı değişken (Guncel_Fiyat) normal dağılıma sahip değildir. (p-value < 0.05)

# Shapiro Testi
stats.shapiro(data_clean_y["Guncel_Fiyat"])
f"T-Statistic : {stats.shapiro(data_clean_y["Guncel_Fiyat"])[0]:.4f}" # Daha okunabilir.
f"P-Value : {stats.shapiro(data_clean_y["Guncel_Fiyat"])[1]:.4f}"

# Kolmogorov-Smirnov Test
stats.kstest(data_clean_y["Guncel_Fiyat"], 'norm')
f"T-Statistic : {stats.kstest(data_clean_y["Guncel_Fiyat"], 'norm')[0]:.4f}"
f"P-Value : {stats.kstest(data_clean_y["Guncel_Fiyat"], 'norm')[1]:.4f}"

# Shapiro ve Kolmogorov-Smirnov testleri p-value değerleri 0.05'ten küçük olduğu için H0 hipotezini reddediyoruz.
# Yani bağımlı değişkenimiz normal dağılıma sahip değildir.
# Aykırı değerleri silmiştim. Şimdi de logaritmik dönüşüm yapacağım.
data_clean_y["Log_Guncel_Fiyat"] = np.log(data_clean_y["Guncel_Fiyat"])

sns.displot(data = data_clean_y["Log_Guncel_Fiyat"], kde = True)
data_clean_y["Log_Guncel_Fiyat"].skew() # 0.09029889035786971
data_clean_y["Log_Guncel_Fiyat"].kurtosis() # -0.7474005896933811

f"T-Statistic : {stats.shapiro(data_clean_y["Log_Guncel_Fiyat"])[0]:.5f}" # Daha okunabilir.
f"P-Value : {stats.shapiro(data_clean_y["Log_Guncel_Fiyat"])[1]:.5f}"

# Log alınıp, shapiro testine göre, H0 Red edilir. Dolayısıyla, bağımlı değişkenimiz normal dağılıma sahip değildir.
# Basıklık ve çarpıklık değerlerine göre test yapan, Jarque-Bera testi yapacağım.
# Jarque-Bera Testi
jb_test = stats.jarque_bera(data_clean_y["Log_Guncel_Fiyat"])
f"T-Statistic : {jb_test[0]:.4f}" # Daha okunabilir.
f"P-Value : {jb_test[1]:.5f}"