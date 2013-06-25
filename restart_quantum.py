from fabric.api import *

env.hosts = [ "controller01.wolkit.local", "network01.wolkit.local", "computo01.wolkit.local" ]
env.user = "root"

def restart_quantum():
	run("cd /etc/init.d/; for i in $( ls quantum-* ); do sudo service $i restart; done")
