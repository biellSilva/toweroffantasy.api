-- AlterTable
ALTER TABLE "User" ALTER COLUMN "created_at" SET DATA TYPE TIMESTAMPTZ,
ALTER COLUMN "updated_at" SET DATA TYPE TIMESTAMPTZ;

-- CreateTable
CREATE TABLE "Banner" (
    "id" SERIAL NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL,
    "object_id" TEXT NOT NULL,
    "start_at" TIMESTAMPTZ NOT NULL,
    "end_at" TIMESTAMPTZ NOT NULL,
    "link" TEXT NOT NULL,
    "limited_only" BOOLEAN NOT NULL DEFAULT false,
    "is_rerun" BOOLEAN NOT NULL DEFAULT false,
    "is_collab" BOOLEAN NOT NULL DEFAULT false,
    "final_rerun" BOOLEAN NOT NULL DEFAULT false,

    CONSTRAINT "Banner_pkey" PRIMARY KEY ("id")
);
