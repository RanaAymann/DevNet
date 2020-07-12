# Python ACI Toolkit SDK - www.acitoolkit.readthedocs.io - github.com/datacenter/acitoolkit
# Creating full Tenant with ACI Toolkit

from acitoolkit.acitoolkit import *

# See capabilities
# dir()

url = 'https://sandboxapicdc.cisco.com'
user = 'admin'
pw = 'ciscopsdt'

# Create the session object
session = Session(url, user, pw)

# Login to the session
session.login()

# Get tenants
tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)
    print(tenant.descr)
    print('*' * 30)
    print(' ')

# Create a new Tenant
new_tenant = Tenant("Tenant_Name_Here")


# Create the application profile and the EPG
# the Parent and what under it , EPG : End Point Group
anp = AppProfile('Ranas_app', new_tenant)
epg = EPG('Ranas_epg', anp)

# Create the L3 Namespace
context = Context('Ranas_VRF', new_tenant)
bridge_domain = BridgeDomain('Ranas_bd', new_tenant)

# Associate the BD with the L3 Namespace
bridge_domain.add_context(context)
epg.add_bd(bridge_domain)

##### Tenant Creation is completed #####
# get_url , get_json fuctions from acitoolkit

print(new_tenant.get_url())
print(new_tenant.get_json())
response = session.push_to_apic(
    new_tenant.get_url(), data=new_tenant.get_json())
print(response)

tenants = Tenant.get(session)
for tenant in tenants:
    if tenant.name == 'Tenant_Name_Here':
        print(tenant.name)
    else:
        print(tenant.name)
        print(tenant.descr)
        print('*' * 30)
        print(' ')

# new_tenant.mark_as_deleted()
#session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())
