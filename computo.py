from fabric.api import *

env.hosts = [ "computo01.wolkit.local", "computo02.wolkit.local", "computo04.wolkit.local", "computo05.wolkit.local", "computo06.wolkit.local" ]
env.user = "root"

def restart_service():
	# Para poder realizar esta accion a de estar en el /root de cada nodo el script:
	# service-compute.sh
	# 
	run("bash /root/service-compute.sh restart")