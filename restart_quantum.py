from fabric.api import *

env.hosts = [ "controller01.sample.local", "network01.sample.local", "computo01.sample.local" ]
env.user = "root"

def restart_quantum():
	run("cd /etc/init.d/; for i in $( ls quantum-* ); do sudo service $i restart; done")
