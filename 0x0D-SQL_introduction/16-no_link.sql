-- This list all the table with scores and name only when name is not null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
;
