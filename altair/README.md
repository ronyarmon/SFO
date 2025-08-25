# SFO
Analysis of customer sureveys conducted by the San Francisco Airport (2010-2017)

"SFO conducts a yearly comprehensive survey of our guests to gauge satisfaction with our facilities, services, and amenities. SFO compares results to previous surveys to look for areas of improvement and discover elements of the guest experience that are not satisfactory."

Source: San Francisco DATA portal (DATA SF)
https://data.sfgov.org/browse?q=SFO%20Customer%20Survey&anonymous=true&sortBy=relevance  

Columns: Rating of airport services by guets.
Ratings scale: 1 (unacceptable),2,3,4,5 (outstanding).   
Excluded from the analyiss: 6=Have never used or visited / Not applicable, 0=Blank.
Thus, the results are in relation to the guests who used or were assisted by the serivces asked about, rather than 
the survey respondents as a whole. 
    
Questions (2016 Codes):
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

Data cleaning and preparation: data_preparation.ipynb
Python tools: 
    Jupyter widgets (drop down menus): https://ipywidgets.readthedocs.io/en/latest/index.html
    altair (visualization): https://altair-viz.github.io/

Survey results and charts can be pulled as: 
  Specific question, all years (select_question.ipynb). 
  All questions for specific year (select_year.ipynb).

¡¡¡¡¡¡
Both scripts run well locally but not on GitHub where I'm getting the CParserError: Error tokenizing data. If you have any idea why please let me know. I'm raising a question on stack and hope it will be sorted out soon.
