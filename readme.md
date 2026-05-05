# 🛡️ Unified AI-Powered Cybersecurity Platform (Backend)

This repository contains the **backend implementation** of a Unified AI-Powered Cybersecurity Platform.
The backend acts as the central system connecting detection pipelines and the frontend dashboard.

---

## 🚀 Features

* FastAPI-based backend
* REST API for handling security events
* SQLite database for storing incidents
* Modular architecture (IDPS + Steganography pipelines)
* WebSocket-ready structure for real-time updates
* Clean and scalable project structure

---

## 🧠 System Overview

The backend integrates:

* **Pipeline A (IDPS)** → Detects network-level attacks
* **Pipeline B (Steganalysis)** → Detects hidden data in images/videos
* **Dashboard** → Displays real-time security events

All components communicate through this backend.

---

## 📁 Project Structure

backend/
│── main.py              # Entry point
│── database.py          # Database configuration
│── models.py            # DB models
│── schemas.py           # Data schemas
│── alert_bus.py         # Pub-sub system
│── websocket.py         # WebSocket handling
│
│── routes/
│     ├── idps.py        # IDPS APIs
│     ├── steg.py        # Steganography APIs
│     ├── incidents.py   # Incident APIs
│     ├── **init**.py

---

## ⚙️ Installation & Setup

### 1. Clone Repository

git clone https://github.com/PKgamer1358/UACP_backend.git
cd your-repo-name

---

### 2. Create Virtual Environment

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

---

### 3. Install Dependencies

pip install fastapi uvicorn sqlalchemy

---

### 4. Run Server

uvicorn main:app --reload

Server runs at:
http://127.0.0.1:8000

---

## 📡 API Endpoints

POST /api/idps/event
→ Receive IDPS attack events

POST /api/steg/event
→ Receive steganography detection events

GET /api/incidents
→ Fetch all stored incidents

---

## 📊 API Testing

Open Swagger UI:

http://127.0.0.1:8000/docs

---

## 🗄️ Database

* SQLite database
* Main table: `incidents`
* Stores:

  * Source IP
  * Attack type
  * Pipeline (A/B)
  * Confidence score
  * Severity

---

## 🔌 Future Improvements

* Real-time WebSocket integration
* Correlation engine for attack tracking
* Advanced filtering and analytics
* Frontend dashboard integration
* Authentication and access control

---

## 👨‍💻 Tech Stack

* Python 3.10+
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

---

## 📌 Notes

* Part of a **4-member cybersecurity project**
* Backend acts as the **central communication layer**
* Designed to integrate multiple detection pipelines

---

## 📜 License

Academic use only

---

## ✨ Author

Backend developed as part of a cybersecurity project system.
