import requests
import pandas as pd

def dapatkan_data_populasi_world_bank():
    """Mengambil data populasi dari API World Bank"""
    
    # URL API World Bank untuk data populasi
    url = "http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=30000"
    
    try:
        print("Mengambil data dari World Bank API...")
        response = requests.get(url)
        data = response.json()
        
        # Data ada di elemen kedua dari response JSON
        records = data[1]
        
        # Konversi ke DataFrame pandas
        df = pd.DataFrame(records)
        
        # Filter kolom yang diperlukan
        df = df[['country', 'value', 'date']]
        df.columns = ['Negara', 'Populasi', 'Tahun']
        
        # Hapus baris dengan nilai populasi kosong
        df = df.dropna(subset=['Populasi'])
        
        print("Data berhasil diambil!")
        return df
    
    except Exception as e:
        print(f"Gagal mengambil data: {e}")
        return None

def simpan_ke_csv(df, data_populasi):
    """Menyimpan DataFrame ke file CSV"""
    df.to_csv(data_populasi, index=False)
    print(f"Data disimpan ke {data_populasi}")

if __name__ == "__main__":
    # Ambil data populasi
    data_populasi = dapatkan_data_populasi_world_bank()
    
    if data_populasi is not None:
        # Tampilkan 5 baris pertama
        print("\nContoh data:")
        print(data_populasi.head())
        
        # Simpan ke CSV
        simpan_ke_csv(data_populasi, "populasi_negara.csv")