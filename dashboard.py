# Import library yang digunakan
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
import streamlit as st  
import datetime  

# Mengatur gaya tampilan seaborn
sns.set(style='darkgrid')

# Membaca dataset dari file CSV
day_df = pd.read_csv("all_data.csv")

# Menampilkan 5 baris pertama dari dataset
day_df.head()

# Menghapus kolom yang tidak diperlukan dalam analisis
drop_col = ['instant', 'temp', 'atemp', 'hum', 'windspeed']
day_df.drop(columns=drop_col, inplace=True)

# Mengubah nilai numerik menjadi kategori yang lebih mudah dipahami
day_df['yr'] = day_df['yr'].map({0: '2011', 1: '2012'})  # Mengubah tahun ke format string
day_df['mnth'] = day_df['mnth'].map({1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April', 5: 'Mei', 6: 'Juni', 7: 'Juli', 8: 'Agustus', 9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'})  # Nama nama bulan
day_df['season'] = day_df['season'].map({1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'})  # Musim
day_df['weekday'] = day_df['weekday'].map({0: 'Minggu', 1: 'Senin', 2: 'Selasa', 3: 'Rabu', 4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'})  # Nama nama hari
day_df['weathersit'] = day_df['weathersit'].map({1: 'Cuaca Cerah', 2: 'Cuaca Berawan', 3: 'Cuaca Hujan atau Salju Ringan', 4: 'Cuaca Buruk'})  # Kondisi cuaca permusim

# Mengubah kolom tanggal ke format datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Mengubah beberapa kolom menjadi tipe data kategori untuk optimasi
day_df[['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']] = day_df[
    ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']
].astype('category')

# Fungsi untuk membuat DataFrame jumlah penyewa per bulan
def create_monthly_rent_df(df):
    monthly_rent_df = df.groupby(by='mnth').agg({'cnt': 'sum'}).reset_index()  # Mengelompokkan data berdasarkan bulan
    ordered_months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']  # Urutan bulan
    monthly_rent_df['mnth'] = pd.Categorical(monthly_rent_df['mnth'], categories=ordered_months, ordered=True)  # Menjaga urutan bulan
    return monthly_rent_df

# Fungsi untuk membuat DataFrame berdasarkan musim dan kondisi cuaca
def create_season_weather_df(df):
    season_weather_df = df.groupby(['season', 'weathersit']).agg({'cnt': 'mean'}).reset_index()  # Menghitung rata-rata jumlah pengguna
    return season_weather_df

# Menampilkan header aplikasi di Streamlit
st.header('DATA ANALISIS PENGGUNAAN SEPEDA PADA TAHUN 2012')

# Input pengguna untuk memilih rentang tanggal
start_date = st.date_input("Tanggal Awal", value=datetime.date(2012, 1, 1))  # Default: 1 Januari 2011
end_date = st.date_input("Tanggal Akhir", value=datetime.date(2012, 12, 31))  # Default: 30 Juni 2011

# Memfilter data berdasarkan rentang tanggal yang dipilih pengguna
filtered_day_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & (day_df['dteday'] <= pd.to_datetime(end_date))]

# Membuat DataFrame jumlah penyewa sepeda per bulan berdasarkan data yang telah difilter
monthly_rent_df = create_monthly_rent_df(filtered_day_df)

# Membuat dua kolom layout di Streamlit
col1, col2 = st.columns([2, 1])  # Kolom kiri lebih besar dari kolom kanan

# Menampilkan grafik jumlah total penyewa sepeda per bulan
with col1:
    st.subheader('Jumlah Total Penyewa Sepeda per Bulan')
    fig, ax = plt.subplots(figsize=(14, 10))
    sns.barplot(data=monthly_rent_df, x='mnth', y='cnt', ax=ax)  # Membuat grafik batang
    ax.set_title(f'Jumlah Total Penyewa Sepeda dari {start_date} sampai {end_date}', fontsize=20)
    ax.set_xlabel('Bulan', fontsize=20)
    ax.set_ylabel('Jumlah Penyewa', fontsize=20)
    ax.grid(axis='y')
    st.pyplot(fig)  # Menampilkan grafik di Streamlit

    if not monthly_rent_df.empty:
        max_users = monthly_rent_df.loc[monthly_rent_df['cnt'].idxmax()]  # Mencari bulan dengan jumlah pengguna tertinggi
        st.write(f"Jumlah pengguna tertinggi terjadi pada bulan **{max_users['mnth']}** "
                 f"dengan total {max_users['cnt']} penyewa sepeda.")  # Menampilkan informasi
    else:
        st.write("Tidak ada data untuk rentang tanggal yang dipilih.")  # Menampilkan pesan jika tidak ada data

with col2:
    # Menampilkan dropdown untuk memilih bulan
    st.subheader('Pilih Bulan')
    
    # Pastikan daftar bulan diambil dari semua bulan yang tersedia dalam kategori
    available_months = list(monthly_rent_df['mnth'].cat.categories)
    
    selected_month = st.selectbox("Pilih bulan untuk melihat jumlah penyewa:", available_months)
    
    # Memeriksa apakah data tersedia untuk bulan yang dipilih
    selected_data = monthly_rent_df[monthly_rent_df['mnth'] == selected_month]
    
    if not selected_data.empty:
        st.write(f"Jumlah penyewa sepeda pada bulan **{selected_month}** yaitu dengan total {selected_data['cnt'].values[0]}")
    else:
        st.write(f"Tidak ada data penyewa sepeda untuk bulan **{selected_month}** dalam rentang tanggal yang dipilih.")


# Membuat DataFrame rata-rata jumlah penyewa sepeda berdasarkan musim dan kondisi cuaca
    season_weather_df = create_season_weather_df(filtered_day_df)

# Menampilkan grafik rata-rata jumlah pengguna sepeda berdasarkan kondisi cuaca dan musim
st.subheader('Rata-Rata Pengguna Sepeda Berdasarkan Cuaca dan Musim')
fig2, ax2 = plt.subplots(figsize=(14, 10))

if not season_weather_df.empty:
    sns.barplot(data=season_weather_df, x='weathersit', y='cnt', hue='season', palette='Set2', ax=ax2)  # Grafik batang
    ax2.set_title('Rata-Rata Pengguna Sepeda Berdasarkan Kondisi Cuaca dan Musim')
    ax2.set_xlabel('Kondisi Cuaca')
    ax2.set_ylabel('Rata-Rata Jumlah Pengguna Sepeda')
    ax2.legend(title='Musim', loc='upper right')
    st.pyplot(fig2)  # Menampilkan grafik di Streamlit

    # Menampilkan kondisi cuaca dengan rata-rata pengguna tertinggi
    max_usage = season_weather_df.loc[season_weather_df['cnt'].idxmax()]  # Mencari kondisi cuaca dengan jumlah pengguna tertinggi
    st.write(f"Rata-rata pengguna tertinggi terjadi pada kondisi **{max_usage['weathersit']}** "
             f"pada musim **{max_usage['season']}** dengan rata-rata {max_usage['cnt']:.2f} pengguna.")  # Menampilkan informasi
else:
    st.write("Tidak ada data untuk rentang tanggal yang dipilih.")  # Menampilkan pesan jika tidak ada data
# Menampilkan dropdown untuk memilih kondisi cuaca di col2

st.subheader('Pilih Kondisi Cuaca')

    # Pastikan daftar kondisi cuaca tersedia dalam kategori
available_weather = list(season_weather_df['weathersit'].unique())

selected_weather = st.selectbox("Pilih kondisi cuaca untuk melihat rata-rata jumlah pengguna:", available_weather)

    # Memeriksa apakah data tersedia untuk kondisi cuaca yang dipilih
selected_weather_data = season_weather_df[season_weather_df['weathersit'] == selected_weather]

if not selected_weather_data.empty:
        st.write(f"Detail rata-rata jumlah pengguna sepeda berdasarkan kondisi **{selected_weather}**:")
        for index, row in selected_weather_data.iterrows():
            st.write(f"- Musim **{row['season']}**: {row['cnt']:.2f} pengguna rata-rata")
else:
        st.write(f"Tidak ada data pengguna sepeda untuk kondisi cuaca **{selected_weather}** dalam rentang tanggal yang dipilih.")

