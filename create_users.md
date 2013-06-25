# To Create Users

#### Comparación entre nodo instalado y nodo sin instalar

```diff
--- computo02.group	2013-03-19 15:38:34.368294362 +0100
+++ computo01.group	2013-03-19 15:38:12.408292363 +0100
@@ -50,3 +50,8 @@
 operador:x:1000:
 lpadmin:x:111:operador
 sambashare:x:112:operador
+nova:x:600:
+libvirtd:x:650:nova
+kvm:x:700:libvirt-qemu
+ntp:x:113:
+quantum:x:114:
```

```diff
--- computo02.passwd	2013-03-19 15:38:23.432292430 +0100
+++ computo01.passwd	2013-03-19 15:38:00.124293530 +0100
@@ -23,3 +23,8 @@
 landscape:x:104:109::/var/lib/landscape:/bin/false
 sshd:x:105:65534::/var/run/sshd:/usr/sbin/nologin
 operador:x:1000:1000:operador,,,:/home/operador:/bin/bash
+nova:x:600:600::/var/lib/nova:/bin/sh
+libvirt-qemu:x:650:650::/var/lib/libvirt:/bin/false
+ntp:x:106:113::/home/ntp:/bin/false
+libvirt-dnsmasq:x:107:650:Libvirt Dnsmasq,,,:/var/lib/libvirt/dnsmasq:/bin/false
+quantum:x:108:114::/var/lib/quantum:/bin/false
```

#### comandos

```
groupadd -g 600 nova
groupadd -g 650 libvirtd
groupadd -g 700 kvm
groupadd -g 113 ntp
groupadd -g 114 quantum

useradd -g 600 -g 600 -G 650 -s /bin/sh -d /var/lib/nova -m nova
useradd -g 650 -g 650 -G 700 -s /bin/false -d /var/lib/libvirt -m libvirt-qemu
useradd -g 108 -g 114 -s /bin/false -d /var/lib/quantum -m quantum
useradd -g 106 -g 113 -s /bin/false -d /home/ntp ntp
useradd -g 107 -g 650 -s /bin/false -d /var/lib/libvirt/dnsmasq -m libvirt-dnsmasq
```
