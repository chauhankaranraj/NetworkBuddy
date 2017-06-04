# ver 1.0
import os
import re
# import subprocess

def getMacAddresses():
    os.system('chmod +x scan_script.sh')
    os.system('sudo ./scan_script.sh')

    macAddresses = []
    with open('scan_results.txt', 'r') as outputFile:
        for line in outputFile:
            if (line[0:3] == "MAC"):
                # print(line.split()[2]+" "+ re.search(r'\((.*?)\)',line).group(1))
                macAddresses.append(line.split()[2]+" "+ re.search(r'\((.*?)\)',line).group(1))

    return macAddresses

# timestamp,

# print(getMacAddresses())

# os.getenv("SUDO_USER")

# os.system('./scan_script.sh')

# result = subprocess.run(['nmap', '-sn', '192.168.0.1/24'], stdout=subprocess.PIPE)
# print(result.stdout.decode('utf-8'))


# sudo


# result = subprocess.run(['sudo','nmap', '-sn', '192.168.0.1/24'], stdout=subprocess.PIPE)
# # print(result.stdout.decode('utf-8'))
# output = result.stdout.decode('utf-8').split()
#
# # i=0
# # for item in result.stdout.decode('utf-8').split():
# #     print("item is " + str(i) +" " +item)
# #     i+=1
# ipAddresses = []
# for index in range(4, len(output), 10):
#     ipAddresses.append(output[index])
#
# macAddresses = []
# for index in range(len(output)):
#     macAddresses.append(output[index])




# sudo nmap -sn 192.168.0.1/24