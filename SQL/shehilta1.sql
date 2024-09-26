CREATE INDEX idx_mission_mission_date ON mission(EXTRACT(YEAR FROM mission_date));

EXPLAIN ANALYZE
SELECT m.air_force, m.target_city, COUNT(m.mission_id) AS mission_count
FROM mission m
WHERE EXTRACT(YEAR FROM mission_date) = 1944
GROUP BY m.air_force, m.target_city
ORDER BY mission_count DESC;

#in the first run the result was -- Execute Time: 303.921 ms
#after indexing the result was -- Execute Time: 40.081 ms