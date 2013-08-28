from fabric.api import *

env.hosts = [ "computo01.sample.local", "computo02.sample.local", "computo04.sample.local", "computo05.sample.local", "computo06.sample.local" ]
env.user = "root"

def restart_service():
	# Para poder realizar esta accion a de estar en el /root de cada nodo el script:
	# service-compute.sh
	# 
	run("bash /root/service-compute.sh stop; bash /root/service-compute.sh start; ip link set br-tun up")

def active_syslog():
	comando = "echo >> /etc/nova/nova.conf && echo 'use_syslog = True' >> /etc/nova/nova.conf"
	run( comando )
	
