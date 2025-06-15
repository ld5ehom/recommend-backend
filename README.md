# Store Recommendations System (Backend)

## Project Overview

-   Utilized: FastAPI, MySQL,

---

## Architecture Diagram:

```
├─ tests/                       # Unit and integration tests
│
├─ Client
│   └─ API Consumer (Browser / Frontend / External Request)
│
├─ API Server (FastAPI + Uvicorn)
│   └─ main.py                  # Entry point for running the FastAPI server using Uvicorn
│
├─ Application Layer (src/)
│   ├─ app.py                   # Creates FastAPI app instance and includes routers
│   ├─ config.py                # Loads settings from .env using Pydantic BaseSettings
│   ├─ openapi_metadata.py      # Defines custom OpenAPI schema metadata for documentation
│   ├─ core/                    # Global configs, error handlers, security settings
│   ├─ dependencies/            # Dependency injection utilities (e.g., DB session)
│   ├─ models/                  # SQLAlchemy or ORM-based DB models
│   ├─ services/                # Business logic and domain services
│   ├─ routers/                 # API endpoints grouped by feature or domain
│   ├─ schemas/                 # Pydantic schemas for request and response validation
│   └─ __init__.py              # Package initializer for src
│
├─ Environment / Configuration
│   ├─ .env                     # Environment variables (e.g., DB URL, secret keys)
│   └─ src/config.py           # Loads configuration values into the app
│
└─ Dependency / Setup
    ├─ requirements.txt         # Python dependency declarations for pip
    └─ venv/                    # Virtual environment directory (should be gitignored)

```

---

## Reference Site

-   [Design System](https://primer.style/components)

---

## Milestones

-   M1 : Project Setup and Basic API Integration
-   M2 : Model Serving and Monitoring Integration
-   M3 : Visualization, Alerts, and Finalization

---

## Task List

### Milestone 1 : Project Setup and Basic API Integration

**Task 1. Project Setup & DB Modeling**

-   **Issues** : [task-1-setup](https://github.com/ld5ehom/recommend-backend/tree/task-1-setup)
-   **Details** :

    -   Initial project setup and model annotation ->
        -   Set up MySQL connection, configured DBeaver access, renamed tables under unified schema, and added structured docstrings and bilingual comments to database models and user schemas.

**Task 2. API Endpoint Implementation**

---

### Milestone 2: Model Serving and Monitoring Integration

**Task 3. Testing and Deployment Pipeline**

**Task 4. ML Model Serving Overview**

**Task 5. ML Model API Integration**

### Milestone 3: Visualization, Alerts, and Finalization

**Task 6. Prometheus Integration**

**Task 7. Grafana Dashboard Setup**

**Task 8. Alerting & Final Alarms**

---

## Setup

-   **Create a virtual environment | 가상환경 생성**

```
python3 -m venv venv
```

-   **Activate the virtual environment (Mac/Linux) | 가상환경 활성화 (Mac/Linux)**

```
source venv/bin/activate
```

-   **Install dependencies from requirements.txt | requirements.txt 기반 의존성 설치**

```
pip install -r requirements.txt
```

---

## Start

-   **Run the main FastAPI development server | 메인 FastAPI 개발 서버 실행**

```
python main.py
```

-   **(Optional) Run the mock server without real DB | (선택) 실제 DB 없이 목서버 실행**

```
python mock_main.py
```
