-- CreateEnum
CREATE TYPE "Roles" AS ENUM ('ADMIN', 'MODERATOR', 'USER');

-- AlterTable
ALTER TABLE "User" ADD COLUMN     "roles" "Roles"[] DEFAULT ARRAY['USER']::"Roles"[];
