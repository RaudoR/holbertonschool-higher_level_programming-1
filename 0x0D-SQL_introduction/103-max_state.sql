-- This gets the average of the scores
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC
LIMIT 3
;
