-- list the number of records
SELECT score, count(*) AS number FROM second_table GROUP BY score DESC;