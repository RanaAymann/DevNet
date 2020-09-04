from ncclient import manager
import json
from pprint import pprint

# in dne-dna-code directory in cisco DevNet

m = manager.connect(
    host=env_lab.IOS_XE_1["host"],
    port=env_lab.IOS_XE_1["netconf_port"],
    username=env_lab.IOS_XE_1["username"],
    password=env_lab.IOS_XE_1["password"],
    hostkey_verify=False
)

for capability in m.server_capabilities:
    print(capability)


m.close_session()
