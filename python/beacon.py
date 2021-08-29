import time
import serial

def getBeacons(ser: serial.Serial):
    beacons = []

    ser.write(b'S')
    res = b''

    while True:
        res += ser.read(ser.inWaiting())
        time.sleep(0.01)

        if res.endswith(b'OK+DISCE\r\n'):
            break
    
    for line in res.split(b'\r\n'):
        if line == b'OK+DISCS':
            continue
        elif line == b'OK+DISCE':
            break
        else:
            temp = line.decode('ascii').split(':')

            if temp[0] != 'OK+DISC':
                continue

            factory_id = temp[1]
            uuid = temp[2]
            identifier = temp[3]
            mac = temp[4]
            rssi = int(temp[5])

            beacons.append({
                'factory_id': factory_id, 
                'uuid': uuid, 
                'identifier': identifier, 
                'mac': mac, 
                'rssi': rssi
            })

    return beacons

def getDistance(power: int, rssi: int, n: int):
    return 10 ** ((power - rssi) / (10 * n))

def getBeaconId(factory_id: str, uuid: str, identifier: str, mac: str):
    return f'{factory_id}:{uuid}:{identifier}:{mac}'

def feedback(ser: serial.Serial):
    ser.write(b'F')