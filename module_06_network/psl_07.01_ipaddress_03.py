# --------------------------------
# CodingGears.io
# --------------------------------

# TODO: Imports
import ipaddress

# TODO: Enter Subnets
aws_subnets = [ipaddress.ip_network('10.1.0.0/24'),
               ipaddress.ip_network('10.2.0.0/24')]

# TODO: Enter IP Addresses
aws_ipaddresses = [ipaddress.ip_address('10.1.0.6'),
                   ipaddress.ip_address('10.7.0.31')]

# TODO: Determine to which network the ip addresses belong to
for ip in aws_ipaddresses:
    for net in aws_subnets:
        if ip in net:
            print("{} is on {} network.".format(ip, net))
            break
        else:
            print("{} is NOT on {} network.".format(ip, net))
    print()
