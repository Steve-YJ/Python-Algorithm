--- 3, 2, 1, fight! ---
SELECT name, sum(won) as won, sum(lost) as lost
FROM fighters
LEFT JOIN winning_moves ON move_id = winning_moves.id
WHERE move NOT IN ('Hadoken', 'Shouoken', 'Kikoken')
GROUP BY name
ORDER BY sum(won) DESC
LIMIT 6;
