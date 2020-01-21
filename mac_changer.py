#! /usr/bin/env python

import subprocess
import optparse
import re

def print_motd():
    print("""
 _     _ _______ _______ _     _
 |_____| |_____| |______ |_____|
 |     | |     | ______| |     |                               
""")


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac_address", help="MAC address")
    (options, arguments) = parser.parse_args()

    #print(options.new_mac_address)
    #print(options.interface)
    if not options.interface:
        print_motd()
        parser.error("\n[-]Please specify an interface to change MAC address.\n use --help / -h for more information")
    elif not options.new_mac_address:
        print_motd()
        parser.error("\n[-]Please specify a MAC address to change MAC address.\n use --help / -h for more information")
    return options

def change_mac(interface, new_mac_address):
    print_motd()
    print("[+]Changing MAC address of " + interface + " to " + new_mac_address)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_search_result.group(0):
        return mac_search_result.group(0)
    else:
        print("[-]Could not find MAC address")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC address : "+ str(current_mac))

change_mac(options.interface, options.new_mac_address)

current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac_address:
    print("[+]Successfully changed MAC address to " + current_mac )
else :
    print("[-]Sorry failed to change the MAC address")