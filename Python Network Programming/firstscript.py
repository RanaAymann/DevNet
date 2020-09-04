# SSH to Ubuntu VM
# Netmiko
! on linux terminal
#sudo apt install python3-pip
#sudo pip3 install -U netmiko

! Create Python Script , to Access a router (SSH) running on the states.
#nano pthon1.py

#!/usr/bin/env python
from netmiko import ConnectHandler
nx_os = {
'device_type': 'cisco_ios',
'ip': 'sbx-nxos-mgmt.cisco.com',
'username': 'admin',
'password': 'Admin_1234!',
'port': 8181
}
net_connect = ConnectHandler(**nx_os)
output = net_connect.send_command('show ip int brief')
print(output)

#exit
#python3 python1.py
 
! print JSON Output :

#!/usr/bin/env python
from netmiko import ConnectHandler
nx_os = {
'device_type': 'cisco_ios',
'ip': 'sbx-nxos-mgmt.cisco.com',
'username': 'admin',
'password': 'Admin_1234!',
'port': 8181
}
net_connect = ConnectHandler(**nx_os)
output = net_connect.send_command('show ip int brief | json-pretty')
print(output)

! Find some data:

#!/usr/bin/env python
from netmiko import ConnectHandler
import json
nx_os = {
'device_type': 'cisco_ios',
'ip': 'sbx-nxos-mgmt.cisco.com',
'username': 'admin',
'password': 'Admin_1234!',
'port': 8181
}
net_connect = ConnectHandler(**nx_os)
output = net_connect.send_command('show ip int brief | json-pretty')
json_data = json.loads(output)
print(json_data['TABLE_intf']['ROW_intf'][0]['intf-name'])
print(json_data['TABLE_intf']['ROW_intf'][0]['prefix'])

!  Use a loop to find IP addresses :
#!/usr/bin/env python
from netmiko import ConnectHandler
import json
nx_os = {
'device_type': 'cisco_ios',
'ip': 'sbx-nxos-mgmt.cisco.com',
'username': 'admin',
'password': 'Admin_1234!',
'port': 8181
}

net_connect = ConnectHandler(**nx_os)
output = net_connect.send_command('show ip int brief | json- pretty')
json_data = json.loads(output)
int_number = len(json_data['TABLE_intf']['ROW_intf'])
for x in range(int_number):
print(json_data['TABLE_intf']['ROW_intf'][x]['intf-name'])
print(json_data['TABLE_intf']['ROW_intf'][x]['prefix'])
