# Gather chassis inventory for junos devices

This project demonstrates how to obtain the equivalent of the cli command `show chassis hardware` using PyEZ or via Ansible using the Juniper Galaxy juniper.junos module
https://junos-ansible-modules.readthedocs.io/en/latest/

In both cases the PyEZ built-in table, ModuleTable, from inventory.yml is used.

## EXAMPLES

```
% python test.py
DESCRIPTION               PART#
RE-EX2300C-12P            BUILTIN
EX2300-C-12P              650-059984
FPC CPU                   BUILTIN
12x10/100/1000 Base-T     BUILTIN
2x10G SFP/SFP+            650-059984
SFP+-10G-SR               740-021308
JPSU-170W-AC              None
```

```
% ansible-playbook -i hosts test.pb.yml

PLAY [all] *****************************************************************************************************

TASK [gather chassis inventory] ********************************************************************************
ok: [192.168.100.100]

TASK [Print response] ******************************************************************************************
ok: [192.168.100.100] => {
    "response": {
        "changed": false,
        "failed": false,
        "msg": "Successfully retrieved 8 items from ModuleTable.",
        "resource": [
            {
                "jname": "Pseudo CB 0",
                "pn": null,
                "sn": null,
                "type": null,
                "ver": null
            },
            {
                "jname": "Routing Engine 0",
                "pn": "BUILTIN",
                "sn": "BUILTIN",
                "type": "RE-EX2300C-12P",
                "ver": null
            },
            {
                "jname": "FPC 0",
                "pn": "650-059984",
                "sn": "HV3620388999",
                "type": "EX2300-C-12P",
                "ver": "REV 20"
            },
            {
                "jname": "CPU",
                "pn": "BUILTIN",
                "sn": "BUILTIN",
                "type": "FPC CPU",
                "ver": null
            },
            {
                "jname": "PIC 0",
                "pn": "BUILTIN",
                "sn": "BUILTIN",
                "type": "12x10/100/1000 Base-T",
                "ver": "REV 20"
            },
            {
                "jname": "PIC 1",
                "pn": "650-059984",
                "sn": "HV3620388999",
                "type": "2x10G SFP/SFP+",
                "ver": "REV 20"
            },
            {
                "jname": "Xcvr 1",
                "pn": "740-021308",
                "sn": "JN101K22333",
                "type": "SFP+-10G-SR",
                "ver": "REV 01"
            },
            {
                "jname": "Power Supply 0",
                "pn": null,
                "sn": null,
                "type": "JPSU-170W-AC",
                "ver": null
            }
        ]
    }
}

PLAY RECAP *****************************************************************************************************
192.168.100.100               : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
