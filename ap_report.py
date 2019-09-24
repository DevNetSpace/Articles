from netmiko import ConnectHandler
import time
import re
import csv


def main():
    current_date = time.strftime("%Y_%m_%d")
    outputFile = open('ap_report_' + current_date + '.csv', 'a', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(["switch IP", "AP name", "AP IP", "AP platform",  "AP outgoing port number", "AP mac address"])
    ips = ['11.11.11.11', '11.11.11.12', '11.11.11.13', '11.11.11.14']
    for ip in ips:
        cisco_switch = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': 'cisco',
            'password': 'cisco',
            'port': 22,
            'secret': 'cisco'
        }
        net_connect = ConnectHandler(**cisco_switch)
        time.sleep(1)

        get_cdp_output = net_connect.send_command('show cdp neigh')
        print (get_cdp_output)
        time.sleep(1)

        device_and_interface_regex = re.compile(r'(AP-\d)\s+(Gig \d/\d|Fas \d/\d) ')
        device_and_interface_found = device_and_interface_regex.findall(get_cdp_output)
        time.sleep(2)
        print (device_and_interface_found)
        for i in range(0, len(device_and_interface_found)):
            get_cdp_det_output = net_connect.send_command('show cdp neighbors ' + str(device_and_interface_found[i][1])
                                                          + ' det')
            print (get_cdp_det_output)
            ip_regex = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
            device_regex = re.compile(r'Device ID: (\S+)')
            platform_regex = re.compile(r'Platform: (\S+ \S+)')
            outgoing_port_regex = re.compile(r'\(outgoing port\): (\S+)')

            ip_found = ip_regex.findall(get_cdp_det_output)
            device_found = device_regex.findall(get_cdp_det_output)
            platform_found = platform_regex.findall(get_cdp_det_output)
            outgoing_found = outgoing_port_regex.findall(get_cdp_det_output)

            get_arp_output = net_connect.send_command('show ip arp | i ' + str(ip_found[0]))

            mac_regex = re.compile(r'((?:[0-9a-f]{4}\.){2}[0-9a-f]{4})')
            mac_found = mac_regex.findall(get_arp_output)

            outputWriter.writerow([ip, device_found[0], ip_found[0], platform_found[0],  outgoing_found[0], mac_found[0]])


if __name__ == "__main__":
    main()
