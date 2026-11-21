"""
Simulasi ESP32 (Publisher + Subscriber) - Praktikum REST API Node-RED
- Publish data sensor (suhu, kelembaban) ke topic iot/sensor tiap 3 detik
- Subscribe topic iot/kontrol untuk menerima perintah dari dashboard (lampu ON/OFF)

Install dependency:
    pip install paho-mqtt
"""
import json
import random
import time
from datetime import datetime

import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC_SENSOR = "iot/sensor"
TOPIC_KONTROL = "iot/kontrol"
INTERVAL = 3  # detik

# Status lampu (disimulasikan sebagai LED di ESP32)
lamp_state = "off"


# ---------- Callback (paho-mqtt v2) ----------
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(f"[OK] Terhubung ke broker {BROKER}:{PORT}")
        client.subscribe(TOPIC_KONTROL)
        print(f"[OK] Subscribe ke topic: {TOPIC_KONTROL}")
    else:
        print(f"[ERROR] Gagal konek, kode: {reason_code}")


def on_message(client, userdata, msg):
    global lamp_state
    try:
        perintah = json.loads(msg.payload.decode())
    except json.JSONDecodeError:
        print(f"[WARN] Pesan bukan JSON di {msg.topic}: {msg.payload}")
        return

    print(f"<- Perintah diterima [{msg.topic}]: {perintah}")

    if perintah.get("device") == "lamp":
        action = perintah.get("action")
        if action in ("on", "off"):
            lamp_state = action
            ikon = "ON " if action == "on" else "OFF"
            print(f"   Lampu sekarang: {ikon}")
        else:
            print(f"   [WARN] action tidak dikenal: {action}")


def on_disconnect(client, userdata, flags, reason_code, properties):
    print(f"[INFO] Terputus dari broker (kode: {reason_code})")


# ---------- Setup client ----------
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="ESP32-Simulator")
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

try:
    client.connect(BROKER, PORT, 60)
except ConnectionRefusedError:
    print("[ERROR] Broker tidak berjalan. Jalankan dulu: mosquitto -v")
    raise SystemExit(1)

client.loop_start()
print("ESP32 Simulator berjalan... Ctrl+C untuk stop")

# ---------- Loop publish sensor ----------
try:
    while True:
        data = {
            "suhu": round(random.uniform(25, 32), 1),
            "kelembaban": round(random.uniform(55, 80), 1),
            "timestamp": datetime.now().isoformat(),
        }
        client.publish(TOPIC_SENSOR, json.dumps(data))
        print(f"-> Publish: {data}")
        time.sleep(INTERVAL)
except KeyboardInterrupt:
    print("\nSimulator dihentikan.")
finally:
    client.loop_stop()
    client.disconnect()