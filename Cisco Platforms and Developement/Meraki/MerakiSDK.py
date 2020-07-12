#SDK Python library for Meraki

from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

# Create token
# CREATE Connection Object and pass the token in it , store the connection in meraki variable
x_cisco_meraki_api_key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'  
meraki = MerakiSdkClient(x_cisco_meraki_api_key)

# Get Orgs
orgs = meraki.organizations.get_organizations()
pprint(orgs)


# Set OrgId
for org in orgs:
    if org['name'] == "DevNet Sandbox":
        orgId = org['id']
pprint(orgId)


# Get Networks in Org
#Serach how to get the networks : get_organization_networks function , the function requires a dictionary in it's design
# create an open dictionary called params 
params = {}
params['organization_id'] = orgId
networks = meraki.networks.get_organization_networks(params)
pprint(networks)

# Set NetworkId
for network in networks:
    if network['name'] == "DevNet Always On Read Only":
        netId = network['id']
pprint(netId)

# GET VLANS
vlans = meraki.vlans.get_network_vlans(netId)
pprint(vlans)


# Configure the vlan ( updating configs )
# update_network_vlan function

vlan = vlans[0]
# CHANGE VLAN NAME HERE
vlan['name'] = 'Rana was here!'

updatedVlan = {}
updatedVlan['network_id'] = netId
updatedVlan['vlan_id'] = vlan['id']
updatedVlan['update_network_vlan'] = vlan

result = meraki.vlans.update_network_vlan(updatedVlan)

# VERIFY
result_vlans = meraki.vlans.get_network_vlans(netId)
pprint(result_vlans)
