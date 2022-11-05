-- list all cities of california
--SELECT id AS ca FROM states WHERE name="California";
--SELECT * FROM cities WHERE state_id=ca

SELECT * FROM cities WHERE state_id=(id FROM states WHERE name="California")