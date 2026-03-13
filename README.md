# URBAN FARMER ECOSYSTEM v2.0 🌿🏙️

**AI-Powered Agri-Tech Suite for Resilient Urban & Rural Farming.**

URBAN FARMER ECOSYSTEM v2.0 is a comprehensive agricultural intelligence platform designed to empower farmers with AI-driven insights, blockchain-backed accountability, and community-driven alerts. From city balconies to large-scale rural farms, this platform optimizes growth and mitigates risks.

---

## 🚀 Vision

To create a "Digital Green Shield" for agriculture by integrating advanced AI, Graph Intelligence, and Blockchain into a seamless, accessible toolkit for modern farmers.

## 🌟 Key Features

### 1. Dual-Engine Plant Identification 📸
- **YOLO Engine**: Local, real-time bounding box detection for quick scans.
- **Gemini Vision PRO**: High-precision botanical identification, invasive species detection, and removal guidance.
- **Invasive Alert System**: Automatically detects "Red Flag" species and triggers community warnings.

### 2. Community Intelligence (Neo4j Graph Database) 🕸️
- **Relationship Mapping**: Connects detections across geographical boundaries.
- **Proximity Alerts**: If a pest or invasive plant is detected, neighbors within 5km receive automated SMS/WhatsApp alerts.
- **Local Trends**: See what your neighbors are planting and what's succeeding in your soil type.

### 3. AI Voice Assistant (hindi-English) ☎️
- **Twilio Integration**: Dial in to talk to our AI assistant.
- **Multimodal Support**: Ask about weather, market prices, or seasonal crop advice in Hindi.
- **Real-time Data**: Integrated with Open-Meteo for hyper-local weather and live market price tracking.

### 4. Immutable Audit Trail (Shardeum Blockchain) ⛓️
- **Farm Verification**: Every farm approval and carbon credit assessment is recorded on the Shardeum blockchain.
- **Transparency**: Creates a permanent, verifiable history for every farm registered on the platform.

### 5. Urban Cooling & Balcony Optimization 🏙️
- **Cooling Impact**: Calculate how your garden reduces urban heat island effects.
- **Space Management**: Specialized models for balcony gardens and vertical farming.

### 6. Crop Recommendations & Gamification 🏆
- **AI Recommendations**: Personalized crop suggestions based on soil, budget, and historical trends.
- **Leaderboards**: Earn points for scanning plants, destroying invasive species, and mapping farms.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend** | FastAPI (Python 3.11+) |
| **Relational DB** | SQLite (Farmer profiles, activity logs) |
| **Graph DB** | Neo4j (Proximity mapping, social alerts) |
| **Blockchain** | Shardeum (Audit records, verification) |
| **Core AI** | Google Gemini 1.5 PRO / Flash |
| **Computer Vision** | YOLOv8 (Local Inference) |
| **Communications** | Twilio (Voice Bot, SMS Alerts) |
| **Frontend** | Jinja2 + Tailwind CSS + Leaflet.js |

---

## ⚡ Quick Start

### 1. Requirements
Ensure you have Python 3.11+, Neo4j Desktop (or Aura), and a Shardeum-compatible wallet.

### 2. Installation
```powershell
# Clone and enter
git clone <repo-url>
cd agriassist

# Run full setup (Windows)
./setup.ps1
```

### 3. Environment Configuration
Create a `.env` file from `.env.example`:
```env
# AI & Core
GEMINI_API_KEY=your_key
SECRET_KEY=your_secret

# Neo4j
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password

# Blockchain (Shardeum)
SHARDEUM_RPC_URL=https://atomium.shardeum.org/
ADMIN_PRIVATE_KEY=your_private_key

# Communications (Twilio)
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_PHONE_NUMBER=your_number
```

### 4. Running the App
```powershell
# Local dev server
./run.ps1
```
The app will be live at `http://localhost:8001`.

---

## 📁 Project Structure

```text
agriassist/
├── app/
│   ├── core/           # DB Config, Neo4j Driver, Security
│   ├── models/         # SQLALchemy & Pydantic Schemas
│   ├── routers/        # API Endpoints (Plants, Voice, Dashboard)
│   ├── services/       # Business Logic (Gemini, Blockchain, Graph)
│   ├── templates/      # Jinja2 Layouts
│   └── main.py         # Entry point
├── scripts/            # Database migrations and seeders
├── uploads/            # Processed plant images
├── requirements.txt    # dependencies
└── README.md           # This file
```

---

## 🛡️ Security & Accountability
- **JWT Authentication** for all farmer sessions.
- **Polygon-based Geofencing** for farm boundary accuracy.
- **Blockchain Verification** to prevent fraudulent carbon credit claims.

---

## 🤝 Support & Contribution
Built for the **hackNO Hackathon**. 
For inquiries, please open an issue or reach out to the development team.

**Built with ❤️ for a Greener, Smarter India.**
