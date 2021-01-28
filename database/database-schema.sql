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
  name text,
  gold_medals integer,
  silver_medals integer,
  bronze_medals integer,
  total_medals integer
);

CREATE TABLE noc_regions (
  id integer,
  noc text,
  region text
); 

CREATE TABLE games (
  id integer,
  year integer,
  season text,
  city text
);

CREATE TABLE events (
  id integer,
  games_id integer,
  sport text
);    
