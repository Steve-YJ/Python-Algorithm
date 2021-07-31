/*  SQL  */
SELECT
  id,
  name,
  case when position(',' in characteristics)=0
  then characteristics
  else split_part(characteristics, ',', 1)   
  end  AS characteristic
FROM monsters
ORDER BY id