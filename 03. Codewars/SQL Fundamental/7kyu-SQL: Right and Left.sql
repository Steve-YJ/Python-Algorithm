/*  SQL  */
SELECT 
--   address AS Origin_Add,
--   commits AS commits,
--   contributors AS contributors,
  substring(project FROM 1 FOR commits) AS project, 
  reverse(substring(reverse(address) FROM 1 FOR contributors)) AS address  -- I'm not good at SQL, So I used reverse() and substring(reverse())
FROM repositories