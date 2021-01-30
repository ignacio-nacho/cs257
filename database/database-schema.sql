CREATE TABLE athletes (
  id integer,
  names text,
  sex text,
  age integer,
  height integer,
  weight integer,
  team text,
  total_medals integer
);

CREATE TABLE teams (    
  id integer,
  noc text,
  name text,
  bronze_medals integer,
  silver_medals integer,
  gold_medals integer,
  total_medals integer
);

CREATE TABLE nocs (
  id integer,
  noc text,
  region text
); 

CREATE TABLE games (
  id integer,
  city text,
  season text,
  year integer
);

CREATE TABLE athletes_medals (
  id integer,
  athletes_id integer,
  season text,
  year integer,
  event text,
  medal_type text
);
