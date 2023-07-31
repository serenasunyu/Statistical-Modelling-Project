# Final-Project-Statistical-Modelling-with-Python

## Project/Goals
Retrieve data from CityBikes, Foursquare and Yelp APIs. Combine all the data together,  build a model and analyze the result to find out the relations between the number of bikes and the number of bars or restaurants (POI). 

## Process
### Connecting to CityBikes API
#### Send a request to retrieve all available bike stations in a particular city, Hamilton in this project
#### Parse the Json object into a Pandas dataframe
### Connecting to Foursquare API
#### Retrieve all restaurants near the selected location
### Connecting to Yelp API
#### Retrieve all restaurants near the selected location
### Compare the quality of the YELP and Foursquare API
### Joining data from the above to create a dataframe
#### Use data visualization to explore the data
#### Create my own SQLite database and store the data collected on the POIs
### Building a regression model using Python's statsmodels module that demonstrates a relationship between the number of bikes in a particular location and the characteristics of the POIs in that location


## Results
There is a statistically significant positive relationship between th enumber of nearby bars and the number of bikes (p_value = 0.013). As the number of bars increases, the number of bikes tends to increase as well (coef = 2.8927). However, it is only about 20.7% of variance in number of bikes can be explained by the number of nearby bars (R-squared = 0.207), this means there are likely other factors affecting the number of bikes which are not included in the model.

## Challenges 
Combine the data together to get number of POIs is challenge. Also, the classification in different APIs is different, it gives me a bit difficult to get the data.

## Future Goals
There is a huge different between the data collected from Yelp API and the data collected from Foursquare API. I will look for more data to explore the reasons behind that. ALso, collect more data to analyze through the model. 
