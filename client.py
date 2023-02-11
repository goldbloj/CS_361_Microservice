import zmq
import time
planet = None

context = zmq.Context()
user_start_number = input("""Hi user. Press "1" to generate a new planet: """)
print("""         1. alpine
         2. gaseous
         3. icy
         4. martian
         5. savannah
         6. swamp
         7. terrestrial
         8. tropical
         9. volcanic""")
print()
user_choice_number = input("""Choose the type of planet via its corresponding number
from the list above and hit "Enter" """)

match user_choice_number:
    case "1":
        planet = "alpine"
    case "2":
        planet = "gaseous"
    case "3":
        planet = "icy"
    case "4":
        planet = "martian"
    case "5":
        planet = "savannah"
    case "6":
        planet = "swamp"
    case "7":
        planet = "terrestrial"
    case "8":
        planet = "tropical"
    case "9":
        planet = "volcanic"

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


#  Do 10 requests, waiting each time for a response
for request in range(1):
    print("Sending request %s …" % request)
    # socket.send(planet)
    print("You chose a(n) " + planet + " planet")
    socket.send(bytes(planet, encoding='utf-8'))
    print()

    time.sleep(20)

    #  Get the reply
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
    print()
    print(message)
