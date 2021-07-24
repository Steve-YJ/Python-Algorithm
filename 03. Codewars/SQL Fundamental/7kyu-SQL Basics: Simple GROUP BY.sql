-- Create your SELECT statement here
SELECT age, count(age) AS people_count
FROM people
GROUP BY age