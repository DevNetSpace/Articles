from netmiko import ConnectHandler
import time
import re


def main():
    # cisco_switch = {
    #     'device_type': 'cisco_ios_telnet',
    #     'ip': '192.168.182.128',
    #     'username': '',
    #     'password': '',
    #     'port': 32769,
    #     'secret': ''
    # }
    # net_connect = ConnectHandler(**cisco_switch)
    # get_cdp_output = net_connect.send_command('show cdp neigh')
    # print (get_cdp_output)
    # time.sleep(1)
    # device_and_interface_regex = re.compile(r'(\S+)\s + (Eth \d/\d) ')
    # print (device_and_interface_regex)
    # device_and_interface = device_and_interface_regex.findall(get_cdp_output)
    # print (device_and_interface)
    # time.sleep(10)

    device_and_interface = [('US-AP-4', 'Eth 1/2'), ('US-AP-3', 'Eth 1/1'), ('US-AP-2', 'Eth 1/0')]
    for i in range(0, len(device_and_interface)):
        # output = net_connect.send_command('show cdp neigh ' + str(device_and_interface[i][1]) + ' detail ')
        # print(output)
        # IP_address_regex = re.compile(r'IP address: ([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})')
        # IP_address = IP_address_regex.findall(output)
        # print(IP_address)
        # time.sleep(1)
        config_commands = ['interface ' + str(device_and_interface[i][1]),
                           'description connected to ' + str(device_and_interface[i][0]),
                           'switchport mode access',
                           'switchport access vlan 100']
        print(config_commands)
        net_connect.send_config_set(config_commands)
        # print(output)




if __name__ == "__main__":
    main()
