# Database IoT

Proyek ini menggunakan SQLite untuk menyimpan riwayat data sensor suhu dan kelembapan.

## Nama Database
`sensor_iot.db`

## Nama Tabel
`sensor_history`

## Struktur Tabel

| Kolom | Tipe Data | Keterangan |
|---|---|---|
| id | INTEGER | Primary Key, Auto Increment |
| suhu | REAL | Data suhu |
| kelembaban | REAL | Data kelembapan |
| received | TEXT | Waktu data diterima |

## Fitur
- Menyimpan data sensor secara otomatis ke SQLite.
- Menampilkan 50 riwayat sensor terbaru melalui API GET `/api/history`.
- Data tetap tersimpan meskipun Node-RED direstart.
