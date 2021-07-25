--but on the land of Lórien no shadow lay--

SELECT CONCAT(initcap(firstname), ' ', initcap(lastname)) AS shortlist
FROM Elves
WHERE 
  firstname LIKE '%tegil%' OR
  lastname LIKE '%astar%';