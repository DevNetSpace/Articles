from netmiko import ConnectHandler
import time

def main():
    cisco_router = {
        'device_type': 'cisco_ios',
        'ip':   '1.1.1.1',
        'username': 'XYZ',
        'password': 'XYZ',
        # 'port' : 22,          # optional - defaults is 22
        # 'secret': '',     # optional - defaults is ''
        # 'verbose': False,       # optional - defaults is False
    }

    net_connect = ConnectHandler(**cisco_router)

    output = net_connect.send_command('show ip int brief')
    print(output)
    time.sleep(5)
    output = net_connect.send_command('sh int loopback 0 description')
    print(output)
    time.sleep(5)
    config_commands = [ 'int loopback 0',
                        'description DESCRIPTION MADE BY NETMIKO']

    output = net_connect.send_config_set(config_commands)
    print(output)
    time.sleep(5)
    output = net_connect.send_command('sh int loopback 0 description')
    print(output)
    time.sleep(5)


if __name__ == "__main__":
    main()