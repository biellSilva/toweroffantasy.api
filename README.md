# toweroffantasy.api

A RESTful API that provides data related to the game **Tower of Fantasy**, such as simulacra, weapons, matrices, events, and more. The goal is to centralize and serve updated information in a structured and accessible way.

[**Tower of Fantasy**](https://tof.perfectworld.com/en-us/index.html) is a free-to-play open-world action RPG developed by **Hotta Studio** and published by **Level Infinite** and **Perfect World Games** in certain regions. Set in a futuristic sci-fi universe filled with exploration, fast-paced combat, and a gacha system for acquiring characters and weapons, the game features both single-player and multiplayer (MMO) elements. Players explore the world of Aida, fight enemies, complete quests, and unlock powerful Simulacra—characters that come with unique weapons and abilities.

This project is not affiliated with the official game. It is intended for fan use, data aggregation, and community-driven tools.

## 🛠️ Data Collection

This API depends on a private CLI tool responsible for extracting and transforming game-related data directly from _Tower of Fantasy_ assets.

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

| Method | Route                       | Description                          |
| ------ | --------------------------- | ------------------------------------ |
| GET    | `/simulacra`                | List all simulacra (paginated)       |
| GET    | `/simulacra/{simulacrumId}` | Get details of a specific simulacrum |
| GET    | `/weapons`                  | List all weapons (paginated)         |
| GET    | `/weapons/{weaponId}`       | Get details of a specific weapon     |
| GET    | `/matrices`                 | List all matrices (paginated)        |
| GET    | `/matrices/{matrixId}`      | Get details of a specific matrix     |
| GET    | `/banners`                  | List all active banners (paginated)  |

> Endpoints that list multiple records (e.g., `/simulacra`, `/weapons`, `/matrices`) support pagination.

For the complete list of available routes, check out the interactive API documentation:

- **Local environment**: http://localhost:8000/docs
- **Production environment**: https://tof-api.ftae5p.easypanel.host/docs _(replace with your actual production URL when available)_

## 🗄️ Databases

- **PostgreSQL** is used for relational and structured data via [Prisma](https://www.prisma.io/)
- **MongoDB** is used for flexible, document-based data storage

## 📁 Project Structure

The project follows a simple structure, where:

- `src/`: Contains the main API logic (routers, models, schemas, services).
- `prisma/`: Prisma schema and database migrations.
- `src/locales/`: Contains language-specific translation files. Each language has its own folder, and the translation data is stored in JSON files (e.g., `src/locales/en/Game.json` for English).
- `pyproject.toml`: Python dependencies management with PDM.
- `README.md`: Project documentation.

For detailed code structure, refer to the [source files](https://github.com/biellSilva/toweroffantasy.api).

## 🌍 Localization Support

The translation files are extracted directly from the game _Tower of Fantasy_ and stored in the `src/locales/` directory. Each language has its own folder, and the translation data is saved in JSON files (e.g., `src/locales/en/Game.json` for English).

These files are automatically updated when new data or localization changes are introduced in the game.

Example of available translation files:

- `src/locales/en/Game.json` – English translations for game-related data.
- `src/locales/pt/Game.json` – Portuguese translations for game-related data.
- `src/locales/de/Game.json` – German translations for game-related data.

### How Translations Are Managed

1. **Data Extraction**: The translation files are pulled from the game's files using a custom CLI tool designed for scraping and extracting the localization data. This ensures that the translations are always up-to-date with the latest changes in the game.
2. **File Structure**: Each language has its own directory inside `src/locales/`, and each translation is stored in a separate JSON file (e.g., `Game.json`).
3. **Adding New Languages**: To add a new language, you would need to extract the translations for that language from the game, create a new folder in `src/locales/`, and place the corresponding JSON file inside it.

### Fallback Mechanism

If a string is not found in the translation file for the requested language, the API follows a fallback mechanism:

1. **Preferred Language**: If the requested language is not available, the system first looks for the translation in **English** (en).
2. **Fallback to Chinese**: If the string is not found in English, it will then fall back to **Chinese** (zh-CN).
3. **Order of Fallbacks**: The order of fallback languages is:
   - `lang` -> English (`en`) -> Chinese (`zh-CN`).

This ensures that even if the translation is missing in a specific language, the system will always try to serve a reasonable fallback value.

By default, the API will serve the data in the language specified in the request header (e.g., `Accept-Language`), and it will fall back to English and then Chinese if the requested language or string is not available.

### Example of the Folder Structure:

```
src/
├── locales/
│   ├── en/
│   │   └── Game.json
│   ├── pt/
│   │   └── Game.json
│   └── zh-CN/
│       └── Game.json
```

## 🛡️ License

**All Rights Reserved.**

This project is protected under the "All Rights Reserved" license. You may not copy, modify, distribute, or use any part of this repository or its contents for commercial or public purposes without explicit written permission from the author.

### ⚠️ Disclaimer

This project uses data extracted from the game _Tower of Fantasy_. All game-related data, names, assets, and translations remain the intellectual property of their respective owners — **Hotta Studio**, **Level Infinite**, and **Perfect World Games**.

This project is **not affiliated with, endorsed, or sponsored by** Hotta Studio, Level Infinite, or Perfect World Games.  
No copyright infringement is intended.

The API and its associated tools are provided **for educational and informational purposes only**, and no game files or proprietary content are distributed directly.

Use at your own risk.

---

_Made with ❤️ by [biellSilva](https://github.com/biellSilva)_
