CREATE TABLE parents (parent TEXT, child TEXT);

INSERT INTO parents VALUES
  ('ace', 'bella'),
  ('ace', 'charlie'),
  ('daisy', 'hank'),
  ('finn', 'ace'),
  ('finn', 'daisy'),
  ('finn', 'ginger'),
  ('ellie', 'finn');

CREATE TABLE dogs (name TEXT, fur TEXT, height INTEGER);

INSERT INTO dogs VALUES
  ('ace',     'long',  26),
  ('bella',   'short', 52),
  ('charlie', 'long',  47),
  ('daisy',   'long',  46),
  ('ellie',   'short', 35),
  ('finn',    'curly', 32),
  ('ginger',  'short', 28),
  ('hank',    'curly', 31);

CREATE TABLE sizes (size TEXT, min INTEGER, max INTEGER);

INSERT INTO sizes VALUES
  ('toy',      24, 28),
  ('mini',     28, 35),
  ('medium',   35, 45),
  ('standard', 45, 60);


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child
  FROM dogs JOIN parents ON parents.parent = dogs.name
  ORDER BY height DESC;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT dogs.name AS name, sizes.size AS size
  FROM dogs JOIN sizes ON (dogs.height > sizes.min AND dogs.height <= sizes.max);


-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT a.child AS sible1, b.child AS sible2
  FROM parents AS a, parents AS b
  WHERE a.parent = b.parent AND a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || size1.name || " and " || size2.name || ", have the same size: " || size1.size
  FROM siblings AS a
  JOIN size_of_dogs AS size1 ON a.sible1 = size1.name
  JOIN size_of_dogs AS size2 ON a.sible2 = size2.name
  WHERE size1.size = size2.size;

-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT fur, MAX(height)-MIN(height) AS height_range
  FROM dogs
  --WHERE
  GROUP BY fur
  --所有的同一fur的狗dog要在平均值区间内，有一个不在都不行。
  HAVING MIN(height) >= 0.7*AVG(height) AND MAX(height) <= 1.3*AVG(height);