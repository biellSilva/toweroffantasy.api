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


COLLECTIONS = [
    "simulacra",
    "weapons",
    "matrices",
    "gifts",
    "mounts",
]


async def main() -> None:
    mongo = AsyncIOMotorClient(dotenv.get_key(dotenv.find_dotenv(), "MONGO_URI"))
    mongo_db = mongo.get_database("dev")

    for collection in COLLECTIONS:
        _data = load_data(f"src/database/{collection}.json")
        print(f"Loaded {len(_data)} {collection}.")  # noqa: T201

        mongo_collection = mongo_db.get_collection(collection)

        for data in _data.values():
            await mongo_collection.find_one_and_update(
                filter={"id": data["id"]},
                update={"$set": data},
                upsert=True,
            )

            print(f"{data['id']} sent!")  # noqa: T201

    print("Done!")  # noqa: T201


if __name__ == "__main__":
    run(main())
