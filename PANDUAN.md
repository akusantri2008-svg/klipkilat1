# Klipkilat: pasang sebagai aplikasi

Klipkilat memotong video panjang jadi klip pendek. Aplikasi menulis transkrip, memberi skor potensi viral di tiap bagian, lalu memotong klip 9:16 dengan subtitle yang menempel di video.

Ada dua cara memasangnya. Keduanya gratis dan tanpa Play Store.

## A. Di laptop Windows (klik dua kali)

1. Ekstrak zip ke satu folder, misalnya `Documents\Klipkilat`.
2. Klik dua kali **Klipkilat.bat**.
   - Kalau Python 3.10 sampai 3.13 belum ada, jendela memberi tahu. Pasang dulu dari python.org (disarankan 3.12, centang "Add python.exe to PATH").
   - Pertama kali, jendela memasang kebutuhan aplikasi dan ffmpeg. Kalau ffmpeg baru terpasang, tutup jendela lalu klik Klipkilat.bat lagi.
3. Aplikasi terbuka di jendelanya sendiri. Jangan tutup jendela hitam selama dipakai.
4. Supaya punya ikon sendiri: di jendela aplikasi, klik menu titik tiga (kanan atas), pilih **Apps** lalu **Install this site as an app**. Atau klik tombol **Pasang aplikasi** di pojok halaman.

Buat pintasan di Desktop: klik kanan Klipkilat.bat, pilih **Send to** lalu **Desktop (create shortcut)**.

### Dipakai dari HP lewat laptop

Klik dua kali **Klipkilat-HP.bat**. Jendela menampilkan alamat seperti `http://192.168.1.5:7860`. Ketik alamat itu di Chrome HP yang tersambung ke Wi-Fi yang sama. Laptop harus menyala dan jendela hitam tetap terbuka. Kalau Windows bertanya soal Firewall, pilih **Allow access**, dan pakai hanya di Wi-Fi rumah sendiri.

Lewat cara ini Chrome HP tidak menawarkan pemasangan penuh karena alamatnya bukan HTTPS. Kamu tetap bisa menaruh pintasan: menu titik tiga lalu **Tambahkan ke layar utama**.

## B. Di HP, terpasang penuh (tanpa laptop menyala)

Ini memakai server gratis Hugging Face Space, jadi aplikasi bisa dibuka kapan saja dari HP.

1. Daftar atau masuk di huggingface.co.
2. Buka **New Space**. Nama bebas, pilih **Docker** lalu **Blank**, hardware **CPU basic (free)**, dan **Private**.
3. Di tab **Files**, pilih **Add file** lalu **Upload files**. Unggah file ini, semuanya di satu level tanpa folder: `Dockerfile`, `requirements.txt`, `main.py`, `pipeline.py`, `scoring.py`, `render.py`, `index.html`, `manifest.webmanifest`, `sw.js`, `icon-192.png`, `icon-512.png`, `apple-touch-icon.png`, `favicon.ico`. Jangan menimpa `README.md` milik Space.
4. Tunggu tab **App** selesai membangun (5 sampai 10 menit pertama kali), lalu buka Space-nya dalam tampilan penuh.
5. Di Chrome HP: menu titik tiga lalu **Pasang aplikasi** (atau **Tambahkan ke layar utama**). Ikon Klipkilat muncul di layar utama dan terbuka seperti aplikasi biasa.

Server gratis lebih lambat dari laptop dan bisa tidur kalau lama tidak dipakai. Link YouTube sering diblokir dari server ini, jadi untuk video yang sulit, unduh dulu lalu pakai "Dari file".

## Cara pakai

- **Dari link**: tempel link video lalu tekan Cari klip terbaik.
- **Dari file**: pilih video dari perangkat. Cocok kalau link diblokir.
- Hasilnya urut dari skor tertinggi. Ketuk satu klip untuk menonton, geser Mulai dan Selesai, pilih subtitle dan format, lalu Buat klip dan Unduh klip.

## Penilaian viral

Tanpa kunci, skor dihitung dari pembuka kalimat, kata emosional, angka, tempo bicara, jeda, energi suara, dan apakah klip utuh. Dengan kunci Gemini gratis dari aistudio.google.com/apikey (tempel di Pengaturan), 12 klip teratas dinilai ulang oleh AI dan judulnya dibuat lebih menarik. Skor hanya perkiraan.

## Batas yang perlu diketahui

- Video lebih dari 90 menit ditolak. Ubah lewat variabel `MAX_MINUTES`.
- Hasil dan file sementara dihapus setelah 3 jam atau saat aplikasi dimatikan.
- Pakai hanya untuk video milik sendiri atau yang kamu punya izinnya.
