# --------------------------------
# CodingGears.io
# --------------------------------

# TODO: Imports
import ipaddress

# TODO: Enter Network List
my_networks = ['192.168.0.0/24', '10.0.0.0/28']

# TODO: Display Network Information
for n in my_networks:
    network = ipaddress.ip_network(n)
    # print(type(network))
    print("Network              : {}".format(n))
    print("Is private network ? : {}".format(network.is_private))
    print("Broadcast Network    : {}".format(network.broadcast_address))
    print("Network              : {}".format(network.with_netmask))
    print("No. of IP addresses  : {}".format(network.num_addresses))

    print()

