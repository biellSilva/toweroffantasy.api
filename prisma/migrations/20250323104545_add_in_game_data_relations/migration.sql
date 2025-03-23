-- CreateTable
CREATE TABLE "DataRelation" (
    "imitation_id" TEXT NOT NULL,
    "weapon_id" TEXT NOT NULL,
    "suit_id" TEXT NOT NULL,

    CONSTRAINT "DataRelation_pkey" PRIMARY KEY ("imitation_id","weapon_id","suit_id")
);

-- CreateIndex
CREATE UNIQUE INDEX "DataRelation_imitation_id_key" ON "DataRelation"("imitation_id");

-- CreateIndex
CREATE UNIQUE INDEX "DataRelation_weapon_id_key" ON "DataRelation"("weapon_id");

-- CreateIndex
CREATE UNIQUE INDEX "DataRelation_suit_id_key" ON "DataRelation"("suit_id");
