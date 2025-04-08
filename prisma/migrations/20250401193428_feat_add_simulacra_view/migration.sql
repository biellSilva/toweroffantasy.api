-- This is a manual migration. It creates a view that orders the banners by start_at date.

DROP VIEW IF EXISTS public."SimulacraOrderedView";

CREATE VIEW public."SimulacraOrderedView" AS
SELECT s.*
FROM public."Simulacra" s
    LEFT JOIN public."BannerOrderedView" b ON s.id = b.imitation_id
ORDER BY
    b.position DESC NULLS LAST, -- Ordena pelos IDs encontrados em BannerOrderedView primeiro
    s.is_limited DESC, -- Simulacra limitados primeiro
    s.no_weapon DESC, -- Simulacra sem arma antes dos outros
    CASE s.rarity -- Ordenação por raridade: SSR antes de SR
        WHEN 'SSR' THEN 1
        WHEN 'SR' THEN 2
        ELSE 3
    END;