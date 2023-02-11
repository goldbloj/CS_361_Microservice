import json
import time
import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request for planet type: %s" % message)
    f = open('database.json')
    data = json.load(f)
    request_planet = None
    for i in data['type']:
        type_planet = i
        if type_planet in str(message):
            request_planet = type_planet
    atmosphere = random.choice(data["type"][request_planet]['atmosphere'])
    texture = random.choice(data["type"][request_planet]['texture'])
    system = random.choice(data["type"][request_planet]['system'])
    size = random.randrange(3000, 100000)
    number_of_moons = random.randrange(0, 20)
    your_planet = {'type': request_planet, 'texture': texture, 'atmosphere': atmosphere, 'system': system, 'size': size, 'moons':number_of_moons }

    print()
    print("Sending back:")
    print(your_planet)

    your_planet_string = str(your_planet)
    f.close()

    #  Do some 'work'
    time.sleep(5)

    #  Send reply back to client
    socket.send(bytes(your_planet_string, encoding='utf-8'))




