## Takes the geo coordinates from the center of the state,
## and from the state capital and uses the Vincenty method
## to get the distance (miles) between them. 

## pip install geopy

from geopy.distance import vincenty
import csv
import math

distance_file = open('Center_of_State_with_Distance.csv', 'wb')
writer = csv.writer(distance_file)

with open('Center_of_States.csv', 'rb') as f:
	reader = csv.reader(f)
	header = next(reader)
	header.extend(('Distance Between (miles)', 'Area to Distance Ratio'))		# Header for new columns
	writer.writerow(header)
	for line in reader:
		# TODO: if line is blank, do something
		coords1 = line[2].split(', ')					# Break coordinates 
		coords2 = line[4].split(', ')					# into (lat, long)
		capital_coords = (float(coords1[0]), float(coords1[1]))
		center_coords = (float(coords2[0]), float(coords2[1]))
		distance = vincenty(capital_coords, center_coords).miles
		ratio = math.log10(float(line[6]) / distance) 		# Calculate before rounding distance
		distance = "{0:.2f}".format(distance)			# Round to 2 decimal places
		ratio = "{0:.2f}".format(ratio)
		line.extend((distance, ratio))
		writer.writerow(line)
distance_file.close()