# import RPi.GPIO as GPIO
from MacScanner import getMacAddresses

#todo: different entery, exit funcs with continuous scanning

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(4, GPIO.OUT)
# GPIO.setup(5, GPIO.OUT)

# macAddressToPersonDict = {'3C:7A:8A:F3:DB:F7':'anand', 'AC:FD:CE:00:D2:87':'vijay', '7C:DD:90:B0:49:CB':'rushi', 'randVal':'karan'}
currentScanMacAddresses = getMacAddresses()

peopleInfo = [{'id':0, 'mac':'3C:7A:8A:F3:DB:F7', 'device':'Arris Group', 'person':'anand'},
              {'id': 1, 'mac': 'AC:FD:CE:00:D2:87', 'device': 'Intel Corporate', 'person': 'vijay'},
              {'id': 2, 'mac': 'asfasf', 'device': 'Intel asfa', 'person': 'rushi'}]

# list of dictionaries, each dict has keys id, mac, device, person
# givin mac address

suspicious = []
macFound = False

# def anandEnter():
#     GPIO.output(4, True)    # red led
#
# def anandExit():
#     GPIO.output(4, False)    # red led
#
# def vijayEnter():
#     GPIO.output(5, True)    # green led
#
# def vijayExit():
#     GPIO.output(5, False)    # green led

# def actionMac(mac):
#     for personInfo in peopleInfo:
#         if personInfo[mac] in currentScanMacAddresses:
#             if personInfo['person'] == 'anand': anandEnter()
#             elif personInfo['person'] == 'vijay': vijayEnter()
#         else:
#             if personInfo['person'] == 'anand': anandExit()
#             elif personInfo['person'] == 'vijay': vijayExit()

#todo: check for intruders




def processPresentMacs(presentMacs):
    print("running tasks for:")
    for mac in presentMacs:
        print(mac)
    return



# while True:
#     for macAddress in currentScanMacAddresses:
#         for personInfo in peopleInfo:
#             if personInfo['mac'] == macAddress:
#                 if personInfo['person'] == 'anand': anandEnter()
#                 elif personInfo['person'] == 'vijay': vijayEnter()
#                 macFound = True
#         if not macFound:
#             suspicious.append(macAddress)