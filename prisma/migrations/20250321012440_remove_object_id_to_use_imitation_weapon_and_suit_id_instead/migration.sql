/*
  Warnings:

  - You are about to drop the column `object_id` on the `Banner` table. All the data in the column will be lost.
  - Added the required column `imitation_id` to the `Banner` table without a default value. This is not possible if the table is not empty.
  - Added the required column `suit_id` to the `Banner` table without a default value. This is not possible if the table is not empty.
  - Added the required column `weapon_id` to the `Banner` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Banner" DROP COLUMN "object_id",
ADD COLUMN     "imitation_id" TEXT NOT NULL,
ADD COLUMN     "suit_id" TEXT NOT NULL,
ADD COLUMN     "weapon_id" TEXT NOT NULL;
