#Created by Nacho Rodriguez-Cortes (rodriguezn@carleton.edu)
#IMPORT QUESTION TO CONSIDER: do I need to load output_file, then input_file?
#If not, then I can open input file, and write to different input files while on# a certain row

import csv

def process_athletes(reader):
  rows_to_write = []
  set_ids = set()
  for row in reader:
    id = int(row[0])
    names = row[1]
    sex = row[2]
    team = row[6]
    
    #Try/Except to account for the 'N/A' data in height, weight, and age rows
    try:
      age = int(row[3])
    except:
      age = None
    try:
      height = int(row[4])
    except:
      height = None
    try:
      weight = int(row[5])
    except:
      weight = None

    medals = row[14]
    if medals != 'NA':
      total_medals = 1
    else:
      total_medals = 0
    
    if id in set_ids:
      for each_row in rows_to_write:
        duplicate_id = each_row[0]
        new_age = each_row[3]
        new_medals = each_row[7]
        if duplicate_id == id:
          new_age = age
          new_medals += 1
    else:
      set_ids.add(id)
      rows_to_write.append([id, names, sex, age, height, weight, team, total_medals])
  return rows_to_write

def process_teams(reader):
  rows_to_write = []
  set_ids = set()
  id = 1
  for row in reader:
    name = row[6]
    medal = row[14]
    if medal == "Gold":
      gold_medals = 1
      silver_medals = 0
      bronze_medals = 0
      total_medals = 1
    elif medal == "Silver":
      gold_medals = 0
      silver_medals = 1
      bronze_medals = 0
      total_medals = 1
    elif medal == "Bronze":
      gold_medals = 0
      silver_medals = 0
      bronze_medals = 1
      total_medals = 1
    else:
      gold_medals = 0
      silver_medals = 0
      bronze_medals = 0
      total_medals = 0
    
    if id in set_ids:
      for each_row in rows_to_write:
        duplicate_id = each_row[0]
        gold_count = each_row[2]
        silver_count = each_row[3]
        bronze_count = each_row[4]
        total_count = each_row[5]
        if duplicate_id == id:
          gold_count += gold_medals
          silver_count += silver_medals
          bronze_count += bronze_medals
          total_count += total_medals
    else:
      set_ids.add(id)
      rows_to_write.append([id, name, gold_medals, silver_medals, bronze_medals, total_medals])
      id += 1
  return rows_to_write



# def process_regions(reader, writer):



def main():
  with open('athletes.csv', newline='') as output_file, open('athlete_events.csv', newline='') as input_file:
    reader = csv.reader(input_file, delimiter=',')
    writer = csv.writer(output_file, delimiter=',')
    next(reader)
    processed_reader = process_athletes(reader)
    print("Processed!")
    for row in processed_reader:
      writer.writerow(row)

if __name__ == "__main__":
  main()

#with open('teams.csv', newline='') as output_file:
#  with open('athlete_events.csv', newline='') as input_file:
#    reader = csv.reader(input_file, delimiter=',')
#    writer = csv.writer(output_file, delimiter=',')
#    # not sure what I should be doing with the id
#    teams_id = 0
#    for row in reader:     
#      id = teams_id
#      name = row[6]
            
