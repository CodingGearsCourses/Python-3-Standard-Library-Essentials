# --------------------------------
# CodingGears.io
# --------------------------------

# TODO: Imports
import ipaddress

# TODO: IP Addresses
my_hosts = ["192.168.0.10", "10.0.0.5",
            "120.120.120.20", '2001:db8::',
            "fe80:7d91::"]

# TODO: Display information
for ip in my_hosts:
    address = ipaddress.ip_address(ip)
    is_private = address.is_private
    ip_version = address.version
    print("{} is a ver{} IP Address.".format(address, ip_version))
    if is_private:
        print("      >>> This is a private IP address!")
    else:
        print("      >>> This is NOT a private IP address!")
    print()
