-- This is a manual migration. It creates a view that orders the banners by start_at date.

DROP VIEW IF EXISTS public."BannerOrderedView";

CREATE VIEW public."BannerOrderedView" AS
select *, ROW_NUMBER() OVER (
        ORDER BY start_at ASC, is_rerun DESC
    ) AS position
FROM public."Banner";