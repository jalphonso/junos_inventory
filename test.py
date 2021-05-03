from jnpr.junos import Device
from jnpr.junos.exception import ConnectError, ProbeError, ConnectAuthError
from jnpr.junos.op.inventory import ModuleTable


hostname = '192.168.100.100'
netconf_port = 830
user = 'user'
passwd = None
ssh_config = '/Users/user/.ssh/conf.d/lab'


with Device(host=hostname, port=netconf_port, user=user, passwd=passwd, ssh_config=ssh_config) as dev:
    # print(dev.facts)
    inventory = ModuleTable(dev).get()
    print(f"{'DESCRIPTION':25} PART#")
    for item in inventory:
        if not item.type:
            continue
        print(f"{item.type:25} {item.pn}")
