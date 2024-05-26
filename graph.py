import matplotlib.pyplot as plt

#Veriler
data = {
    "ks_19_0": 0.203,
    "ks_50_0": 5.398,
    "ks_100_2": 0.288,
    "ks_500_0": 8.149,
    "ks_10000_0": 243.791
}

#Boyut ve süre listelerini oluştur
dosyalar = []
sureler = []

for key, value in data.items():
    dosyalar.append(key)
    sureler.append(value)

#Grafik oluşturma
plt.figure(figsize=(10, 5))
plt.plot(dosyalar, sureler, marker='o', linestyle='-', color='b')

#Grafik başlıkları ve etiketleri
plt.title('Boyut-Zaman Grafiği')
plt.xlabel('Dosya Adı')
plt.ylabel('Süre (saniye)')
plt.grid(True)

#x eksenindeki dosya adlarını döndürerek yazdırma
plt.xticks(rotation=45, ha='right')

#Göster
plt.tight_layout()  # Etiketlerin kesilmemesi için
plt.show()