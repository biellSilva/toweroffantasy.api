from datetime import datetime
from zoneinfo import ZoneInfo

import dotenv
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pydantic import BaseModel


class CreateBanner(BaseModel):
    imitation_id: str
    weapon_id: str
    suit_id: str | None = None

    start_at: datetime
    end_at: datetime
    link: str | None = None

    limited_only: bool = False
    is_rerun: bool = False
    is_collab: bool = False
    final_rerun: bool = False


async def create_new_banner(
    *,
    mongo_db: AsyncIOMotorDatabase,
    imitation_id: str,
    start_at: datetime,
    end_at: datetime,
    link: str | None = None,
    is_limited: bool = False,
    is_collab: bool = False,
) -> CreateBanner:
    response = await mongo_db.get_collection("relations").find_one(
        filter={"imitation_id": imitation_id},
    )
    if not response:
        msg = f"Imitation with id {imitation_id} not found in database."
        raise ValueError(msg)

    banner = CreateBanner(
        imitation_id=response["imitation_id"],
        weapon_id=response["weapon_id"],
        suit_id=response["suit_id"],
        start_at=start_at,
        end_at=end_at,
        link=link,
        limited_only=is_limited,
        is_collab=is_collab,
    )

    print("Creating release banner \n", banner)  # noqa: T201

    return banner


async def create_rerun_banner(
    *,
    mongo_db: AsyncIOMotorDatabase,
    imitation_id: str,
    start_at: datetime,
    end_at: datetime,
    link: str | None = None,
    final_rerun: bool = False,
) -> CreateBanner:
    response = await mongo_db.get_collection("banners").find_one(
        filter={"imitation_id": imitation_id},
    )
    if not response:
        msg = f"Imitation with id {imitation_id} not found in database."
        raise ValueError(msg)

    banner = CreateBanner(
        imitation_id=response["imitation_id"],
        weapon_id=response["weapon_id"],
        suit_id=response["suit_id"],
        start_at=start_at,
        end_at=end_at,
        link=link,
        limited_only=response.get("limited_only", False),
        is_collab=response.get("is_collab", False),
        is_rerun=True,
        final_rerun=final_rerun,
    )

    print("Creating rerun banner \n", banner)  # noqa: T201

    return banner


async def main() -> None:
    mongo = AsyncIOMotorClient(dotenv.get_key(dotenv.find_dotenv(), "MONGO_URI"))
    mongo_db = mongo.get_database("prod")

    link = "https://tof.perfectworld.com/eneu/news/notice/20250617/256911.shtml"
    start_at = datetime(2025, 6, 24, 6, 0, 0, tzinfo=ZoneInfo("UTC"))
    end_at = datetime(2025, 7, 28, 21, 0, 0, tzinfo=ZoneInfo("UTC"))

    banners = [
        await create_new_banner(
            mongo_db=mongo_db,
            imitation_id="imitation_72",
            link=link,
            start_at=start_at,
            end_at=end_at,
            is_limited=False,
            is_collab=False,
        ),
        await create_rerun_banner(
            mongo_db=mongo_db,
            imitation_id="imitation_71",
            link=link,
            start_at=start_at,
            end_at=end_at,
        ),
        await create_rerun_banner(
            mongo_db=mongo_db,
            imitation_id="imitation_65",
            link=link,
            start_at=start_at,
            end_at=end_at,
        ),
        await create_rerun_banner(
            mongo_db=mongo_db,
            imitation_id="imitation_64",
            link=link,
            start_at=start_at,
            end_at=end_at,
        ),
        await create_rerun_banner(
            mongo_db=mongo_db,
            imitation_id="imitation_59",
            link=link,
            start_at=start_at,
            end_at=end_at,
        ),
        await create_rerun_banner(
            mongo_db=mongo_db,
            imitation_id="imitation_57",
            link=link,
            start_at=start_at,
            end_at=end_at,
        ),
        await create_rerun_banner(
            mongo_db=mongo_db,
            imitation_id="imitation_53",
            link=link,
            start_at=start_at,
            end_at=end_at,
        ),
        await create_rerun_banner(
            mongo_db=mongo_db,
            imitation_id="imitation_46",
            link=link,
            start_at=start_at,
            end_at=end_at,
        ),
    ]

    await mongo_db.get_collection("banners").insert_many(
        [banner.model_dump(mode="json") for banner in banners],
        ordered=False,
    )

    print("Banners created successfully.")  # noqa: T201


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
