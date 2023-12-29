import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog, simpledialog
from ttkthemes import ThemedStyle
import requests
import json
import folium
import webbrowser
from folium.plugins import MarkerCluster
import os


class AirportApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Havaalanı Bilgi Uygulaması")
        self.airports_data = {}

        # GUI öğelerini oluştur
        self.create_widgets()
        # Temayı ayarla
        self.set_theme()

    def set_theme(self):
        # ThemedStyle sınıfını kullanarak temayı ayarla
        style = ThemedStyle(self.root)
        style.set_theme("elegance")

    def create_widgets(self):
        # Ana çerçeve
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Havaalanları tablosunu gösteren buton
        show_table_button = ttk.Button(
            frame, text="Havaalanları Tablosu", command=self.show_airports_table
        )
        show_table_button.grid(column=0, row=0, sticky=tk.W, pady=5, padx=5)

        # Havaalanlarını haritada gösteren buton
        show_map_button = ttk.Button(
            frame, text="Havaalanları Haritası", command=self.show_airports_map
        )
        show_map_button.grid(column=1, row=0, sticky=tk.W, pady=5, padx=5)

        # Havaalanı verilerini dosyadan okuyan buton
        read_file_button = ttk.Button(
            frame, text="Dosyadan Oku", command=self.read_airports_from_file
        )
        read_file_button.grid(column=2, row=0, sticky=tk.W, pady=5, padx=5)

        # Havaalanlarının hava durumunu gösteren buton
        weather_button = ttk.Button(frame, text="Hava Durumu", command=self.get_weather)
        weather_button.grid(column=3, row=0, sticky=tk.W, pady=5, padx=5)

    def read_airports_from_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON Files", "*.json"), ("CSV Files", "*.csv")]
        )

        if file_path:
            try:
                # JSON dosyası okuma kodu
                if file_path.lower().endswith(".json"):
                    with open(file_path, "r") as file:
                        self.airports_data = json.load(file)

                    # Havaalanı verilerini içeren anahtar kontrolü
                    if "havaalanlari" in self.airports_data:
                        messagebox.showinfo(
                            "Başarılı", "Havaalanı verileri başarıyla okundu."
                        )
                    else:
                        messagebox.showwarning(
                            "Uyarı",
                            "Havaalanı verileri bulunamadı veya uygun formatta değil.",
                        )
            except Exception as e:
                messagebox.showerror("Hata", f"Hata oluştu: {str(e)}")

    def show_airports_table(self):
        if self.airports_data and "havaalanlari" in self.airports_data:
            # Yeni bir pencere oluştur
            table_window = tk.Toplevel(self.root)
            table_window.title("Havaalanları Tablosu")

            # Tablo oluştur
            tree = ttk.Treeview(table_window)
            tree["columns"] = tuple(self.airports_data["havaalanlari"][0].keys())

            # Sütun başlıklarını ayarla
            for col in tree["columns"]:
                tree.heading(col, text=col)
                tree.column(col, anchor="center", width=100)

            # Verileri tabloya ekle
            for data in self.airports_data["havaalanlari"]:
                tree.insert("", "end", values=tuple(data.values()))

            tree.pack(expand=True, fill="both")
        else:
            messagebox.showinfo("Uyarı", "Havaalanı verileri bulunamadı veya boş.")

    def get_weather_data(self, lat, lon):
        api_key = "b8e0ccbdb7c69e1fb02f4c163e2b12af"
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"lat": lat, "lon": lon, "appid": api_key, "units": "metric"}
        response = requests.get(base_url, params=params)
        data = response.json()
        return data

    def show_airports_map(self):
        if self.airports_data and "havaalanlari" in self.airports_data:
            map_window = tk.Toplevel(self.root)
            map_window.title("Havaalanları Haritası")
            map_window.geometry("800x600")
            map_window.transient(self.root)
            map_window.grab_set()
            map_window.update()

            m = folium.Map(
                location=[39.9334, 32.8597],
                zoom_start=6,
                control_scale=True,
                favicon=None,
                prefer_canvas=True,
            )
            # Havaalanlarını haritaya ekledim
            for data in self.airports_data["havaalanlari"]:
                if (
                    isinstance(data, dict)
                    and "Latitude" in data
                    and "Longitude" in data
                ):
                    try:
                        lat, lon = float(data["Latitude"]), float(data["Longitude"])
                        weather_data = self.get_weather_data(lat, lon)
                        temperature = weather_data.get("main", {}).get(
                            "temp", "Bilinmiyor"
                        )
                        popup_content = (
                            f"{data.get('isim', '')}<br>Sıcaklık: {temperature}°C"
                        )
                        folium.Marker([lat, lon], popup=popup_content).add_to(m)
                    except ValueError:
                        print(f"Hata: Geçersiz Latitude veya Longitude değeri: {data}")
                else:
                    print(f"Hata: {data} bir sözlük değil veya eksik alanlara sahip.")

            # Haritayı HTML dosyasına kaydet ve tarayıcıda aç
            m.save("airports_map.html")
            webbrowser.open("file://" + os.path.abspath("airports_map.html"))

            # Haritayı HTML dosyasına kaydet ve tarayıcıda aç
            m.save("airports_map.html")
            webbrowser.open("file://" + os.path.abspath("airports_map.html"))

            # Pencere içeriğini güncelle
            map_window.update_idletasks()
        else:
            messagebox.showinfo("Uyarı", "Lütfen önce havaalanı verilerini okuyun.")

    def get_weather(self):
        def kelvin_to_celsius(kelvin):
            return kelvin - 273.15

        if self.airports_data and "havaalanlari" in self.airports_data:
            # Kullanıcının seçim yapmasını sağla
            selected_airport = simpledialog.askstring(
                "Havaalanı Seç",
                "Hava durumu bilgisini almak istediğiniz havaalanını girin:",
            )

            if selected_airport:
                # Seçilen havaalanının verilerini bul
                selected_airport_data = next(
                    (
                        data
                        for data in self.airports_data["havaalanlari"]
                        if data.get("isim") == selected_airport
                    ),
                    None,
                )

                if selected_airport_data:
                    # OpenWeatherMap API'inden hava durumu verilerini al
                    api_key = "b8e0ccbdb7c69e1fb02f4c163e2b12af"  # OpenWeatherMap API anahtarını buraya ekleyin
                    url = f"http://api.openweathermap.org/data/2.5/weather?lat={selected_airport_data['Latitude']}&lon={selected_airport_data['Longitude']}&appid={api_key}"

                    try:
                        response = requests.get(url)
                        response.raise_for_status()
                        weather_data = response.json()

                        # Sıcaklık değerini Kelvin'den Celsius'a dönüştür
                        temperature_kelvin = weather_data["main"]["temp"]
                        temperature_celsius = kelvin_to_celsius(temperature_kelvin)

                        # Hava durumu verilerini göster
                        description = weather_data["weather"][0]["description"]
                        messagebox.showinfo(
                            "Hava Durumu",
                            f"{selected_airport} Hava Durumu: {description}\nSıcaklık: {temperature_celsius:.2f}°C",
                        )
                    except requests.exceptions.RequestException as e:
                        print(f"Hava durumu bilgisi alınamadı: {e}")
                        messagebox.showinfo("Hata", "Hava durumu bilgisi alınamadı.")
                else:
                    messagebox.showinfo(
                        "Uyarı", "Seçilen havaalanı verileri bulunamadı."
                    )
        else:
            messagebox.showinfo("Uyarı", "Lütfen önce havaalanı verilerini okuyun.")


#! Uygulama penceresini oluştur
root = tk.Tk()
app = AirportApp(root)
root.mainloop()
