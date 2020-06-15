import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'david', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_mac_address_table()
print (json.dumps(ios_output, sort_keys=True, indent=4))

iosvl2.close()

# Example 2 of napalm bgp functions

bgplist = ['192.168.10.1',
           '192.168.10.2',
           '192.168.10.3']

for ip_address in bgplist:
    print("Connecting to" + str(ip_address))
    driver = get_network_driver('ios')
iosv_router = driver(ip_address, 'david', 'cisco')
iosv_router.open()
ios_output2 = iosv_router.get_bgp_neighbors()
print(json.dumps(ios_output2, indent=4))
iosv_router.close()
