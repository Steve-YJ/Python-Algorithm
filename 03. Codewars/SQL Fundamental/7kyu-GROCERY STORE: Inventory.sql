-- select all of the items
SELECT id, name, stock
FROM products
WHERE producent='CompanyA' and stock <= 2
ORDER BY id 