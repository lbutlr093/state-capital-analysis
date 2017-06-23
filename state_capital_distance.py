## Takes the geo coordinates from the center of the state,
## and from the state capital and uses the Vincenty method
## to get the distance (miles) between them. 

## pip install geopy

from geopy.distance import vincenty
import csv

distance_file = open('Center_of_State_with_Distance.csv', 'wb')
writer = csv.writer(distance_file)

with open('Center_of_States.csv', 'rb') as f:
	reader = csv.reader(f)
	header = next(reader)
	header.append('Distance Between (miles)')		# Header for new column
	writer.writerow(header)
	for line in reader:
		# If line is blank, do something
		coords1 = line[2].split(', ')				# Break coordinates 
		coords2 = line[4].split(', ')				# into (lat, long)
		capital_coords = (float(coords1[0]), float(coords1[1]))
		center_coords = (float(coords2[0]), float(coords2[1]))
		distance = vincenty(capital_coords, center_coords).miles
		distance = "{0:.2f}".format(distance)		# Round to 2 decimal places
		line.append(distance)
		writer.writerow(line)
distance_file.close()