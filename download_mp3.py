import yt_dlp
import os

# --- KONFIGURASI DI SINI NGAB ---
# 1. Masukin Link Mix YouTube lu di bawah ini:
LINK_MIX = "https://www.youtube.com/watch?v=SgV4ndY1Yc8&list=RDMMZuBAjNqMiWk"  # <-- Ganti pake link lu

# 2. Mau download berapa lagu? (JANGAN RAKUS, ingat Mix itu infinite)
# Gw saranin 20 - 50 dulu buat ngetes.
JUMLAH_LAGU = 30
# -------------------------------

def sikat_mix_mp3(url, limit):
    output_folder = "lagu_mix_downloadmp3"
    
    # Bikin folder kalo belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    print(f"🔥 Siap memanen {limit} lagu dari Mix...")
    print(f"📂 Lokasi simpen: {os.path.abspath(output_folder)}")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s', # Nama file: Judul Lagu.mp3
        'playlistend': limit, # INI REM-NYA. Dia bakal stop sesuai angka JUMLAH_LAGU
        'ignoreerrors': True, # Kalau ada 1 lagu error, lanjut ke lagu berikutnya
        'no_warnings': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n✅ MANTAP! {limit} lagu udah diamankan di folder '{output_folder}'.")
    except Exception as e:
        print(f"❌ Yah error: {e}")

if __name__ == "__main__":
    # Panggil fungsinya
    sikat_mix_mp3(LINK_MIX, JUMLAH_LAGU)