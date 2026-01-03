# 🚀 YouTube Mix to MP3 Downloader

Script Python buat download lagu massal dari YouTube Mix atau Playlist. Gak perlu download satu-satu lagi, tinggal sekali run langsung jadi koleksi MP3!

### 🧠 Otak, Tangan, & Pisau (Tools):
* **Python 3.14 (Otak):** Engine utama buat jalanin script.
* **yt-dlp (Tangan):** Library sakti buat narik stream audio dari YouTube.
* **FFmpeg (Pisau):** Alat buat potong dan convert file ke format MP3.

# Ganti pake link YouTube Mix atau Playlist kesukaan lu
LINK_MIX = "[https://www.youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID](https://www.youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID)"
---

### 🕹️ Cara Install (Langkah demi Langkah):

1. **Bikin File Script:**
   Bikin file Python di VS Code, kasih nama contoh: `download_mp3.py`.

2. **Install Library Utama:**
   Buka terminal di VS Code (View -> Terminal), lalu ketik:
   ```powershell
   pip install yt-dlp

Install Converter (FFmpeg): Ketik perintah ini di terminal buat pasang "pisaunya":
 ```
winget install ffmpeg

