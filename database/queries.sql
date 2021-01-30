SELECT names
FROM athletes
INNER JOIN teams ON athletes.team = teams.name
WHERE teams.noc = 'KEN'
ORDER BY names ASC;

SELECT season, year, event, medal_type
FROM athletes_medals
WHERE athletes_id IN (SELECT id FROM athletes WHERE names='Gregory Efthimios "Greg" Louganis')
ORDER BY year DESC;

SELECT noc, region
FROM nocs
ORDER BY noc ASC;

SELECT noc, gold_medals
FROM teams
ORDER BY gold_medals DESC;
