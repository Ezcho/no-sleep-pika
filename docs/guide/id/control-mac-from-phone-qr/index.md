Source: https://no-sleep-pika.online/guide/id/control-mac-from-phone-qr/
Language: id

MAC GUIDE · 2026-11-23

# Kendalikan Mac dengan QR: sesi, timer, dan matikan dari ponsel

pika 1.3.0 memungkinkan ponsel mengatur Session dan daya setelah Anda menyetujui koneksinya di Mac.

## Lebih dari melihat status

Tinggalkan proses build atau unduhan di Mac, lalu atur Session, timer, atau permintaan matikan dan mulai ulang dari ponsel. pika 1.3.0 menambahkan kendali pada halaman status QR.

Ini bukan kendali percakapan AI. Tidak ada instruksi baru untuk agen, keluaran terminal, persentase kemajuan pekerjaan, atau tampilan layar Mac.

## Perbarui aplikasi Mac dahulu

Jalankan pika 1.3.0 atau lebih baru di Mac. Pencegahan tidur saat tutup tertutup memerlukan layanan pembantu yang bekerja. Kedua perangkat memerlukan internet.

Jika pengembang tidak dapat diverifikasi, pastikan berkas berasal dari situs resmi. Setelah mencoba membukanya, buka System Settings → Privacy & Security → Open Anyway untuk berkas itu, lalu ikuti konfirmasi macOS. Nama dapat berbeda; lihat panduan instalasi di bawah. Jangan menonaktifkan seluruh perlindungan.

Peringatan malware atau berkas rusak adalah masalah berbeda; jangan gunakan pengecualian membuka ini untuk peringatan tersebut.

[Unduh pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [Bantuan instalasi](https://no-sleep-pika.online/install/)

## Pindai lalu izinkan di Mac

Minta QR pika dalam percakapan AI yang sudah terhubung ke pika MCP. Pindai dengan kamera ponsel dalam lima menit. QR sekali pakai; awalnya hanya memberi akses baca dan tidak menyalakan Session.

Minta kendali dari ponsel, lalu setujui dialog di Mac. Selesaikan saat kedua perangkat masih di depan Anda. Tanpa persetujuan Mac, kendali tidak tersedia.

Tombol ponsel saat ini berbahasa Korea: “이 Mac에 연결” untuk terhubung, lalu “Mac에 제어 허용 요청” untuk meminta kendali, kemudian izinkan di Mac. “예약·카운트다운 취소” membatalkan timer. Untuk MCP pertama kali, ikuti panduan di bawah.

[Panduan koneksi MCP →](https://no-sleep-pika.online/id/#mcp)

## Yang bisa dikendalikan

Session menyalakan atau melepas pencegahan tidur. Monitor hanya dapat diubah saat Session ON; kebijakan layar mode tutup tertutup diterapkan setelah tutup ditutup. Nilai Monitor adalah pengaturan yang diminta, bukan bukti keadaan layar fisik.

Pilih hanya saat daya tersambung, lepas Session saat pengisi daya dicabut, atau pada baterai 30/40/50%. Perlindungan baterai dan panas tetap berlaku. Panas adalah tingkat macOS, bukan suhu °C.

## Timer dan waktu pembatalan 60 detik

Pilih 15, 30, 60, 180, atau 360 menit untuk melepas Session, tidur, mematikan, atau memulai ulang. Melepas Session tidak menutup paksa aplikasi.

Permintaan matikan atau mulai ulang langsung memerlukan konfirmasi, lalu hitung mundur 60 detik yang dapat dibatalkan. pika memulihkan pengaturan tidur dahulu. Dialog dokumen belum tersimpan dapat menunda atau membatalkan tindakan; terkirim tidak berarti selesai.

## Izin berakhir bersama koneksi

Izin berlaku untuk koneksi yang sedang disetujui. Putus koneksi atau cabut izin membatalkan timer jarak jauh dan hitung mundur; sambungan baru perlu persetujuan baru. Akses maksimal 24 jam sejak QR diterbitkan. Timer tidak berjalan terus setelah pika keluar atau Mac tidur.

Putus koneksi dapat memerlukan puluhan detik untuk terdeteksi. Untuk mencegah Mac mati, tekan “예약·카운트다운 취소” dan pastikan status batal, bukan sekadar memutus koneksi. Timer jarak jauh memerlukan sinyal koneksi browser berkelanjutan; memindahkan browser ke latar belakang dapat memutus koneksi dan membatalkan timer.

Jangan bagikan QR. Uji perubahan Session dan pembatalan timer dengan pekerjaan yang tidak penting dahulu. Status lama saat terputus bukan bukti Mac mati. Jaringan dan penyelesaian tugas AI tidak dijamin.

Sumber dan cakupan

Ditulis pembuat no-sleep-pika pada 23 November 2026 untuk aplikasi sendiri, versi 1.3.0. Periksa juga panduan resmi Apple untuk peringatan instalasi.

- [pika 1.3.0 · Release notes](https://github.com/Ezcho/no-sleep-pika/releases/tag/v1.3.0)

- [pika · Remote connection and permissions](https://github.com/Ezcho/no-sleep-pika/blob/v1.3.0/Remote/README.md)

- [Apple · Safely open apps on your Mac](https://support.apple.com/en-us/102445)

Ditulis oleh pembuat no-sleep-pika; mencakup aplikasi kami.

[Unduh pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg)[Cara menjaga Mac tetap aktif: clamshell, caffeinate, dan pika →](https://no-sleep-pika.online/guide/id/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/id/control-mac-from-phone-qr/index.md)
