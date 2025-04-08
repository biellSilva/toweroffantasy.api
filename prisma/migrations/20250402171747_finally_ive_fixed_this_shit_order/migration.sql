DROP VIEW IF EXISTS public."SimulacraOrderedView";

CREATE VIEW public."SimulacraOrderedView" AS
WITH
    banner_ordenado AS (
        SELECT DISTINCT
            ON (imitation_id) imitation_id,
            position
        FROM public."BannerOrderedView"
        ORDER BY imitation_id, position ASC
    )
SELECT s.*, COALESCE(b.position, NULL) AS banner_position
FROM public."Simulacra" s
    LEFT JOIN banner_ordenado b ON s.id = b.imitation_id
ORDER BY
    banner_position DESC NULLS LAST, -- Ordena primeiro pelos que estão no Banner
    is_limited DESC, -- Depois pelos limitados (TRUE primeiro)
    no_weapon DESC, -- Depois pelos que possuem arma (TRUE primeiro)
    CASE rarity -- Ordena rarity: SSR antes de SR
        WHEN "SSR" THEN 1
        WHEN "SR" THEN 2
        WHEN "R" then 3
        when "N" then 4
        ELSE 5
    END;