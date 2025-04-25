# toweroffantasy.api

A RESTful API that provides data related to the game **Tower of Fantasy**, such as simulacra, weapons, matrices, events, and more. The goal is to centralize and serve updated information in a structured and accessible way.

[**Tower of Fantasy**](https://tof.perfectworld.com/en-us/index.html) is a free-to-play open-world action RPG developed by Hotta Studio and published by Level Infinite. Set in a futuristic sci-fi universe filled with exploration, fast-paced combat, and a gacha system for acquiring characters and weapons, the game features both single-player and multiplayer (MMO) elements. Players explore the world of Aida, fight enemies, complete quests, and unlock powerful Simulacra—characters that come with unique weapons and abilities.

This project is not affiliated with the official game. It is intended for fan use, data aggregation, and community-driven tools.

## 🛠️ Data Collection

This API depends on a private CLI tool responsible for extracting and transforming game-related data directly from *Tower of Fantasy* assets.

The data is processed and saved before the API runs, and may be stored in:
- **Databases** (MongoDB or PostgreSQL), or
- **Local JSON files** (for development or backups).

> Due to the nature of the data extraction process, the CLI is not public and is intended for personal or internal use only.

You must ensure the data is properly generated before starting the API.

## 🚀 Technologies Used

- **Python**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **PDM** – Python dependency & package manager
- **PostgreSQL** with **Prisma** ORM
- **MongoDB** (for document-based data)
- **Docker** (optional)

## 📦 Installation

```bash
git clone https://github.com/biellSilva/toweroffantasy.api.git
cd toweroffantasy.api
pdm install
```

## 🔧 How to Run

```bash
pdm run dev
```

Make sure MongoDB and PostgreSQL are running and Prisma is properly configured.  
Then access the interactive API docs:  
[http://localhost:8000/docs](http://localhost:8000/docs)

## 📚 Main Endpoints

| Method | Route                       | Description                                      |
|--------|-----------------------------|--------------------------------------------------|
| GET    | `/simulacra`                 | List all simulacra (paginated)                   |
| GET    | `/simulacra/{simulacrumId}`  | Get details of a specific simulacrum             |
| GET    | `/weapons`                   | List all weapons (paginated)                     |
| GET    | `/weapons/{weaponId}`        | Get details of a specific weapon                 |
| GET    | `/matrices`                  | List all matrices (paginated)                    |
| GET    | `/matrices/{matrixId}`       | Get details of a specific matrix                 |
| GET    | `/banners`                   | List all active banners (paginated)              |

> Endpoints that list multiple records (e.g., `/simulacra`, `/weapons`, `/matrices`) support pagination.

For the complete list of available routes, check out the interactive API documentation:

- **Local environment**: http://localhost:8000/docs
- **Production environment**: https://tof-api.ftae5p.easypanel.host/docs *(replace with your actual production URL when available)*

## 🗄️ Databases

- **PostgreSQL** is used for relational and structured data via [Prisma](https://www.prisma.io/)
- **MongoDB** is used for flexible, document-based data storage

## 📁 Project Structure

The project follows a simple structure, where:

- `app/`: Contains the main API logic (routers, models, schemas, services).
- `prisma/`: Prisma schema and database migrations.
- `pyproject.toml`: Python dependencies management with PDM.
- `README.md`: Project documentation.

For detailed code structure, refer to the [source files](https://github.com/biellSilva/toweroffantasy.api).

## 📄 License

This project is licensed under the MIT License.

---

*Made with ❤️ by [biellSilva](https://github.com/biellSilva)*
