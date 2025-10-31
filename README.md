# 🗺️ Modul Visualisasi Geospasial Dasar

**Pemilik:** Dahlan  
**Target:** Mahasiswa tingkat awal-menengah

---

## 📖 Deskripsi

Modul ini mengajarkan dasar-dasar visualisasi peta menggunakan Python. Anda akan belajar:
- Bagaimana peta digital bekerja (koordinat, proyeksi, layer)
- Cara membuat peta menggunakan kode Python
- Perbandingan berbagai alat visualisasi peta

**Mengapa penting?** Visualisasi geospasial membantu kita memahami data berbasis lokasi seperti persebaran toko, peta kejadian, atau analisis wilayah.

---

## 🎯 Tujuan Pembelajaran

Setelah menyelesaikan modul ini, Anda akan dapat:

1. **Memahami konsep dasar peta digital**
   - Sistem koordinat (latitude, longitude)
   - Proyeksi peta (WGS84/EPSG:4326)
   - Jenis layer: titik (point), garis (line), poligon (polygon)

2. **Membuat peta dengan Python**
   - Peta statis menggunakan GeoPandas
   - Peta interaktif dengan Folium (marker, popup, cluster)
   - Peta interaktif dengan Plotly (scatter map, tooltips)

3. **Membandingkan alat visualisasi**
   - Kapan menggunakan kode vs GUI (QGIS/Kepler)
   - Kelebihan dan kekurangan masing-masing alat

---

## 📁 Struktur Repositori

```
datavis-geospasial/
├── notebooks/           # 3 notebook praktikum (MULAI DI SINI!)
│   ├── 01_pengenalan_peta.ipynb
│   ├── 02_alat_visualisasi_geospasial.ipynb
│   └── 03_latihan_tugas.ipynb
├── data/
│   ├── raw/            # Data mentah dan contoh
│   │   ├── umkm_sample.csv
│   │   └── indonesia_admin.geojson
│   └── processed/      # Data hasil olahan
├── assets/
│   ├── img/            # Gambar untuk dokumentasi
│   └── css/            # Styling (opsional)
├── scripts/            # Skrip bantu
├── exports/            # Hasil export peta (HTML/PDF/PPTX)
├── README.md           # File ini
└── requirements.txt    # Daftar paket Python
```

---

## 🚀 Cara Memulai

### ⚡ Quick Start (Sudah Dioptimasi!)

Notebook sekarang **5-10x lebih cepat** berkat optimasi loading data!
- Pertama kali: 1-2 detik
- Reload dengan cache: 0.2-0.3 detik ⚡

📖 **Baca:** [TIPS_CEPAT.md](TIPS_CEPAT.md) untuk penjelasan singkat  
📖 **Detail:** [OPTIMASI.md](OPTIMASI.md) untuk detail teknis lengkap

---

### Langkah 1: Persiapan Environment

**Opsi A: Menggunakan venv (disarankan untuk pemula)**
```bash
# Buat virtual environment
python3 -m venv venv

# Aktifkan environment
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate     # Windows

# Install paket
pip install -r requirements.txt
```

**Opsi B: Menggunakan conda**
```bash
# Buat environment baru
conda create -n geo python=3.10

# Aktifkan
conda activate geo

# Install paket
pip install -r requirements.txt
```

### Langkah 2: Jalankan Jupyter

```bash
# Jalankan Jupyter Lab (interface modern)
jupyter lab

# ATAU Jupyter Notebook (interface klasik)
jupyter notebook
```

### Langkah 3: Buka Notebook Pertama

1. Di Jupyter, navigasi ke folder `notebooks/`
2. Buka `01_pengenalan_peta.ipynb`
3. Jalankan sel per sel dengan menekan `Shift + Enter`
4. Ikuti instruksi dan coba latihan di setiap notebook

---

## 📚 Urutan Belajar

Ikuti notebook secara berurutan:

1. **Notebook 01 - Pengenalan Peta** (⏱️ 30-45 menit)
   - Konsep koordinat dan proyeksi
   - Membuat peta statis dengan GeoPandas
   - Latihan: menampilkan titik UMKM

2. **Notebook 02 - Alat Visualisasi** (⏱️ 45-60 menit)
   - Demo Folium (marker & popup)
   - Demo Plotly (scatter mapbox)
   - Perbandingan alat (tabel lengkap)
   - Latihan: kustomisasi warna & tooltip

3. **Notebook 03 - Latihan & Tugas** (⏱️ 60-90 menit)
   - Tugas praktikum: peta persebaran UMKM
   - Contoh agregasi dan clustering
   - Rubrik penilaian

---

## 📦 Paket yang Digunakan

| Paket | Fungsi |
|-------|--------|
| `pandas` | Manipulasi data tabular (CSV, Excel) |
| `geopandas` | Analisis & visualisasi data geospasial |
| `folium` | Peta interaktif berbasis Leaflet.js |
| `plotly` | Visualisasi interaktif (termasuk peta) |
| `matplotlib` | Plot dasar untuk visualisasi |
| `jupyter` | Environment notebook interaktif |

**Opsional (untuk fitur lanjutan):**
- `shapely`: manipulasi geometri
- `pyproj`: transformasi koordinat
- `contextily`: basemap dari web tiles

---

## 💡 Tips Belajar

1. **Jalankan kode sambil baca** - Jangan hanya membaca, eksekusi setiap sel kode!
2. **Ubah-ubah parameter** - Coba ganti warna, zoom level, atau filter data
3. **Catat error** - Error adalah guru terbaik, baca pesan error dengan teliti
4. **Eksplorasi data** - Lihat isi CSV dan GeoJSON untuk memahami strukturnya
5. **Tanya jika bingung** - Diskusikan dengan teman atau instruktur

---

## ⚡ Optimasi Performa

Modul ini menggunakan beberapa teknik untuk memastikan loading data **cepat** dan **efisien**:

### 1. **Lazy Loading**
- Data besar (seperti kelurahan) hanya dimuat saat benar-benar dibutuhkan
- Menghemat waktu & memori untuk pembelajaran dasar

### 2. **Simplifikasi Geometri**
- Polygon disederhanakan untuk mengurangi kompleksitas
- Trade-off: Detail berkurang ~1-5%, **kecepatan naik 5-10x**
- Materi tetap tersampaikan dengan baik

### 3. **Caching Otomatis**
- File GeoJSON yang sudah diproses disimpan di `data/cache/`
- **Pertama kali**: 1-3 detik
- **Loading ulang**: 0.1-0.3 detik ⚡⚡⚡

### 4. **Prioritas Data**
- **Essential** (selalu dimuat): Kabupaten, Kecamatan
- **On-demand** (opsional): Kelurahan/Desa (untuk detail maksimal)

### Hasil Optimasi:
```
✅ Loading 5-10x lebih cepat
✅ Plotting 3-5x lebih cepat  
✅ Materi tetap tersampaikan dengan baik
✅ Tidak terlalu kompleks
```

**Catatan**: Cache otomatis dibuat saat pertama kali menjalankan notebook. Jika file GeoJSON berubah, cache akan diperbarui otomatis.

---

## 🔧 Troubleshooting

### Masalah instalasi paket
```bash
# Jika pip install gagal, coba update pip dulu
pip install --upgrade pip

# Lalu install ulang
pip install -r requirements.txt
```

### Peta tidak muncul
- Pastikan Jupyter sudah dijalankan dari folder root proyek
- Cek koneksi internet (untuk map tiles Folium/Plotly)
- Untuk offline, gunakan tiles default atau saved HTML

### Path file tidak ditemukan
- Pastikan menjalankan notebook dari folder `notebooks/`
- Kode sudah menggunakan path relatif otomatis

---

## 📊 Dataset

Modul ini menggunakan:
1. **umkm_sample.csv** - Data dummy UMKM di Jawa Timur (10 baris)
   - Kolom: id, nama, kota, kecamatan, lat, lon, jenis, skor

2. **indonesia_admin.geojson** - Placeholder batas Jawa Timur
   - Format: GeoJSON dengan 1 polygon

**Untuk proyek riil**, Anda bisa menggunakan:
- [Natural Earth](https://www.naturalearthdata.com/) - batas negara/provinsi
- [OpenStreetMap](https://www.openstreetmap.org/) - jalan, POI, bangunan
- [Data.go.id](https://data.go.id/) - data pemerintah Indonesia

---

## 📝 Evaluasi

Setiap notebook memiliki:
- **Latihan singkat** - untuk menguji pemahaman konsep
- **Jawaban/hint** - disediakan di akhir latihan
- **Tugas akhir** (Notebook 03) - dengan rubrik penilaian:
  - Data benar & lengkap: 30%
  - Peta interaktif berfungsi: 40%
  - Insight/narasi: 30%

---

## 📄 Lisensi

Materi ini tersedia untuk tujuan pembelajaran.  
Silakan dimodifikasi sesuai kebutuhan kelas Anda.

---

## 🤝 Kontribusi

Jika menemukan error atau punya saran perbaikan:
1. Catat masalah yang ditemukan
2. Diskusikan dengan instruktur
3. Bantu perbaiki untuk mahasiswa berikutnya

---

**Selamat belajar! 🎓**