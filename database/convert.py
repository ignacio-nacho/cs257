#Created by Nacho Rodriguez-Cortes (rodriguezn@carleton.edu)

with open('athlete_events.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',',quotechar='|')
    next(reader)
    for row in reader:

        ID = int(row[0])
        names = row[1]
        sex = row[2]
        age = int(row[3])
        height = int(row[4])
        weight = int(row[5])
        team = row[6]

