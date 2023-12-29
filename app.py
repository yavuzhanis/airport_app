import json

# Oluşturulacak veri
veri = {
    "havaalanlari": [
    {"isim": "Adana Şakirpaşa Havalimanı", "kod": "LTAF", "sehir": "Adana", "Latitude": 36.9822, "Longitude": 35.2803},
    {"isim": "Ankara Esenboğa Havalimanı", "kod": "LTAC", "sehir": "Ankara", "Latitude": 40.1281, "Longitude": 32.9956},
    {"isim": "Antalya Havalimanı", "kod": "LTAI", "sehir": "Antalya", "Latitude": 36.9003, "Longitude": 30.7939},
    {"isim": "Gazipaşa Havalimanı", "kod": "LTFG", "sehir": "Alanya", "Latitude": 36.2992, "Longitude": 32.3014},
    {"isim": "Balıkesir Koca Seyit Havalimanı", "kod": "LTFD", "sehir": "Balıkesir", "Latitude": 39.5525, "Longitude": 27.0103},
    {"isim": "Bursa Yenişehir Havalimanı", "kod": "LTBR", "sehir": "Bursa", "Latitude": 40.2558, "Longitude": 29.5619},
    {"isim": "Çanakkale Havalimanı", "kod": "LTBH", "sehir": "Çanakkale", "Latitude": 40.1375, "Longitude": 26.4308},
    {"isim": "Denizli Çardak Havalimanı", "kod": "LTAY", "sehir": "Denizli", "Latitude": 37.7878, "Longitude": 29.705},
    {"isim": "Diyarbakır Havalimanı", "kod": "LTCC", "sehir": "Diyarbakır", "Latitude": 37.9011, "Longitude": 40.1858},
    {"isim": "Elazığ Havalimanı", "kod": "LTCA", "sehir": "Elazığ", "Latitude": 38.5975, "Longitude": 39.2814},
    {"isim": "Erzurum Havalimanı", "kod": "LTCE", "sehir": "Erzurum", "Latitude": 39.9569, "Longitude": 41.1706},
    {"isim": "Eskişehir Hasan Polatkan Havalimanı", "kod": "LTBY", "sehir": "Eskişehir", "Latitude": 39.8125, "Longitude": 30.5281},
    {"isim": "Gaziantep Havalimanı", "kod": "LTAJ", "sehir": "Gaziantep", "Latitude": 36.9478, "Longitude": 37.4789},
    {"isim": "Hatay Havalimanı", "kod": "LTDA", "sehir": "Hatay", "Latitude": 36.3722, "Longitude": 36.2986},
    {"isim": "Isparta Süleyman Demirel Havalimanı", "kod": "LTFC", "sehir": "Isparta", "Latitude": 37.8558, "Longitude": 30.3669},
    {"isim": "İstanbul Havalimanı", "kod": "LTFM", "sehir": "İstanbul", "Latitude": 41.2608, "Longitude": 28.7422},
    {"isim": "Sabiha Gökçen Havalimanı", "kod": "LTFJ", "sehir": "İstanbul", "Latitude": 40.8942, "Longitude": 29.3083},
    {"isim": "Adnan Menderes Havalimanı", "kod": "LTBJ", "sehir": "İzmir", "Latitude": 38.2892, "Longitude": 27.155},
    {"isim": "Kars Harakani Havalimanı", "kod": "LTCF", "sehir": "Kars", "Latitude": 40.5622, "Longitude": 43.1147},
    {"isim": "Erkilet Havalimanı", "kod": "LTAU", "sehir": "Kayseri", "Latitude": 38.7703, "Longitude": 35.4953},
    {"isim": "Cengiz Topel Havalimanı", "kod": "LTBQ", "sehir": "Kocaeli", "Latitude": 40.735, "Longitude": 30.0833},
    {"isim": "Konya Havalimanı", "kod": "LTAN", "sehir": "Konya", "Latitude": 37.9806, "Longitude": 32.5625},
    {"isim": "Zafer Havalimanı", "kod": "LTBZ", "sehir": "Kütahya", "Latitude": 39.1114, "Longitude": 30.13},
    {"isim": "Malatya Havalimanı", "kod": "LTAT", "sehir": "Malatya", "Latitude": 38.4322, "Longitude": 38.0831},
    {"isim": "Dalaman Havalimanı", "kod": "LTBS", "sehir": "Muğla", "Latitude": 36.7125, "Longitude": 28.7914},
    {"isim": "Milas-Bodrum Havalimanı", "kod": "LTFE", "sehir": "Muğla", "Latitude": 37.2494, "Longitude": 27.6647},
    {"isim": "Nevşehir Kapadokya Havalimanı", "kod": "LTAZ", "sehir": "Nevşehir", "Latitude": 38.7753, "Longitude": 34.5267},
    {"isim": "Ordu-Giresun Havalimanı", "kod": "LTCB", "sehir": "Ordu", "Latitude": 40.9672, "Longitude": 38.0822},
    {"isim": "Rize-Artvin Havalimanı", "kod": "LTFO", "sehir": "Rize-Artvin", "Latitude": 41.1683, "Longitude": 40.8294},
    {"isim": "Trabzon Havalimanı", "kod": "TZX", "sehir": "Trabzon", "Latitude":40.9951, "Longitude":39.7899},
    {"isim": "Samsun Çarşamba Havalimanı", "kod": "LTFH", "sehir": "Samsun","Latitude":41.1169,"Longitude":36.4822},
    {"isim": "Van Ferit Melen Havalimanı", "kod": "LTCI", "sehir": "Van","Latitude":38.4681,"Longitude":43.3322},
    {"isim": "Şanlıurfa GAP Havalimanı", "kod": " LTCH", "sehir": "Şanlıurfa","Latitude":37.2236,"Longitude": 38.8611},
    {"isim": "Mardin Havalimanı", "kod": " LTCR", "sehir": "Mardin","Latitude":37.2231,"Longitude":40.6394},
    {"isim": "Amasya Merzifon Havalimanı", "kod": " LTBF", "sehir": "Amasya / Merzifon","Latitude":40.8294,"Longitude":35.5219},

    

    ]
}


# JSON dosyasına yazma
dosya_adı = "airports_data.json"
with open(dosya_adı, "w") as dosya:
    json.dump(veri, dosya)

print(f"{dosya_adı} adlı JSON dosyası oluşturuldu.")
