#! /usr/bin/env python

import subprocess
import optparse

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
    if not options.interface:
        print_motd()
        parser.error("\n[-]Please specify an interface to change MAC address.\n use --help / -h for more information")
    elif not options.new_mac_address:
        print_motd()
        parser.error("\n[-]Please specify a MAC address to change MAC address.\n use --help / -h for more information")
    return options


def change_mac(interface, new_mac_address):
    print_motd()
    print("[+] changing MAC address of " + interface + " to " + new_mac_address)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac_address)
