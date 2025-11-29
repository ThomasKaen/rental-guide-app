📘 Rental Guide App

A modern digital guest-guide system for company flats, built with FastAPI & React.

The Rental Guide App provides guests with a clean, mobile-friendly digital guidebook containing everything they need for their stay — property details, check-in instructions, Wi-Fi codes, appliance guides, local recommendations, emergency contacts, and more.

Originally built for internal company use, the system is designed to be extendable into a full multi-property SaaS product if needed.

🚀 Features (Current & Planned)
✅ Phase 1 (MVP)

Public guest guide page (mobile-first)

Property info sections:
Welcome • Check-in • Check-out • House rules • WiFi • Appliances • Local area

Simple templating or React frontend

Static content stored in DB/JSON

One guide per flat (single-property mode)

🔄 Phase 2–3 (In development)

Admin dashboard for editing content

Multi-property support

Image & media uploads

Unique guest/booking links (per stay)

Auto-generated QR codes

Templates for common sections (house rules, emergency info)

🔮 Future (Optional Productisation)

Multi-tenant (multiple companies/accounts)

Analytics dashboard

Email/SMS automation

Cloud SQL integration

Branded subdomains or custom domains

Paid commercial usage (Prosperity License)

🏗️ Tech Stack

Backend

FastAPI

Pydantic

SQLAlchemy

SQLite (dev) → PostgreSQL (prod)

Docker

Frontend

React + Vite (planned)

OR Jinja templates (for early MVP)

Infrastructure

Docker Compose

Nginx (reverse proxy)

Deployable on Google Cloud (VM or Cloud Run)

📂 Project Structure
rental-guide-app/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── templates/   ← optional (Jinja guest pages)
│   │   ├── static/      ← images/css if not using React
│   │   └── main.py
│   ├── tests/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── alembic/         ← DB migrations (future)
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── Dockerfile
│
├── infra/
│   ├── docker-compose.yml
│   ├── nginx/
│   └── scripts/
│
├── LICENSE
└── README.md

🔧 Development Setup
1. Clone the repository
git clone git@github.com:ThomasKaen/rental-guide-app.git
cd rental-guide-app

2. Start backend in dev mode
cd backend
uvicorn app.main:app --reload

3. (Optional) Start frontend
cd frontend
npm install
npm run dev

4. Docker (recommended)
docker-compose up --build

📝 License

This project is licensed under the Prosperity Public License 3.0.0.
This means:

Free for personal and non-commercial use

Commercial use requires a paid license

See LICENSE for full terms.

👤 Author

Tamas Kiss
Prosperity License Holder
Contact for commercial licensing:
📧 your-email-here

⭐ Roadmap Snapshot

 Phase 0 — Scope + folder structure

 Phase 1 — Single-property MVP

 Phase 2 — Admin UI

 Phase 3 — Guest links + booking tokens

 Phase 4 — Media + interactive maps

 Phase 5 — Automation + analytics

 Phase 6 — Multi-tenant + SaaS mode