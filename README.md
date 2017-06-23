# state-capital-analysis

### Hypotheses

1. The further west you travel, the state capital will be closer to the geographic center of the state.
2. The year each state was founded (or capital moved) correlates to the distance between points.


### Step / Methods / Libraries
1. Collect data for States, Geographic Center, Capital Center, Area, etc...
2. Write a script to calculate the distance between the two coordinates
3. Control for size (area) of each state
4. Create a dashboard showing the above hypotheses


geopy - Python library to calculate distance between geo coordinates

vincenty method - Method for calculating the distance (Thaddeus Vincenty, 1975)


### Sources
Data for geographic centers calculated by the USGS (U.S. Geological Survey)