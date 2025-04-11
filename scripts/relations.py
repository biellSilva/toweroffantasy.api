from typing import Any

import dotenv
from motor.motor_asyncio import AsyncIOMotorClient


async def main() -> None:
    mongo = AsyncIOMotorClient(dotenv.get_key(dotenv.find_dotenv(), "MONGO_URI"))

    db = mongo.get_database(dotenv.get_key(dotenv.find_dotenv(), "MONGO_DB"))

    simulacra = await db.get_collection("simulacra").find().to_list(length=None)
    weapons = await db.get_collection("weapons").find().to_list(length=None)

    relations = db.get_collection("relations")

    for simulacrum in simulacra:
        relation: dict[str, Any] = {
            "imitation_id": simulacrum["id"],
            "weapon_id": None,
            "suit_id": None,
        }
        for weapon in weapons:
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

    print("Done!")  # noqa: T201


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
