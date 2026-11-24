Source: https://no-sleep-pika.online/guide/id/parallel-ai-agents-git-worktree/
Language: id

MAC GUIDE · 2026-11-24

# Dua agen AI mengedit berkas yang sama? Pisahkan foldernya dulu.

Git worktree memberi setiap agen folder kerja sendiri. Bagi tugas, tinjau perubahan, lalu gabungkan hasil tanpa mencampur pekerjaan yang belum selesai.

## Masalah satu folder bersama

Satu agen mengubah antarmuka, yang lain menulis pengujian. Jika memakai folder yang sama, keduanya membaca dan mengubah berkas yang sama. Dua nama branch tidak membuat dua salinan berkas di folder itu. Berpindah branch juga mengubah berkas yang sedang dipakai agen lain.

Git worktree menambahkan folder kerja ke repositori yang sama. Setiap folder dapat memiliki branch dan berkasnya sendiri sambil berbagi riwayat. Ini memisahkan pekerjaan yang berlangsung, tetapi tidak menjamin hasil akhirnya bebas konflik.

- 1 Pisahkan folder

- 2 Bagi tugas

- 3 Tinjau perubahan

- 4 Gabungkan bergiliran

## Siapkan titik awal yang sudah ditinjau

Jalankan perintah berikut di proyek Git yang sudah ada. Harus ada setidaknya satu commit; HEAD menjadi titik awal yang tersimpan. Keluaran kosong berarti tidak ada perubahan atau berkas tak terlacak yang dilaporkan. Berkas yang diabaikan masih mungkin ada.

Jika muncul daftar, periksa dahulu. Commit hanya perubahan yang memang diperlukan atau pilih commit yang sudah ada. Jangan menambahkan seluruh folder tanpa memeriksa rahasia dan pekerjaan lain. Folder baru dimulai dari HEAD, bukan dari perubahan yang belum di-commit.

```
git status --short
```

## Buat dua folder kerja

Jalankan kedua perintah dari proyek asli. Perintah ini membuat branch ai-ui dan ai-tests serta folder di sebelah proyek. Gunakan nama branch dan jalur yang belum dipakai; pilih nama lain jika sudah ada, bukan menimpa paksa.

Dependensi terpasang, .env yang diabaikan, dan pengaturan lokal tidak semuanya disalin otomatis. Siapkan sesuai petunjuk proyek, berikan hanya kredensial yang diperlukan, dan gunakan port berbeda untuk server bersamaan. Worktree bukan sandbox keamanan: alat yang memiliki izin tetap bisa mengakses folder lain.

```
git worktree add -b ai-ui ../project-ai-ui HEAD
git worktree add -b ai-tests ../project-ai-tests HEAD
```

## Tentukan folder dan lingkup tugas

Buka satu agen di project-ai-ui dan satu di project-ai-tests. Berikan jalur absolut dan tugas terbatas, misalnya “ubah hanya komponen antarmuka” dan “tambahkan pengujian perilaku saat ini tanpa mengubah kode aplikasi”.

Tentukan penanggung jawab berkas bersama, seperti daftar dependensi dan lockfile. Jika keduanya perlu mengedit berkas yang sama, kerjakan bergiliran. Minta laporan berkas yang diubah, pemeriksaan yang dilakukan, dan pekerjaan tersisa.

## Tinjau dan gabungkan satu per satu

Jalankan tiga perintah berikut di setiap folder. Status menampilkan perubahan dan berkas tak terlacak. Diff menampilkan perubahan berkas terlacak yang belum di-stage; diff --cached menampilkan yang sudah di-stage. Berkas baru tak terlacak tidak muncul di diff ini: buka dan periksa terpisah.

Jalankan pemeriksaan proyek, lalu commit perubahan yang disetujui pada branch masing-masing. Kembali ke proyek asli untuk meninjau dan menggabungkan satu branch setiap kali ke branch tujuan. Worktree tidak menggabungkan hasil otomatis. Selesaikan konflik dan periksa hasil gabungan sebelum melanjutkan.

```
git status --short
git diff
git diff --cached
```

## Peran pika

pika membantu Mac tetap terjaga selama pekerjaan lokal sesuai pengaturan sesi dan perlindungannya. pika tidak membagi tugas, menggabungkan branch, atau menyelesaikan konflik. QR pika 1.3 menunjukkan status Mac dan kontrol daya yang diizinkan, bukan keluaran AI atau persentase selesai yang andal. Nilai penyelesaian dari hasil agen dan pemeriksaan proyek.

[Unduh pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [Bantuan instalasi](https://no-sleep-pika.online/install/)

Sumber dan batas pembahasan

Panduan pembuat no-sleep-pika ini berdasarkan dokumentasi resmi Git. Pembahasan memakai agen umum tanpa mengasumsikan fitur atau izin produk tertentu. Ikuti juga aturan kontribusi proyek dan penanganan rahasia.

- [Git · git-worktree](https://git-scm.com/docs/git-worktree)

- [Git · git-status](https://git-scm.com/docs/git-status)

- [Git · git-diff](https://git-scm.com/docs/git-diff)

Ditulis oleh pembuat no-sleep-pika; mencakup aplikasi kami.

[Cara menjaga Mac tetap aktif: clamshell, caffeinate, dan pika →](https://no-sleep-pika.online/guide/id/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/id/parallel-ai-agents-git-worktree/index.md)
