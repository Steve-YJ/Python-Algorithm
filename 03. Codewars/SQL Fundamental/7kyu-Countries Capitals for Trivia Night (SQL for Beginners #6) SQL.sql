-- Your solution here
SELECT capital
FROM countries
WHERE country LIKE 'E%' and continent IN ('Afrika', 'Africa')
ORDER BY capital
LIMIT 3;