-- This is a manual migration. It creates a view that orders the banners by start_at date.

CREATE VIEW public."BannerOrderedView" AS
select *, ROW_NUMBER() OVER (
        ORDER BY start_at ASC
    ) AS position
FROM public."Banner";