# Gayrimenkul Fiyat Regresyon Analizi

## Proje Açıklaması
Bu proje, Ankara-Çankaya bölgesindeki belirli mahallelerde 2018-2023 yılları arasındaki gayrimenkul fiyatlarının analizini içermektedir. Proje kapsamında fiyatlar Yİ-ÜFE kullanılarak güncel değerlere getirilmiş ve regresyon analizi için veri hazırlığı yapılmıştır.

## Veri Seti
- **Zaman Aralığı**: 2018-2023
- **Bölge**: Ankara-Çankaya (22 mahalle)
- **Veri Kaynakları**: 
  - Gayrimenkul fiyat verileri
  - TÜİK Yİ-ÜFE verileri

## Metodoloji
1. **Veri Ön İşleme**
   - Eksik değerlerin doldurulması
   - Veri tipi dönüşümleri
   - Kategorik değişkenlerin belirlenmesi
   - Bina yaşı gruplandırması

2. **Fiyat Güncellemesi**
   - Yİ-ÜFE kullanılarak geçmiş fiyatların güncellenmesi
   - Enflasyon etkisinin normalize edilmesi

3. **İstatistiksel Analiz**
   - Normallik testleri (Shapiro-Wilk, Kolmogorov-Smirnov)
   - Çarpıklık ve basıklık analizi
   - Aykırı değer tespiti (IQR yöntemi)
   - Logaritmik dönüşüm

## Kullanılan Teknolojiler
- Python 3.x
- Pandas
- NumPy
- Seaborn
- Matplotlib
- SciPy

## Kurulum
```bash
git clone [repo-url]
cd RealEstate_Regression
pip install -r requirements.txt
```

## Klasör Yapısı
```
RealEstate_Regression/
│
├── Data/                   # Veri dosyaları (gitignore'da)
├── .gitignore             # Git dışında tutulan dosyalar
├── Regression.py          # Ana kod dosyası
└── README.md              # Proje dokümantasyonu
```

