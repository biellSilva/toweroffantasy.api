DROP VIEW IF EXISTS public."SimulacraOrderedView";

CREATE VIEW public."SimulacraOrderedView" AS
SELECT *
FROM (
        SELECT s.*, ROW_NUMBER() OVER (
                PARTITION BY
                    s.id
                ORDER BY
                    b.position DESC NULLS LAST, -- Ordena pelos IDs encontrados em BannerOrderedView primeiro
                    s.is_limited DESC, -- Simulacra limitados primeiro
                    s.no_weapon DESC, -- Simulacra sem arma antes dos outros
                    CASE s.rarity -- Ordenação por raridade: SSR antes de SR
                        WHEN 'SSR' THEN 5
                        WHEN 'SR' THEN 4
                        ELSE 3
                    END
            ) AS row_num
        FROM public."Simulacra" s
            LEFT JOIN public."BannerOrderedView" b ON s.id = b.imitation_id
    ) ranked
WHERE
    row_num = 1;