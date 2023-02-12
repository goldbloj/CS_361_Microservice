# CS_361_Microservice
# CS_361_Microservice_Planet

**** Communication Contract ****

To REQUEST data from the microservice you implemented. 

Data is requested by running **client.py** and choosing a number that corresponds to a specific planet type. That information will be stored as user_choice_number which then stores the planet in a "planet" variable. A socket is created via zeroMQ and connected to by **client.py** The request is then sent to **server.py**, a request to access the JSON object that matches the planet variable. A validation message that includes the specific type of planet requested by the user is also displayed. 

Example call:
python client.py
Hi user. Press "1" to generate a new planet: 1 
         1. alpine
         2. gaseous
         3. icy
         4. martian
         5. savannah
         6. swamp
         7. terrestrial
         8. tropical
         9. volcanic
Choose the type of planet via its corresponding number
from the list above and hit "Enter": 8
Sending request 0 …
You chose a(n) tropical planet

To RECIEVE data from the microservice you implemented.

Data is received by running **server.py**, which will then create a socket that matches one created by **client.py** via zeroMQ. Receiving the information sent from **client.py**, **server.py** will verify the request sent for a specific type of planet. **server.py** will open a database.json file, locate the planet type requested and construct a new JSON object using random characteristics from the specified type of planet. That JSON object will be packaged and sent back to the **client.py**. packaged  will   

Example call:

Received request for planet type: b'tropical'

Sending back:
{'type': 'tropical', 'texture': 'tropical1.bmp', 'atmosphere': 'mostly nitrogen', 'system': 'Proxima Centauri', 'size': 27849, 'moons': 8}
