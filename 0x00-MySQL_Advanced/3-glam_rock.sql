-- Script that lists all bands with glam rock style
-- ranked by their longetivity, using formed and split

SELECT band_name, (COALESCE(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
