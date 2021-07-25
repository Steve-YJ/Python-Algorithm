--your code here--
SELECT
  ss.senshi_name AS sailor_senshi,
  ss.real_name_jpn AS real_name,
  ca.name AS cat,
  sc.school AS school
  
FROM sailorsenshi as ss
LEFT JOIN cats as ca ON cat_id = ca.id
LEFT JOIN schools as sc ON school_id = sc.id