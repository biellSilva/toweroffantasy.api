# type: ignore

import json
from asyncio import run
from pathlib import Path
from typing import Any

import dotenv
from motor.motor_asyncio import AsyncIOMotorClient


def load_data(path: str | Path) -> dict[str, dict[str, Any]]:
    if isinstance(path, str):
        path = Path(path)

    return json.loads(path.read_bytes().decode("utf-8"))


async def main() -> None:
    _data = load_data("src/database/matrices.json")
    print(f"Loaded {len(_data)} matrices.")  # noqa: T201

    mongo = AsyncIOMotorClient(dotenv.get_key(dotenv.find_dotenv(), "MONGO_URI"))

    collection = mongo.get_database("dev").get_collection("matrices")

    for data in _data.values():
        collection.find_one_and_update(
            filter={"id": data["id"]},
            update={"$set": data},
            upsert=True,
        )

        print(f"{data['id']} sent!")  # noqa: T201

    print("Done!")  # noqa: T201


if __name__ == "__main__":
    run(main())
