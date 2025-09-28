# STC Connect 🌀

STC Connect adalah gateway API untuk menghubungkan aplikasi, IoT device, dan sistem blockchain dalam ekosistem SmartTourismChain (STC).
Dengan STC Connect, developer bisa dengan mudah melakukan login, booking, logging IoT events, cek transaksi blockchain, verifikasi booking, hingga realtime analytics.

[![SWH](https://img.shields.io/badge/archived%20at-Software%20Heritage-orange)](https://archive.softwareheritage.org/browse/directory/824f9ed66775c2764adb15796448bc4994e3982b/?origin_url=https://doi.org/10.5281/zenodo.17216998&path=mrbrightsides-stc-iot-connect-39c932e&release=2&snapshot=f6bdb64ab13314f50b0a3b3211d1c9fdeeddc280)
[![OpenAIRE](https://img.shields.io/badge/indexed%20by-OpenAIRE-blue)](https://explore.openaire.eu/search/result?pid=10.5281%2Fzenodo.17217000)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17217000.svg)](https://doi.org/10.5281/zenodo.17217000)

---

## ✨ Features

🔑 Authentication → Login dan dapatkan token JWT.

🏨 Booking Management → Create, verify, dan track booking.

📟 IoT Device Logging → Catat event dari device langsung ke sistem.

🔗 Blockchain Integration → Cek transaksi dengan tx_hash.

📊 Realtime Analytics → Ambil data analitik STC untuk dashboard.

📜 Smart Contract Functions → Panggil fungsi smart contract langsung via API.

---

## 📂 Endpoints
| Method | Endpoint                 | Deskripsi                       |
| ------ | ------------------------ | ------------------------------- |
| POST   | `/auth/login`            | Login user, generate token JWT  |
| POST   | `/booking/create`        | Buat booking baru               |
| GET    | `/booking/verify`        | Verifikasi status booking       |
| POST   | `/device/log`            | Simpan event IoT device         |
| GET    | `/transaction/{tx_hash}` | Cek detail transaksi blockchain |
| GET    | `/analytics/realtime`    | Ambil data realtime analytics   |
| POST   | `/contract/call`         | Panggil fungsi smart contract   |

---

## 🔧 Setup
1. Clone Repository
```bash
git clone https://github.com/elpeef/stc-connect.git
cd stc-connect
```

2. Install Dependencies
```bash
npm install
# atau
pip install -r requirements.txt
```
3. Jalankan Server
```bash
npm start
# atau
python app.py
```

API akan jalan di:
👉 http://localhost:5000/api (default)

---

## 🚀 Quickstart (Postman)

1. Import Postman Collection:

- STC Connect API.postman_collection.json

2. Import Environment:

- STC Connect Env.postman_environment.json

3. Ubah base_url ke:

```arduino
https://stc-connect.streamlit.app/api
```

4. Jalankan request **Auth - Login** → simpan token.

5. Gunakan token untuk request lainnya (Booking, Transaction, dsb).

---

## 📜 License

MIT License © 2025 ELPEEF
