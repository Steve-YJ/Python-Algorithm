-- Replace with your SQL Query
SELECT count(country) as products, country
FROM products
WHERE country IN ('United States of America', 'Canada')
GROUP BY country
ORDER BY count(country) DESC