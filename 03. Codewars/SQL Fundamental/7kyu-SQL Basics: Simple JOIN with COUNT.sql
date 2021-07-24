-- Create your SELECT statement here

SELECT people.id, people.name, count(*) AS toy_count
FROM people
LEFT JOIN toys ON people.id = toys.people_id
GROUP BY people.id