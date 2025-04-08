-- CreateTable
CREATE TABLE "Simulacra" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "unlock_info" TEXT NOT NULL,
    "desc" TEXT NOT NULL,
    "rarity" TEXT NOT NULL,
    "sex" TEXT NOT NULL,
    "assets" JSONB NOT NULL,
    "assetsA3" JSONB,
    "weapon_id" TEXT NOT NULL,
    "suit_id" TEXT NOT NULL,
    "avatar_id" TEXT NOT NULL,
    "is_limited" BOOLEAN NOT NULL,
    "no_weapon" BOOLEAN NOT NULL,
    "extras" JSONB NOT NULL,
    "fashions" JSONB[],
    "likeabilities" JSONB[],

    CONSTRAINT "Simulacra_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "Banner" ADD CONSTRAINT "Banner_imitation_id_fkey" FOREIGN KEY ("imitation_id") REFERENCES "Simulacra"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Simulacra" ADD CONSTRAINT "Simulacra_id_fkey" FOREIGN KEY ("id") REFERENCES "DataRelation"("imitation_id") ON DELETE RESTRICT ON UPDATE CASCADE;
