"""
usage:

    fab -f distkeys.py set_hosts:/path/to/hosts_file add_key:/path/to/key

    Use --password and --user options as necessary

Inspired by shell script at http://github.com/mlbright/mybin/raw/master/distkeys.sh
Fabric recipe to distribute your ssh key to large number of hosts.

Thanks to Jeff Forcier for clearing up the env.hosts setup.
"""

import sys
import os
from fabric.api import env, sudo

def set_hosts(filename):

    with open(os.path.expanduser(filename)) as fd:
        env.hosts = [ host.strip() for host in fd.readlines() ]


def stop_vpn():

    commands = (
        "hostname -f;"
	"apt-get install openvpn;"
        "sed -i 's/zentyal-abada-client/none/g' /etc/default/openvpn;"
        "service openvpn stop;"
    )

    sudo(commands)
