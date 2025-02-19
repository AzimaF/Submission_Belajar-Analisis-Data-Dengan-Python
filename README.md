# Proyek Analisis Data - Dicoding

## Penulis
- **Nama:** Fauzan Azima
- **Email:** azzamfauzan21@gmail.com
- **Username Dicoding:** fa_zima26

## Persiapan Lingkungan - Shell/Terminal
Untuk memulai proyek ini, lakukan langkah-langkah berikut di terminal:
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Struktur Berkas
- `Proyek_Analisis_Data.ipynb`: Jupyter Notebook yang berisi analisis data.
- `dashboard/`: Folder yang berisi aplikasi dashboard berbasis Streamlit.

## Menjalankan Dashboard Streamlit
Jupyter Notebook dapat dibuka langsung melalui GitHub atau dijalankan di lingkungan yang mendukung Python.
Untuk menjalankan dashboard Streamlit secara lokal, ikuti langkah berikut:
```
cd dashboard
streamlit run dashboard.py
```

## Menjalankan Dashboard di Command Prompt
Pastikan Anda sudah berada di dalam folder `dashboard` sebelum menjalankan aplikasi Streamlit:
```
cd dashboard
streamlit run dashboard.py
```
Dengan menjalankan perintah di atas, dashboard akan otomatis terbuka di browser Anda.

## Menjalankan Streamlit di Localhost
1. Unduh dataset dalam format `.csv` yang dibutuhkan.
2. Jalankan kode dalam `dashboard.py` untuk melakukan Exploratory Data Analysis (EDA).
3. Instal Streamlit melalui command prompt dengan perintah:
```
pip install streamlit
```
4. Setelah instalasi selesai, navigasikan ke folder `dashboard` dan jalankan:
```
cd dashboard
streamlit run dashboard.py
```
5. Dashboard akan terbuka di browser secara lokal.

## Fitur Dashboard Streamlit
Dashboard yang dibuat mencakup fitur berikut:
1. Tampilan interaktif data mentah dan statistik ringkas.
2. Visualisasi data untuk menjawab pertanyaan bisnis utama:
   - Apakah ada pola tren yang terlihat? Jika iya, bagaimana polanya, dan di bulan serta tahun berapa jumlah pengguna mencapai puncaknya?
   - Berdasarkan analisis, jumlah pengguna sepeda meningkat secara konsisten dari Januari hingga Juni, dengan puncaknya di bulan Juni. Apakah peningkatan ini menunjukkan bahwa cuaca yang lebih hangat pada bulan April, Mei, dan Juni berdampak positif terhadap minat masyarakat untuk bersepeda?

## Kebutuhan dan Instalasi
Proyek ini membutuhkan pustaka berikut agar dapat berjalan dengan optimal:
- matplotlib==3.10.0
- matplotlib-inline==0.1.7
- numpy==2.2.3
- Pandas 2.2.3
- Seaborn 0.13.2
- Streamlit 1.42.0
