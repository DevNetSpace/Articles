from jinja2 import Environment, FileSystemLoader

# This line uses the current directory and loads environment

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('interface_template.j2')
# here define variables:


interfaces = []
for i in range(1, 12):
    interface = {'number': str(i),
                 'description': 'Users',
                 'vlan': '10'}
    interfaces.append(interface)

for i in range(12, 17):
    interface = {'number': str(i),
                 'description': 'Printers',
                 'vlan': '20'}
    interfaces.append(interface)

for i in range(17, 25):
    interface = {'number': str(i),
                 'description': 'Servers',
                 'vlan': '50'}
    interfaces.append(interface)

output = template.render(interfaces=interfaces)
#Print the output
print(output)