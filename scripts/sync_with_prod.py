import dotenv
from motor.motor_asyncio import AsyncIOMotorClient


async def main() -> None:
    mongo = AsyncIOMotorClient(dotenv.get_key(dotenv.find_dotenv(), "MONGO_URI"))

    prod = mongo.get_database("prod")
    dev = mongo.get_database("dev")

    for coll in await dev.list_collection_names():
        async for data in dev.get_collection(coll).find():
            data = dict(data)  # noqa: PLW2901
            data.pop("_id", None)

            if coll == "banners":
                await prod.get_collection(coll).find_one_and_update(
                    filter={"imitation_id": data["imitation_id"]},
                    update={"$set": data},
                    upsert=True,
                )
                continue

            await prod.get_collection(coll).find_one_and_update(
                filter={"id": data["id"]},
                update={"$set": data},
                upsert=True,
            )

        print(f"{coll} sent!")  # noqa: T201
    print("Done!")  # noqa: T201


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
