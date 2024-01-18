The project is used to retrieve data from nasa open api from endpoints 
- GET: /nasa/picture_of_the_day/
- POST: /nasa/interplanetary_shock/
 - GET/PUT/DELETE: /nasa/interplanetary_shock/<int:pk>/

Initially you need to get your secret key from nasa here "https://api.nasa.gov/" and pass it to the NASA_SECRET_KEY variable in the .env file.

Now you can retrieve the data 
Example:
- GET: /nasa/picture_of_the_day/
Request Body:
- None
  
Example:
- POST: /nasa/interplanetary_shock/
Request Body:
  {
    "start_date": "2022-01-01",
    "end_date": "2023-01-10"
  }
Example:
- GET/PUT/DELETE: /nasa/interplanetary_shock/<int:pk>/
Request Body:
- None

Use
 - GET/PUT/DELETE: /nasa/interplanetary_shock/1/ 
endpoint is possible only after a request to 
- POST: /nasa/interplanetary_shock/
has been made.
Because the data is stored in a local variable