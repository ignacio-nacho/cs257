'''
Created by Nacho Rodriguez-Cortes (rodriguezn@carleton.edu)
'''

import csv

def process_athletes(reader):
  '''
  creates a row for each athlete, while using duplicated rows to update values such as age and medals
  '''
  rows_to_write = {}
  for row in reader:
    id = int(row[0])
    names = row[1]
    sex = row[2]
    age = row[3]
    height = row[4]
    weight = row[5]
    team = row[6]
    
    if age == 'NA':
      age = 'NULL'
    if height == 'NA':
      height = 'NULL'
    if weight == 'NA':
      weight = 'NULL'
    
    medals = row[14]
    if medals != 'NA':
      total_medals = 1
    else:
      total_medals = 0
    
    if id in rows_to_write:
      values = rows_to_write.pop(id)
      new_age = values[3]
      new_medals = values[7]
      new_age = age
      new_medals += 1
      rows_to_write[id] = [id, names, sex, new_age, height, weight, team, new_medals]
    else:
      rows_to_write[id] = [id, names, sex, age, height, weight, team, total_medals]
  return rows_to_write

def process_teams(reader):
  '''
  creates a row for each team, along with its medal statistics and noc
  '''
  rows_to_write = {}
  id = 1
  for row in reader:
    name = row[6]
    noc = row[7]
    medal = row[14]
    if medal == "Gold":
      bronze_medals = 0
      silver_medals = 0
      gold_medals = 1
      total_medals = 1
    elif medal == "Silver":
      bronze_medals = 0
      silver_medals = 1
      gold_medals = 0
      total_medals = 1
    elif medal == "Bronze":
      bronze_medals = 1
      silver_medals = 0
      gold_medals = 0
      total_medals = 1
    else:
      bronze_medals = 0
      silver_medals = 0
      gold_medals = 0
      total_medals = 0
    if name in rows_to_write:
      values = rows_to_write.pop(name)
      old_id = values[0]
      bronze_count = values[3]
      silver_count = values[4]
      gold_count = values[5]
      total_count = values[6]
      bronze_count += bronze_medals
      silver_count += silver_medals
      gold_count += gold_medals
      total_count += total_medals
      rows_to_write[name] = [old_id, noc, name, bronze_count, silver_count, gold_count, total_count]
    else:
      rows_to_write[name] = [id, noc, name, bronze_medals, silver_medals, gold_medals, total_medals]
      id += 1
  return rows_to_write



def process_nocs(reader):
  '''
  creates a row for each noc with its region
  '''
  rows_to_write = {}
  id = 1
  for row in reader:
    noc = row[0]
    region = row[1]
    rows_to_write[noc] = [id, noc, region]
    id += 1
  return rows_to_write

def process_games(reader):
  '''
  creates a row for each olympic game in dataset
  '''
  rows_to_write = {}
  id = 1
  for row in reader:
    game = row[8]
    year = row[9]
    season = row[10]
    city = row[11]
    if game not in rows_to_write:
      rows_to_write[game] = [id, city, season, year]
      id += 1
  return rows_to_write

def process_athletes_medals(reader):
  '''
  creates a row containg each athletes medals with its corresponding game and event information
  '''
  rows_to_write = {}
  id = 1
  for row in reader:
    athletes_id = row[0]
    year = row[9]
    season = row[10]
    event = row[13]
    medal_type = row[14]
    if medal_type != 'NA':
      rows_to_write[id] = [id, athletes_id, season, year, event, medal_type]
      id += 1
  return rows_to_write

def main():
  with open('athlete_events.csv', 'r', newline='') as input_file, open('athletes.csv', 'w') as output_file:
    reader = csv.reader(input_file, delimiter=',')
    writer = csv.writer(output_file, delimiter=',')
    next(reader)
    processed_athletes = process_athletes(reader)
    for key in processed_athletes:
      value = processed_athletes.get(key)
      writer.writerow(value)

  with open('athlete_events.csv', 'r', newline='') as input_file, open('teams.csv', 'w') as output_file:
    reader = csv.reader(input_file, delimiter=',')
    writer = csv.writer(output_file, delimiter=',')
    next(reader)
    processed_teams = process_teams(reader)   
    for key in processed_teams:
      value = processed_teams.get(key)
      writer.writerow(value)
 
  with open('noc_regions.csv', 'r', newline='') as input_file, open('nocs.csv', 'w') as output_file:
    reader = csv.reader(input_file, delimiter=',')
    writer = csv.writer(output_file, delimiter=',')
    next(reader)
    processed_nocs = process_nocs(reader)   
    for key in processed_nocs:
      value = processed_nocs.get(key)
      writer.writerow(value)

  with open('athlete_events.csv', 'r', newline='') as input_file, open('games.csv', 'w') as output_file:
    reader = csv.reader(input_file, delimiter=',')
    writer = csv.writer(output_file, delimiter=',')
    next(reader)
    processed_games = process_games(reader)   
    for key in processed_games:
      value = processed_games.get(key)
      writer.writerow(value)
 
  with open('athlete_events.csv', 'r', newline='') as input_file, open('athletes_medals.csv', 'w') as output_file:
    reader = csv.reader(input_file, delimiter=',')
    writer = csv.writer(output_file, delimiter=',')
    next(reader)
    processed_athletes_medals = process_athletes_medals(reader)   
    for key in processed_athletes_medals:
      value = processed_athletes_medals.get(key)
      writer.writerow(value)

if __name__ == "__main__":
  main()

            
