-- i choose you! --
-- A-ha! 
-- You are Ash Ketchum! you want to fight grass type pokemon!


SELECT p.pokemon_name, (p.str * mul.multiplier) AS modifiedStrength, mul.element
FROM pokemon p
LEFT JOIN multipliers mul ON p.element_id = mul.id
WHERE (p.str * mul.multiplier) > 40  -- don't forget using where clause!
ORDER BY modifiedStrength DESC