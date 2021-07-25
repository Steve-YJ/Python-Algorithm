--your code here--
SELECT sailorsenshi.senshi_name AS sailor_senshi, sailorsenshi.real_name_jpn as real_name, cats.name AS cat, schools.school AS school
FROM sailorsenshi
LEFT JOIN cats ON cats.id = sailorsenshi.cat_id
LEFT JOIN schools ON schools.id=sailorsenshi.school_id