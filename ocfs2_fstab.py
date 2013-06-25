import sys
import os
from fabric.api import env, sudo, run

def set_hosts(filename):

    with open(os.path.expanduser(filename)) as fd:
        env.hosts = [ host.strip() for host in fd.readlines() ]


def ocfs2_fstab():

    run("echo '# nova instances ocfs2 file system' >> /tmp/fstab")
    run("echo '/dev/mapper/instances /var/lib/nova/instances/ ocfs2 defaults 0 0' >> /etc/fstab")

def ocfs2_restart():

    run("service ocfs2 restart")

def ocfs2_fstab_mount():

    run("mount -va")

def ocfs2_fstab_umount():

    run("umount -vf /var/lib/nova/instances")

def ocfs2_reconfigure():

    run("dpkg-reconfigure ocfs2-tools")
    run("mount | grep instances")
    run("mounted.ocfs2 -d")
