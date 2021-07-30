/*  SQL  */

SELECT 
CASE WHEN sum(number1)%2=1 then min(number1)
ELSE max(number1)
END AS number1,
CASE WHEN sum(number2)%2=1 then min(number2)
ELSE max(number2)
END AS number2
--IF(sum(number1)%2=1, min(number1), max(number1)) AS number1, 
--IF(sum(number2)%2=1, min(number2), max(number2)) AS number2
FROM numbers