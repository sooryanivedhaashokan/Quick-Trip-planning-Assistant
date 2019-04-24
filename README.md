                           Title: Profitable Trip planning Assistant from New York to Anywhere


Aim of the project:

  The aim of this project is to provide the user a quick and handy information about the destination they dream to visit and to make their planning profitable.

Abstract:
    
   In this project I have created a web application that quickly provide an overall idea about the destination the user plans to visit anywhere in the world from New York. The application would provide information about weather, closest airports and cheapest air fares. Based on the airfares the user could decide their vacation destination as per their budget. Also with the knowledge of weather they could plan their activity during the vaction.


Input from the user:
    
    Destination: where to go
    Travel start date : departure date 
    Travel End date : arrival date
    
Output:
   
    Weather condition of the destination
    Current air fares if you book air ticket immediately
    
How this works:
    
    Used Django framework to create web application for travel recommendation
    Used Django forms to get user input - Location, Date range
    Used weather API to obtain temperatures for the given date range
    Used flight API to identify closest airports to the destination  
    Also check for the cheapest flight available for the travel period

Future Enhancement:
    
    We could enhance the project by simulating various models for forecasting the future air fares and classifying whether to buy or wait for the reduction in air ticket fare based on historical trends.
  
