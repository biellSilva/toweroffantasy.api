-- AlterTable
ALTER TABLE "Banner" ALTER COLUMN "link" DROP NOT NULL;

-- CreateTable
CREATE TABLE "Weapon" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "desc" TEXT NOT NULL,
    "brief" TEXT NOT NULL,
    "lottery_desc" TEXT NOT NULL,
    "rarity" TEXT NOT NULL,
    "quality" TEXT NOT NULL,
    "is_fate" BOOLEAN NOT NULL,
    "is_limited" BOOLEAN NOT NULL,
    "is_warehouse" BOOLEAN NOT NULL,
    "element" JSONB NOT NULL,
    "category" JSONB NOT NULL,
    "shatter" JSONB NOT NULL,
    "charge" JSONB NOT NULL,
    "skills" JSONB[],
    "advancements" JSONB[],
    "passives" TEXT[],
    "values" DOUBLE PRECISION[],
    "multi_element" JSONB[],
    "fashions" JSONB[],
    "recommended_matrices" JSONB[],
    "assets" JSONB NOT NULL,

    CONSTRAINT "Weapon_pkey" PRIMARY KEY ("id")
);
