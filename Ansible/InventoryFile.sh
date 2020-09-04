#Ansible knows about all the devices and servers it needs to manage by the inventory file.
# [group name] then under it the IPs 

sudo nano /etc/ansible/hosts

#then add the devices at the end of the file

[linuxhosts]
ubuntu
centos

ansible -m ping all 
# m means module

ansible -m ping linuxhosts
#will ping both devices
