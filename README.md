                           Title: Profitable Trip planning Assistant from New York 

Aim of the project:

  The aim of this project is to provide user a quick and handy information about the destination they dream to visit and to make their planning profitable.

Abstract:
    
   In this project I have created a web application that quickly provide an overall idea about the destination the user plans to visit anywhere in the world from New York having direct flights. The application would provide information about weather, closest airports and cheapest air fares for destination. Based on the airfares the user could decide their vacation destination as per their budget. Also with the knowledge of weather they could plan their activity during the vaction.


Input from the user:
    
    Destination: where to go
    Travel start date : departure date 
    Travel End date : arrival date
    
Output:
   
    Weather condition of the destination
    Closest Airports and city
    Current air fares for the direct flights 
    

Directory Structure:

    |__mysite               # Django Project created called "mysite"
       |__kunju             # Application created inside Django Project
          |__ __pycache__
          |__ migrations
          |__ templates
          |__ tests
          |__ admin.py
          |__ air.py
          |__ apps.py
          |__ forms.py
          |__ 
       |__manage.py 
       |__test
       |__mysite
          |__ __init__.py
          |__ __pycache__
          |__ settings.py
          |__ urls.py
          |__ wsgi.py
    |__README.md
    
    
    


How this works:
    
    Used Django framework to create web application for travel recommendation
    Used Django forms to get user input - Location, Date range
    Used weather API to obtain temperatures for the given date range
    Used flight API to identify closest airports to the destination  
    Also check for the cheapest flight available for the travel period
    
Motivation:
    Most of us love travelling, whenever we begin to plan a vacation, the main thing we would consider is how much the trip would cost and how satisfactory our trip would be, if we travel in particular period of the year. Because psycologically season and weather has effects on travel related mood and travel satisfaction[1]. So here I took two parameters such as weather and air fare mainly to get a basic idea before planning a trip.


Future Enhancement:
    
    We could enhance the project by simulating various models for forecasting the future air fares and classifying whether to buy or wait for the reduction in air ticket fare based on historical trends. Also add auto complete options for search locations and provide flight details for destinations with multiple hops.
    
References:
[1]. https://www.frontiersin.org/articles/10.3389/fpsyg.2017.00140/full
[2]. https://www.djangoproject.com/
[3]. https://pypi.org/project/amadeus/
[4]. https://darksky.net/dev
[5]. https://tempusdominus.github.io/bootstrap-4/

  
