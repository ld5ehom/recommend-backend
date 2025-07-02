# Store Management and Recommendation System (Backend)

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

-   [FastAPI](https://fastapi.tiangolo.com/)
-   [SQLAlchemy](https://docs.sqlalchemy.org/)
-   [MySQL](https://dev.mysql.com/doc/)
-   [Pydantic](https://docs.pydantic.dev/)
-   [Design System](https://primer.style/components)

---

## Milestones

-   M1 : Project Setup and Basic API Integration
-   M2 : Deployment & ML Model Integration
-   M3 : Visualization, Alerts, and Finalization

---

## Task List

### Milestone 1 : Project Setup and Basic API Integration

**Task 1. Project Setup & DB Modeling**

-   **Issues** : [task-1-setup](https://github.com/ld5ehom/store-backend/tree/task-1-setup)
-   **Details** :

    -   Initial project setup and model annotation -> [ae8b533](https://github.com/ld5ehom/store-backend/commit/ae8b533174bc9add5e90ed29bd6b7775a8c655d0)
        -   Set up MySQL connection and verified access through DBeaver. Defined initial SQLAlchemy models and schemas for core user and restaurant-related entities. Added structured docstrings for maintainability and consistency across database models.

**Task 2. API Endpoint Implementation**

-   **Issues** : [task-2-api](https://github.com/ld5ehom/store-backend/tree/task-2-api)
-   **Details** :
    -   Add user login and signup with JWT auth -> [3af69a6](https://github.com/ld5ehom/store-backend/commit/3af69a65c7a8dc253867fe80bec3ff878b8e9844)
        -   Implemented user authentication system including signup and login endpoints, JWT-based access token issuance, password hashing, and database integration using FastAPI and SQLAlchemy.
    -   Implemented user-related features -> [8fa702e](https://github.com/ld5ehom/store-backend/commit/8fa702e35cb88206bea60a76cd2ad556d44b7a13)
        -   Developed user-related endpoints and services including profile update, follow/unfollow, and user lookup using FastAPI with OAuth2 authentication and SQLAlchemy, along with modular router/service integration and test-ready batch user creation.
    -   Article Feature Implementation -> [461184f](https://github.com/ld5ehom/store-backend/commit/461184f91436bdadd27688e333bffac10f0b4a47)
        -   Implemented core article features including listing with pagination and sorting options, and fetching individual articles by ID, using FastAPI routing, SQLAlchemy queries, and modular service-router architecture for maintainability.
    -   Implement restaurant feature: schema, model, and relationship mappings -> [020c9e4](https://github.com/ld5ehom/store-backend/commit/020c9e4b0a5c3e1a2b3c4f63aa237d8a42e3b42f)
        -   Developed core restaurant functionalities including full schema definitions for restaurant creation, update, and search. Implemented SQLAlchemy models for Restaurant, Tag, Keyword, CuisineType, and their respective category models (TagCategory, CuisineTypeCategory).
        -   Established many-to-many mappings such as RestaurantTag, RestaurantKeyword, and RestaurantCuisineType.
        -   Added blog review and review models with schema integration.
        -   Ensured complete bidirectional relationships across models and Pydantic schemas to support FastAPI routing, dependency injection, and modular querying.

---

### Milestone 2: Deployment & ML Model Integration

**Task 3. Testing and Deployment Pipeline**

-   **Issues** : [task-3-test](https://github.com/ld5ehom/store-backend/tree/task-3-test)
-   **Details** :
    -   **Add article retrieval test cases**
        -   Implemented test_read_article and test_read_nonexistent_article using FastAPI TestClient to verify successful retrieval of a specific article and proper 404 handling for non-existent articles.

**Task 4. ML Model API Integration**

### Milestone 3: Visualization, Alerts, and Finalization

**Task 5. Prometheus Integration**

**Task 6. Grafana Dashboard Setup**

**Task 7. Alerting & Final Alarms**

---

## Setup

-   **Create a virtual environment | 가상환경 생성**

```
python3 -m venv venv
```

-   **Activate the virtual environment (Mac/Linux) | 가상환경 활성화 (Mac/Linux)**

```
source .venv/bin/activate
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

## Test

```
PYTHONPATH=. pytest
```

## Docker

```
docker login
```

```
docker compose up -d --build
```

```
docker compose down
```
