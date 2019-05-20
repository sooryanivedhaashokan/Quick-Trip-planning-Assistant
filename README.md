                           Title: Quick Trip planning Assistant from New York 

Aim of the project:

  The aim of this project is to provide user a quick and handy information about the destination they dream to visit and to make their planning profitable.

Abstract:
    
   In this project I have created a web application that quickly provide an overall idea about the destination the user plans to visit anywhere in the world from New York having direct flights. The application would provide information about weather, closest airports and cheapest air fares for destination with no layover or hops. Based on the airfares the user could decide their vacation destination as per their budget with minimum travel time. Also with the knowledge of weather they could plan their activity during the vaction.


Input from the user:
Note: Please enter the correct spelling for the Location. Auto complete feature is not implemented yet   
    
    Destination: where to go
    Travel start date : departure date 
    Travel End date : arrival date
    
Output:
   
    Weather condition of the destination
    Closest Airports and city
    Current air fares for the direct flights, if there is no direct flights then displays Nothing
    

Directory Structure:

    |__mysite               # Django Project created called "mysite"
       |__kunju             # Application created inside Django Project
          |__ migrations
          |__ templates
          |__ tests
              |__ test.py   # Test command: (Top) cd mysite , $python3 -m unittest kunju/tests/test.py
              |__ test_air.py
              |__ test_flight.py
              |__ test_geolocate.py
              |__ test_weather.py
          |__ air.py
          |__ apps.py
          |__ flight.py
          |__ forms.py
          |__ geolocate.py
          |__ urls.py
          |__ views.py
          |__ weather.py
          |__ widgets.py
       |__ manage.py 
       |__ requiement.txt    # contains all the required installation to access the application 
       |__ test               # Executable file for quick testing of the application
       |__ mysite             # Django Project created called "mysite", folder contains required file for project to run
          |__ settings.py
          |__ urls.py
          |__ wsgi.py
    |__README.md
    
How to Test:
   
    cd mysite(Top)
    Run the executable file "./test" (if not open this file and run each command individually)
    Then start the server by clicking the link on the terminal
    Example:
        Starting development server at http://127.0.0.1:8000/

How this works:
    
    Used Django 2.1.7 framework to create web application for travel recommendation
    Used Django forms to get user input - Location, Date range
    Used weather API to obtain temperatures for the given date range
    Used flight API to identify closest airports to the destination  
    Also check for the cheapest flight available for the travel period
    
Motivation:
    Most of us love travelling, whenever we begin to plan a vacation, the main thing we would consider is how much the trip would cost and how satisfactory our trip would be, if we travel in particular period of the year. Because psycologically season and weather has effects on travel related mood and travel satisfaction[1]. So here I took two parameters such as weather and air fare mainly to get a basic idea before planning a trip.


Future Enhancement:
    
    We could enhance the project by simulating various models for forecasting the future air fares and classifying whether to buy or wait for the reduction in air ticket fare based on historical trends. 
    
References:
[1]. https://www.frontiersin.org/articles/10.3389/fpsyg.2017.00140/full
[2]. https://www.djangoproject.com/
[3]. https://pypi.org/project/amadeus/
[4]. https://darksky.net/dev
[5]. https://tempusdominus.github.io/bootstrap-4/

  
