# IoT REST API Node-RED

Proyek Internet of Things (IoT) untuk memantau suhu dan kelembapan menggunakan simulasi ESP32, MQTT, Node-RED, REST API, WebSocket, dan SQLite.

## Teknologi
- Python
- MQTT Mosquitto
- Node-RED
- HTML, CSS, JavaScript
- Chart.js
- WebSocket
- SQLite

## Fitur Utama
- Monitoring suhu dan kelembapan secara real-time.
- Kontrol perangkat melalui REST API.
- Menampilkan riwayat data sensor.
- Grafik suhu dan kelembapan.
- Notifikasi ketika suhu melewati batas yang ditentukan.
- Autentikasi API menggunakan API Key.
- Pembaruan data menggunakan WebSocket.
- Penyimpanan riwayat sensor menggunakan SQLite.

## Endpoint REST API

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | `/api/suhu` | Mengambil data sensor terbaru |
| GET | `/api/history` | Mengambil riwayat sensor |
| GET | `/api/threshold` | Mengambil batas suhu |
| PUT | `/api/threshold` | Mengubah batas suhu |
| POST | `/api/kontrol` | Mengirim perintah kontrol |

## MQTT Topic
- `iot/sensor` — data sensor.
- `iot/kontrol` — perintah kontrol perangkat.

## Autentikasi
API menggunakan header:

`X-API-Key`

Ganti API Key contoh dengan nilai milik sendiri pada konfigurasi Node-RED dan dashboard. Jangan publikasikan API Key pribadi di repository.

## Struktur Repository

```text
iot-rest-api-node-red/
├── README.md
├── dashboard.html
├── simulasi_esp32.py
├── node-red/
│   └── flow.json
├── database/
│   └── README.md
```

## Cara Menjalankan
1. Jalankan Mosquitto MQTT Broker.
2. Jalankan Node-RED.
3. Import `node-red/flow.json` ke Node-RED.
4. Sesuaikan konfigurasi database SQLite.
5. Jalankan simulasi ESP32 menggunakan Python.
6. Buka dashboard melalui Live Server.

## Pengembangan Tambahan
1. API pengaturan threshold.
2. Grafik real-time menggunakan Chart.js.
3. Autentikasi API Key.
4. Pembaruan data menggunakan WebSocket.
5. Penyimpanan riwayat menggunakan SQLite.
