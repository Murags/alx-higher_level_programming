-- select records from table
SELECT state, MAX(value) FROM temperatures GROUP BY state ORDER BY state
