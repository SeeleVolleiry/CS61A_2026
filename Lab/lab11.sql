CREATE table newest AS
  SELECT title, year 
  FROM titles
  ORDER BY year DESC
  LIMIT 10;


CREATE table dog_movies AS 
  SELECT title, character
  FROM titles JOIN principals ON titles.tconst = principals.tconst
  WHERE character LIKE "%dog%";


CREATE table leads AS 
  SELECT name, count(*) AS lead_roles
  FROM names JOIN principals ON names.nconst = principals.nconst
  WHERE ordering = 1
  GROUP BY names.nconst
  HAVING count(*) > 10;


CREATE table long_movies AS 
  SELECT ( year / 10 * 10) || "s" AS decade, count(*) AS count
  FROM titles
  WHERE runtime > 180
  GROUP BY year / 10;

