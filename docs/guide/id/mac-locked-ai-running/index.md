Source: https://no-sleep-pika.online/guide/id/mac-locked-ai-running/
Language: id

MAC GUIDE · 2026-10-05

# Mac terkunci: apakah Claude Code dan Codex tetap bekerja?

Bedakan layar terkunci, layar mati, dan tidur sistem saat memeriksa pekerjaan AI lokal.

## Kunci layar dan tidur

Layar kata sandi bukan bukti pekerjaan berhenti. Perintah latar dapat berjalan jika Mac tetap terjaga, aplikasi terbuka, dan koneksi tersedia. Otomasi tampilan atau autentikasi mungkin perlu membuka kunci. Sistem juga bisa tidur setelah layar terkunci. Pertahankan perlindungan kata sandi.

## Lokal atau cloud

Codex CLI memakai berkas dan perintah lokal; pekerjaan Codex Cloud berjalan di lingkungan terpisah. Claude Code Remote Control tetap terhubung ke sesi lokal. Tersambung kembali bukan berarti pekerjaan berjalan selama tidur. pika tidak memindahkan pekerjaan ke cloud.

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Codex Cloud](https://learn.chatgpt.com/docs/cloud) · [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

## Periksa penyebabnya

Baca pesan terakhir: persetujuan, pertanyaan, selesai, atau kesalahan. Lalu periksa aplikasi, Wi-Fi, VPN, dan login. Perintah baca-saja di bawah menunjukkan permintaan daya dan kejadian, bukan kemajuan AI. CPU rendah juga bukan bukti kegagalan.

```
pmset -g assertions
```

```
pmset -g log | tail -n 60
```

## Uji tiga menit

Jalankan loop dengan penutup terbuka, biarkan terminal terbuka, lalu kunci sekitar tiga menit. Bandingkan waktu dan hentikan dengan Ctrl+C. Cocokkan jeda dengan log daya serta hasil AI. Ini hanya menguji proses sederhana; uji penutup tertutup secara terpisah.

```
while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done
```

## Pengaturan pika

Pasang pika dan layanan pendamping, aktifkan Session, pilih Monitor OFF bila layar tidak diperlukan, lalu tutup penutup. Kebijakan layar berlaku setelah penutup ditutup. Session OFF melepas pencegahan tidur tanpa langsung mematikan layar. Gunakan daya dan meja berventilasi, bukan tas tertutup. Perlindungan atau gangguan layanan dapat menghentikan sesi.

[Unduh pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Bantuan instalasi](https://no-sleep-pika.online/install/)

## Pertanyaan umum

Monitor OFF bukan perintah menghentikan AI. tmux tidak mencegah tidur; caffeinate tidak mengatasi jaringan atau persetujuan. Status pika MCP bukan kemajuan semua pekerjaan AI.

Sumber dan cakupan

Dokumentasi resmi dan implementasi diperiksa 5 Oktober 2026. Panduan dari pembuat pika, tanpa jaminan operasi tanpa putus pada semua perangkat.

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [OpenAI · Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

- [OpenAI · Codex Cloud](https://learn.chatgpt.com/docs/cloud)

- [Anthropic · Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

Ditulis oleh pembuat no-sleep-pika; mencakup aplikasi kami.

[Unduh pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Cara menjaga Mac tetap aktif: clamshell, caffeinate, dan pika →](https://no-sleep-pika.online/guide/id/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/id/mac-locked-ai-running/index.md)
