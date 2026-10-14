Source: https://no-sleep-pika.online/guide/id/macbook-downloads-stop/
Language: id

MAC GUIDE · 2026-10-15

# Unduhan MacBook berhenti: layar mati, tidur, atau penutup?

Periksa jaringan dan penyimpanan sebelum memakai caffeinate atau pika.

## Kapan berhenti

Periksa jeda, kesalahan jaringan, ruang kosong, dan login aplikasi. Jika gagal saat digunakan, cek Wi-Fi, VPN, dan server. Pencegahan tidur tidak memperbaiki tautan kedaluwarsa.

## Layar dan tidur

Layar mati tidak berarti sistem tidur. Transfer bisa berlanjut, tetapi tidur otomatis dapat menyusul penguncian. Periksa opsi tetap terjaga saat tersambung daya jika tersedia. Tetap gunakan kata sandi.

## caffeinate dengan penutup terbuka

Perintah berikut meminta pencegahan tidur karena tidak aktif selama satu jam. Biarkan terminal terbuka dan unduh melalui aplikasi biasa. Ctrl+C mengakhiri lebih awal; -t dalam detik, -i untuk sistem, -d untuk layar. Ini tidak menjamin jaringan atau mencegah semua keadaan tidur.

```
caffeinate -i -t 3600
```

```
man caffeinate
```

## Syarat menutup penutup

Dengan monitor eksternal, periksa daya, keyboard, mouse, dan dukungan model. Pengisi daya saja belum cukup. Tanpa monitor, uji transfer singkat dan bandingkan jumlah byte sebelum dan setelah menutup.

## Mengunduh dengan pika

Siapkan pika dan layanan pendamping, mulai unduhan, aktifkan Session, pilih Monitor OFF jika layar tidak diperlukan, lalu tutup. Kebijakan layar berlaku setelah penutup ditutup. Akhiri dengan Session OFF. Gunakan daya dan meja berventilasi, bukan tas tertutup. Perlindungan atau gangguan dapat menghentikan sesi.

[Unduh pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Bantuan instalasi](https://no-sleep-pika.online/install/)

## Periksa hasil

Periksa status selesai, ukuran, dan checksum jika disediakan. Lanjutkan lewat fitur aplikasi. pika tidak memulihkan jaringan atau mendeteksi selesai; mematikan layar tidak menjamin lebih cepat.

Sumber

Diperiksa 11 Oktober 2026 berdasarkan Apple, caffeinate(8), dan kode pika. Panduan pembuat pika.

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [Apple · External displays](https://support.apple.com/en-us/102501)

- `man caffeinate` · macOS System Manager’s Manual

[Jika AI bekerja semalaman, siapa membayar listriknya? →](https://no-sleep-pika.online/guide/id/ai-overnight-electricity-cost/)

Ditulis oleh pembuat no-sleep-pika; mencakup aplikasi kami.

[Unduh pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Cara menjaga Mac tetap aktif: clamshell, caffeinate, dan pika →](https://no-sleep-pika.online/guide/id/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/id/macbook-downloads-stop/index.md)
