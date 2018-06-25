-- count the numbers of scores and dispalys them in order
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC
;
