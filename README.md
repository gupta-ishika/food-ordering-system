# 🍽️ QR Code Food Ordering System

A full-stack food ordering application where customers can scan a QR code placed on a restaurant table, browse the digital menu, place orders, and track their order status in real time.

This project is being built from scratch following industry-standard software development practices.

---

## 🚀 Features (Planned)

### 👨‍🍳 Customer
- Scan QR code to access the menu
- Browse food categories
- Search and filter menu items
- Add items to cart
- Place orders
- Track order status

### 🏪 Restaurant Admin
- Secure authentication
- Manage menu categories
- Add, edit, and delete food items
- Upload food images
- Manage tables and QR codes
- View and manage orders
- Analytics dashboard

### 👨‍🍳 Kitchen
- View incoming orders
- Update order status
- Real-time order management

---

## 🛠️ Tech Stack

### Frontend
- React
- Vite
- Tailwind CSS

### Backend
- FastAPI
- SQLAlchemy

### Database
- PostgreSQL (Docker)

### Database Client
- DBeaver

### Tools
- Docker & Docker Compose
- Git & GitHub

---

## 📁 Project Structure

```text
food-ordering-system/
│
├── backend/
│   ├── alembic/
│   │   └── versions/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── database.py
│   │   ├── enums/
│   │   │   ├── __init__.py
│   │   │   └── order_status.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── restaurant.py
│   │   │   ├── category.py
│   │   │   ├── food_item.py
│   │   │   ├── table.py
│   │   │   ├── order.py
│   │   │   └── order_item.py
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── alembic.ini
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── context/
│   │   ├── hooks/
│   │   ├── layouts/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── styles/
│   │   └── utils/
│   │
│   └── package.json
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Start PostgreSQL

```bash
docker compose up -d
```

### 3. Start the backend

```bash
cd backend

# Activate virtual environment
venv\Scripts\activate      # Windows
# source venv/bin/activate # macOS/Linux

uvicorn app.main:app --reload
```

### 4. Start the frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🌐 Application URLs

Frontend:

```
http://localhost:5173
```

Backend:

```
http://127.0.0.1:8000
```

Swagger API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📌 Current Status

**Phase 1 – Project Planning & Setup** ✅

Completed:
- Git repository setup
- FastAPI backend setup
- React + Vite frontend setup
- Tailwind CSS configuration
- Frontend ↔ Backend communication
- PostgreSQL with Docker
- SQLAlchemy database connection

**Phase 2 – Database Design** ✅

Completed:
- SQLAlchemy models: Restaurant, Category, FoodItem, Table, Order, OrderItem
- Enum: OrderStatus (Received, Preparing, Ready, Served, Cancelled)
- DeclarativeBase setup with relationship mappings

**Phase 2.5 – Database Setup & Migration** ✅

Completed:
- Alembic installed and configured (`alembic.ini` & `env.py`)
- Initial database migration created (`initial_schema`)
- PostgreSQL schema populated and managed with Alembic

---

## 📅 Roadmap

- [x] Phase 1 – Project Planning & Setup
- [x] Phase 2 – Database Design
- [x] Phase 2.5 – Database Setup & Migration
- [ ] Phase 3 – Authentication
- [ ] Phase 4 – Restaurant Dashboard
- [ ] Phase 5 – QR Code & Table Management
- [ ] Phase 6 – Customer Menu
- [ ] Phase 7 – Shopping Cart
- [ ] Phase 8 – Order Management
- [ ] Phase 9 – Kitchen Dashboard
- [ ] Phase 10 – Order Tracking
- [ ] Phase 11 – Analytics
- [ ] Phase 12 – Deployment

---

## 👩‍💻 Author

**Ishika Gupta**

Built as a learning project to gain hands-on experience in full-stack web development using React, FastAPI, PostgreSQL, Docker, and modern development practices.