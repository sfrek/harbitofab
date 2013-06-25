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
# from fabric.api import env, sudo, run, put
from fabric.api import *

def set_hosts(filename):

    with open(os.path.expanduser(filename)) as fd:
        env.hosts = [ host.strip() for host in fd.readlines() ]


def add_computo_usuarios():

    commands = (
	"groupadd -g 600 nova;"
	"groupadd -g 650 libvirtd;"
	"groupadd -g 700 kvm;"
	"groupadd -g 113 ntp;"
	"groupadd -g 114 quantum;"
	"useradd -g 600 -g 600 -G 650 -s /bin/sh -d /var/lib/nova -m nova;"
	"useradd -g 650 -g 650 -G 700 -s /bin/false -d /var/lib/libvirt -m libvirt-qemu;"
	"useradd -g 108 -g 114 -s /bin/false -d /var/lib/quantum -m quantum;"
	"useradd -g 106 -g 113 -s /bin/false -d /home/ntp ntp;"
	"useradd -g 107 -g 650 -s /bin/false -d /var/lib/libvirt/dnsmasq -m libvirt-dnsmasq;"
    )

    sudo(commands)

def get_vpn_ip():

    sudo("ip a show tap0")

def set_root_pass():

    sudo("passwd")

def install_ocfs2():

    sudo("apt-get -y install ocfs2-tools")
    run("service ocfs2 stop")

def ocfs2_restart():

    run("service ocfs2 restart")

def ocfs2_mounted():

    run("mounted.ocfs2 -f")
    run("grep instances /proc/mounts")

def ocfs2_write():

   run("dd if=/dev/zero of=/var/lib/nova/instances/$(hostname).zeros count=10 bs=1024")
   run("ls -ls /var/lib/nova/instances/")

def multipath_list():

   run("multipath -ll")

def reboot():

   run("hostname -f")
   run("nslookup $(hostname -f)")
   run("reboot")

def upgrade():

   run("aptitude update")
   run("aptitude -y full-upgrade")

def add_grizzly():
   
   command='echo "deb http://ubuntu-cloud.archive.canonical.com/ubuntu precise-updates/grizzly main" > /etc/apt/sources.list.d/grizzly.list'
   run(command)

def update():

   run("aptitude update")

def get_interfaces():

   run("ip a show | grep -A3 eth")

def get_hostname():

   run("hostname -f")

def get_mem():

   run("cat /proc/meminfo | awk '/MemTotal:/ {print $2\" \"$3}'")

def get_disk():

   run("fdisk -l;mount")

def get_all():

   get_hostname()
   get_mem()
   get_interfaces()


def send_file(localpath,remotepath):

   put(localpath,remotepath)

def stop_all():
	# Esta funcion hace uso de un script que ya tiene que estar en el server
	run("/root/stop_all.sh")

def desinstall_all():
	# Esta funcion hace uso de un script que ya tiene que estar en el server
	run("/root/desinstall_all.sh")

def reboot():
	run("reboot")

def disable_o2cb():
	run("update-rc.d -f o2cb remove")

def redirect_syslog(host,port="5140"):
	command = 'echo "*.* @%s:%s" > /etc/rsyslog.d/00_redirect.conf' % ( host, port )
	command = command + " && service rsyslog restart"
	run(command)

def architecture():
	command = "lsb_release -a && uname -a"
	run(command)

def remove_corosync():
	comando = "service pacemaker stop; service corosync stop; apt-get -y remove --purge corosync* pacemaker* && apt-get -y autoremove"
	run(comando)

def ocfs_start():
	comando = "service o2cb restart && service ocfs2 restart && "
	comando = comando + " mount -t ocfs2 -o _netdev,defaults /dev/mapper/instances /var/lib/nova/instances && service o2cb status"
	run(comando)

def install_headers():
	run("apt-get install -y linux-headers-$(uname -r)")
