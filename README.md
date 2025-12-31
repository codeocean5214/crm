# COSMOS – CRM Backend System

COSMOS is a modular, production-ready **CRM backend** designed with scalability, performance, and clean architecture in mind. It provides core CRM capabilities through well-defined services and follows industry-standard backend engineering practices.

The system is built using **Python** and **FastAPI**, supports **JWT-based authentication**, uses **PostgreSQL (Neon DB)** as the primary database, **SQLite** for local/dev use, **Redis** for caching, and is fully **containerized using Docker**.

---

## 🚀 Features

* Modular CRM backend with clear service boundaries
* High-performance async APIs using FastAPI
* Secure authentication using JWT
* Database abstraction using Repository pattern
* Redis-based caching for optimized reads
* Dockerized setup for consistent deployments
* Clean separation of concerns (Controllers, Services, Repositories)

---

## 🧱 Core Services

COSMOS consists of **4 independent CRM services**:

1. **Customer Service**

   * Create and manage customers
   * Customer profile and metadata handling

2. **Lead Service**

   * Lead creation and tracking
   * Lead lifecycle management

3. **Task Service**

   * Task creation and assignment
   * Follow-ups and task status tracking

4. **Deal Service**

   * Deal pipeline management
   * Deal stages and revenue tracking

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Framework:** FastAPI
* **Primary Database:** PostgreSQL (Neon DB)
* **Secondary Database:** SQLite (local/dev)
* **Caching:** Redis
* **Authentication:** JWT (Admin & User)
* **Logging:** Structured application logging
* **Containerization:** Docker & Docker Compose

---

## 🗂️ Project Architecture

The project follows a **layered architecture** for maintainability and scalability:

```
COSMOS/
│── app/
│   ├── api/            # Route definitions
│   ├── services/       # Business logic layer
│   ├── repositories/   # Database access layer
│   ├── models/         # ORM / schema models
│   ├── schemas/        # Pydantic request/response schemas
│   ├── auth/           # JWT authentication & security
│   ├── cache/          # Redis cache logic
│   ├── core/           # Config, settings, utilities
│   └── main.py         # Application entry point
│
│── docker/
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── README.md
```

---

## 🔐 Authentication & Authorization

* Secure **JWT-based authentication** for both **Admin** and **User** roles
* Separate login flows for Admin and User accounts
* Role-based route protection using FastAPI dependencies
* Secure password hashing and token validation
* Access & refresh token mechanism implemented
* Sensitive parameters handled via environment variables and secure configs

---

## ⚡ Caching Strategy (Redis)

* Frequently accessed data cached in Redis
* Role-aware caching (Admin/User scoped data)
* Reduces database load significantly
* Improves response time for read-heavy endpoints

---

## 🐳 Docker & Containerization

* Application fully containerized using Docker
* Redis runs as a separate service
* PostgreSQL handled via Neon DB (external managed DB)
* Secure environment variable injection at runtime
* Easy local setup and consistent runtime environment

### Run with Docker

```bash
docker-compose up --build
```

---

## 📦 Environment Variables

Create a `.env` file and configure the following:

```env
DATABASE_URL=postgresql://<user>:<password>@<host>/<db>
JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
REDIS_URL=redis://redis:6379
```

---

## 🧪 Development Notes

* SQLite can be used for lightweight local testing
* PostgreSQL (Neon) recommended for staging/production
* Redis is optional but strongly recommended for performance
* Logging enabled across services for debugging and monitoring

---

## 🎯 Project Goal

COSMOS was built as a **backend-first CRM product** focusing on:

* Clean architecture
* Scalability
* Performance
* Real-world backend engineering practices

---

## 📌 Future Enhancements

* Role-based access control (RBAC)
* Background tasks with Celery
* WebSocket-based real-time updates
* API rate limiting
* Advanced analytics & reporting

---

## 👤 Author

**Aditya Mishra**
Backend Engineer | FastAPI | Databases | System Design

---

## ⭐ If you find this project useful

Consider starring the repository and sharing feedback.
