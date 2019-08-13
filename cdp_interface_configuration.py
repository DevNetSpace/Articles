from netmiko import ConnectHandler
import time
import re


def main():
    cisco_switch = {
        'device_type': 'cisco_ios_telnet',
        'ip': '10.110.11.1',
        'username': 'root',
        'password': 'admin',
        'port': 23,
        'secret': 'enable'
    }
    net_connect = ConnectHandler(**cisco_switch)
    get_cdp_output = net_connect.send_command('show cdp neigh')
    print (get_cdp_output)
    time.sleep(1)
    device_and_interface_regex = re.compile(r'(\S+)\s + (Eth \d/\d) ')
    print (device_and_interface_regex)
    device_and_interface = device_and_interface_regex.findall(get_cdp_output)
    print (device_and_interface)
    time.sleep(2)

    for i in range(0, len(device_and_interface)):
        config_commands = ['interface ' + str(device_and_interface[i][1]),
                           'description connected to ' + str(device_and_interface[i][0]),
                           'switchport mode access',
                           'switchport access vlan 100']
        print(config_commands)
        net_connect.send_config_set(config_commands)


if __name__ == "__main__":
    main()
