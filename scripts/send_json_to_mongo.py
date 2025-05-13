# type: ignore


import json
from asyncio import run
from pathlib import Path
from typing import Any

import dotenv
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


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


async def fix_relations(mongo_db: AsyncIOMotorDatabase) -> None:
    relations = mongo_db.get_collection("relations")
    simulacra = load_data("src/database/simulacra.json")
    weapons = load_data("src/database/weapons.json")

    for simulacrum in simulacra.values():
        relation: dict[str, Any] = {
            "imitation_id": simulacrum["id"],
            "weapon_id": None,
            "suit_id": None,
        }
        for weapon in weapons.values():
            if (
                simulacrum["weapon_id"]
                and weapon["id"].lower() == simulacrum["weapon_id"].lower()
            ):
                relation["weapon_id"] = weapon["id"]

                if any(
                    weapon["id"].lower() == x.lower()
                    for x in [
                        "stave_thunder",
                        "digger_thunder",
                    ]
                ):
                    relation["suit_id"] = weapon["recommended_matrices"][1]["id"]

                else:
                    relation["suit_id"] = weapon["recommended_matrices"][0]["id"]
                break

        await relations.find_one_and_update(
            filter={"imitation_id": simulacrum["id"]},
            update={"$set": relation},
            upsert=True,
        )

        print(f"{simulacrum['id']} sent!")  # noqa: T201


async def main() -> None:
    mongo = AsyncIOMotorClient(dotenv.get_key(dotenv.find_dotenv(), "MONGO_URI"))
    mongo_db = mongo.get_database("prod")

    for collection in COLLECTIONS:
        _data = load_data(f"src/database/{collection}.json")
        print(f"Loaded {len(_data)} {collection}.")  # noqa: T201

        mongo_collection = mongo_db.get_collection(collection)

        for data in _data.values():
            if collection == "matrices" and str(data["id"]).startswith("S"):
                data["id"] = str(data["id"]).replace("S", "s", 1)

            await mongo_collection.find_one_and_update(
                filter={"id": data["id"]},
                update={"$set": data},
                upsert=True,
            )

            print(f"{data['id']} sent!")  # noqa: T201

    await fix_relations(mongo_db)

    print("Done!")  # noqa: T201


if __name__ == "__main__":
    run(main())
