# Lab11: SQL

## SQL Basics

A SELECT statement describes an output table based on input rows. To write one:

    Describe the input rows using FROM and WHERE clauses.
    Group those rows and determine which groups should appear as output rows using GROUP BY and HAVING clauses.
    Format and order the output rows and columns using SELECT and ORDER BY clauses.
    SELECT (Step 3) FROM (Step 1) WHERE (Step 1) GROUP BY (Step 2) HAVING (Step 2) ORDER BY (Step 3);
Step 1 may involve joining tables (using commas) to form input rows that consist of two or more rows from existing tables.
The WHERE, GROUP BY, HAVING, and ORDER BY clauses are optional.

### Creating Tables and Insert values

```sql
CREATE TABLE big_game (
    berkeley INTEGER, stanford INTEGER, year INTEGER);

INSERT INTO big_game (berkeley, stanford, year) VALUES
    (30, 7, 2002),
    (28, 16, 2003),
    (17, 38, 2014);

sqlite> .mode column
sqlite> SELECT * FROM big_game;
berkeley  stanford  year
--------  --------  ----
30        7         2002
28        16        2003
17        38        2014
```

### Selecting From Tables

Typically, we will create a new table from existing tables using a SELECT statement:

    SELECT [columns] FROM [tables] WHERE [condition] ORDER BY [columns] LIMIT [limit];

Let's break down this statement:

    1. SELECT [columns] tells SQL that we want to include the given columns in our output table; [columns] is a comma-separated list of column names, and * can be used to select all columns
    2. FROM [table] tells SQL that the columns we want to select are from the given table
    3. WHERE [condition] filters the output table by only including rows whose values satisfy the given [condition], a boolean expression
    4. ORDER BY [columns] orders the rows in the output table by the given comma-separated list of columns; by default, values are sorted in ascending order (ASC), but you can use DESC to sort in descending order
    5. LIMIT [limit] limits the number of rows in the output table by the integer [limit]

Here are some examples:
```sql
-- 单行注释
/*
多行注释
*/

sqlite> SELECT berkeley FROM big_game WHERE year > 2002;
28
17

sqlite> SELECT berkeley, stanford FROM big_game WHERE berkeley > stanford;
30|7
28|16

sqlite> SELECT year FROM big_game WHERE stanford > 15;
2003
2014
```

### SQL Operators

Expressions in the SELECT, WHERE, and ORDER BY clauses can contain one or more of the following operators:

    comparison operators: =, >, <, <=, >=, <> or != ("not equal")
    boolean operators: AND, OR
    arithmetic operators: +, -, *, /
    concatenation operator: ||

```sql
--Output the ratio of Berkeley's score to Stanford's score each year:
sqlite> select berkeley * 1.0 / stanford from big_game;
0.447368421052632
1.75
4.28571428571429

--Output the sum of scores in years where both teams scored over 10 points:
sqlite> select berkeley + stanford from big_game where berkeley > 10 and stanford > 10;
55
44

/*Output a table with a single column and single row containing the value "hello world":*/
sqlite> SELECT "hello" || " " || "world";
hello world
```

### Joins

To select data from multiple tables, we can use joins. There are many types of joins, but the only one we'll worry about is the inner join.
We can select from multiple different tables or from the same table multiple times.
To perform an `inner join` on two on more tables, simply list them all out in the FROM clause of a SELECT statement:

    SELECT [columns] FROM [table1], [table2], ... WHERE [condition] ORDER BY [columns] LIMIT [limit];
When we join two or more tables, the default output is a `cartesian product`(笛卡尔积).

If a column name exists in more than one of the tables being joined, or if we join a table with itself, we must disambiguate the column names using dot notation and aliases.

```sql
--创建表格 coaches
CREATE TABLE coaches (
    name TEXT,
    start INTEGER,
    end INTEGER
);

INSERT INTO coaches (name, start, end)
VALUES
    ('Jeff Tedford', 2002, 2012),
    ('Sonny Dykes', 2013, 2016),
    ('Justin Wilcox', 2017, 2025);

/*When we join two or more tables, the default output is a cartesian product.
For example, if we joined big_game with coaches, we'd get the following: */
sqlite> SELECT * FROM big_game JOIN coaches;
berkeley  stanford  year  name           start  end
--------  --------  ----  -------------  -----  ----
30        7         2002  Jeff Tedford   2002   2012
30        7         2002  Sonny Dykes    2013   2016
30        7         2002  Justin Wilcox  2017   2025
28        16        2003  Jeff Tedford   2002   2012
28        16        2003  Sonny Dykes    2013   2016
28        16        2003  Justin Wilcox  2017   2025
17        38        2014  Jeff Tedford   2002   2012
17        38        2014  Sonny Dykes    2013   2016
17        38        2014  Justin Wilcox  2017   2025

/*If we want to match up each game with the coach that season,
 we'd have to compare columns from the two tables in the WHERE clause:*/
sqlite> SELECT * FROM big_game JOIN coaches ON year >= start AND year <= end
   ...> ;
berkeley  stanford  year  name          start  end
--------  --------  ----  ------------  -----  ----
30        7         2002  Jeff Tedford  2002   2012
28        16        2003  Jeff Tedford  2002   2012
17        38        2014  Sonny Dykes   2013   2016

/*In the query below, we give the alias a to the first big_game table and the alias b to the second big_game table.
  We can then reference columns from each table using dot notation with the aliases.
  e.g. a.Berkeley, a.Stanford, and a.Year to select from the first table.
*/
sqlite> SELECT b.Berkeley - a.Berkeley, b.Stanford - a.Stanford, a.Year, b.Year
   ...>   FROM big_game AS a, big_game AS b WHERE a.Year < b.Year;
b.Berkeley - a.Berkeley  b.Stanford - a.Stanford  year  year
-----------------------  -----------------------  ----  ----
-2                       9                        2002  2003
-13                      31                       2002  2014
-11                      22                       2003  2014
```

### SQL Aggregation and Group

SQL Aggregation: Applying an `aggregate function` such as MAX(column) combines the values from multiple rows into an output row.

What if we wanted to group together the values in similar rows and perform the aggregation operations within those groups? We use a `GROUP BY` clause.
Just like how we can filter out rows with WHERE, we can also filter out groups with `HAVING`.
Typically, a HAVING clause should use an aggregation function, such as `DISTINCT`.

```sql
-- Here's another example table, this time about flights:
CREATE TABLE flights (
    departure TEXT, arrival TEXT, price INTEGER);

INSERT INTO flights (departure, arrival, price) VALUES
    ('SFO', 'LAX', 97),
    ('SFO', 'AUH', 848),
    ('LAX', 'SLC', 115),
    ('SFO', 'PDX', 192),
    ('AUH', 'SEA', 932),
    ('SLC', 'PDX', 79),
    ('SFO', 'LAS', 40),
    ('SLC', 'LAX', 117),
    ('SEA', 'PDX', 32),
    ('SLC', 'SEA', 42),
    ('SFO', 'SLC', 97),
    ('LAS', 'SLC', 50),
    ('LAX', 'PDX', 89);

-- if we wanted to count the number of rows in our flights table, we could use:
sqlite> SELECT COUNT(*) from FLIGHTS;
13

/*For each unique departure, collect all of the rows having the same departure airport into a group.
  Then, select the price column and apply the MIN aggregation to recover the price of the cheapest departure from that group.
  The end result is a table of departure airports and the cheapest departing flight.*/
sqlite> SELECT departure, MIN(price) FROM flights GROUP BY departure;
departure  MIN(price)
---------  ----------
AUH        932
LAS        50
LAX        89
SEA        32
SFO        40
SLC        42

-- Suppose we want to see all airports with at least two departures:
sqlite> SELECT departure FROM flights GROUP BY departure HAVING COUNT(*) >= 2;
departure
---------
LAX
SFO
SLC

-- Enumerating all the different departure airports available in our flights table(in this case: SFO, LAX, AUH, SLC, SEA, and LAS).
sqlite> SELECT COUNT(DISTINCT departure) AS destinations FROM flights;
destinations
------------
6
```

### SQL Usage in assignments

You can start an interactive SQLite session in your Terminal or Git Bash with the following command:

    python3 sqlite_shell.py

While the interpreter is running, you can type .help to see some of the commands you can run.
To exit out of the SQLite interpreter, type `.exit` or `.quit` or press `Ctrl-C`.
Remember that if you see ...> after pressing enter, you probably forgot a `;`.

You can also run all the statements in a `.sql` file by doing the following: (Here we're using the lab11.sql file as an example.)

    Runs your code and then exits SQLite immediately afterwards.
        python3 sqlite_shell.py < lab11.sql
    
    Runs your code and then opens an interactive SQLite session, which is similar to running Python code with the interactive -i flag.
        python3 sqlite_shell.py --init lab11.sql


## IMDb:一个数据库

The IMDb 1000 dataset contains the 1000 highest rated popular movies (top 0.2% of votes) from the Internet Movie Database.

tconst is a unique identifier for each movie (the t is for title), and nconst is a unique identifier for each person.

```sql
% sqlite3
sqlite> .read imdb1000.sql
sqlite> .tables
crew        names       principals  ratings     titles

sqlite> .mode column
sqlite> SELECT tconst, title, year, runtime FROM titles LIMIT 3;
tconst     title                            year  runtime
---------  -------------------------------  ----  -------
tt0012349  The Kid                          1921  68
tt0013442  Nosferatu: A Symphony of Horror  1922  94
tt0015864  The Gold Rush                    1925  95

sqlite> SELECT tconst, ordering, nconst, character FROM principals LIMIT 3;
tconst     ordering  nconst     character
---------  --------  ---------  ---------
tt0012349  1         nm0000122  A Tramp
tt0012349  2         nm0701012  The Woman
tt0012349  3         nm0001067  The Child

sqlite> SELECT nconst, name, birth, death FROM names LIMIT 3;
nconst     name            birth  death
---------  --------------  -----  -----
nm0000002  Lauren Bacall   1924   2014
nm0000004  John Belushi    1949   1982
nm0000005  Ingmar Bergman  1918   2007
```

## Q1: Newest Movies

Create a table newest that contains the 10 newest movies in the dataset, and that has two columns:

    title: The name of a movie
    year: The year the movie was made

```sql
SELECT title, year FROM titles
ORDER BY DSC -- 降序排序，最新的在上面
LIMIT 10; -- 10部
```


## Q2: Movies with Dogs

Create a dog_movies table that includes one row for each movie character that includes the word "dog", and that has two columns:

    title (text): The name of a movie
    character (text): The name of the dog character
A single movie may appear multiple times if it has multiple dog characters.

Hint:
    
    SELECT _____, _____
    FROM _____ JOIN _____ ON _____
    WHERE ____ LIKE "%dog%";
Use FROM, JOIN, and ON to combine the information in the titles and principals tables.
Use WHERE to select only characters that include "dog".
Use SELECT to put the movie title and character in the output.


## Q3: Leads of Leads

Create a leads table that has two columns:

name (text): The name of an actor
lead_roles (integer): The number of movies that the actor has been the lead in
You can find lead roles by looking in the principals table for rows with ordering set to 1. Only select actors who have been the lead in more than 10 movies.

Hint:
  
    SELECT ____, ____ AS lead_roles
    FROM ____ JOIN ____ ON ____ -- ON后面为两表连接的条件
    WHERE ____
    GROUP BY names.nconst
    HAVING count(*) > 10;
Use FROM and ON to combine the information in the principals and names tables.
Use WHERE to select only lead roles.
Use GROUP BY to create a single row for each person.
Use HAVING to output only people who had more than 10 lead roles.
Use SELECT to put the person's name and the count of their roles in the output.

解题思路：找出主演电影数目最多的10个演员

    第一步是要组合表格，一张表根本不能一次性找到所有信息。
    主演：principals中 ordering=1 的演员

## Q4: Long Movies

Create a long_movies table that contains the number of movies in each decade that are over 3 hours long.
long_movies has two columns:

    decade (strings): The decade, e.g., 1920s
    count (numbers): The number of movies in that decade that are over 3 hours (180 minutes) long

SQL的`/`似乎就是整除
When adding numbers and including the result in a string, put parentheses around the arithmetic, e.g., Be careful with the string concatenation!
    
    sqlite> SELECT (192 * 10) || "s";
    1920s

Hint:

    SELECT ____ AS decade, ____ AS count
    FROM ____
    WHERE ____
    GROUP BY ____;
Use FROM and WHERE to choose only the movies with runtime greater than 180 minutes.
Use GROUP BY to group together all of the movies for one decade.
Use SELECT to create a string like 1920s for each decade, and to select the count of movies for each decade.