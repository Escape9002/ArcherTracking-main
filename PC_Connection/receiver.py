import asyncio
from bleak import BleakScanner
from bleak import BleakClient

async def quickTest():
    devices = await BleakScanner.discover()
    device = None

    for d in devices:
        print("name: {} | address: {} | rssi: {} ".format(d.name, d.rssi, d.address))
        if d.name == "MPU9250":
            device = d
            break
    
    async with BleakClient(device.address) as client:
        value = await client.read_gatt_char("d6b78de4-40c7-11eb-b378-0242ac130002")
        print("received value: {}".format(value))

async def scan():
    devices = await BleakScanner.discover()
    print("Found Devices: ")
    for d in devices:
        if d.name != None:
            print("    name: {} | address: {} | rssi: {} ".format(d.name, d.rssi, d.address))
    return devices

async def connect(address, service):
    async with BleakClient(address) as client:
        
        while client.is_connected == False:
            client.connect()
            

def lol()
    return True

while !lol():
    print(" ")
##################################################
########## THE REAL PROGRAMM #####################
##################################################

# asyncio.run(quickTest())

found_devices = asyncio.run(scan())

address = ""
service = "d6b78de4-40c7-11eb-b378-0242ac130002"

chosen_device = input("enter devices name: ")
for d in found_devices:
    if d.name == chosen_device:
        print("Chose: name: {} | address: {} | rssi: {} ".format(d.name, d.rssi, d.address))
        address = d.address

asyncio.run(connect(address, service))


