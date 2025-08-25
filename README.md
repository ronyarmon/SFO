# SFO
Analysis of customer sureveys conducted by the San Francisco Airport (2010-2017)

"SFO conducts a yearly comprehensive survey of our guests to gauge satisfaction with our facilities, services, and amenities. SFO compares results to previous surveys to look for areas of improvement and discover elements of the guest experience that are not satisfactory."

Source: San Francisco DATA portal (DATA SF)
https://data.sfgov.org/browse?q=SFO%20Customer%20Survey&anonymous=true&sortBy=relevance  


# Columns
## Rating of airport services by guets  
### Questions:  
Q7ART Artwork and exhibitions
Q7FOOD Restaurants
Q7STORE Retail shops and concessions
Q7SIGN Signs and directions inside SFO
Q7WALKWAYS Escalators/Elevators/Moving walkways
Q7SCREENS Information on screens/monitors
Q7INFODOWN Information booths (lower level - near baggage claim)
Q7INFOUP Information booths (upper level - departure area)
Q7WIFI Accessing and using free WiFi at SFO
Q7ROADS Signs and directions on SFO airport roadways
Q7PARK Airport parking facilities
Q7AIRTRAIN AirTrain
Q7LTPARKING Long term parking lot shuttle (bus ride)
Q7RENTAL Airport Rental Car Center
Q7ALL SFO Airport as a whole  
### Ratings:  
1 (unacceptable),2,3,4,5 (outstanding).   
6=Have never used or visited / Not applicable, 0=Blank.  
## Respondent demography  
### Questions & Ratings: 
Gender  
Non-Binary is added only in 2018, Other used in some datasets but removed since the focus was on comparing males and females 
Age for 2016 includes values related to specific ages: 'Under 20', 'Under 23', 'Under 25', 'Under 27', 'Under 28', 'Under 30', 'Under 32', 'Under 18', 'Under 19', 'Under 21', 'Under 22', 'Under 24', 'Under 26', 'Under 29', 'Under 31'. They were introduced under the most suitable groupings: 'Under 20' in '18-24', 'under 27' in '25-34' etc
For all demographic questions:   
Blank may indicate an answer left blank or given multiple responses (In questionnaire: Blank/Multiple responses) and cases of Don’t know/Refused or 'Other Currency' in income  


Variables exploration: explore directory  
Data cleaning and preparation: data/build.py  
Dashboard data: data/dataset.xlsx  

