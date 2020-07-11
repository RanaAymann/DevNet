###### REMOTE HOSTS #######
#create local hostnames in hosts file
#it's like creating DNS in my ansible server, so the remote devices IPs will be saved.

sudo nano /etc/hosts

#then try to ping with their names.


#Create SSH key on ansible server

ssh-keygen

#list the keys to verify : id_rsa , id_rsa.pub (public key)

ls .ssh


#copy the key to other machines ( ubuntu , centOs ) names.

ssh-copy-id -i .ssh/id_rsa.pub ubuntu
ssh-copy-id -i .ssh/id_rsa.pub centos



#note if refused because ssh is not enabled on the other ubuntu machine , run:
sudo apt-get install openssh-server

#now try ssh
ssh ubuntu
ssh centos

#Now configure sudo on both machines so that it doesnt require a password ,to run the commands as sudo :
ssh ubuntu
sudo visudo

#very bottom of file add this line:
Rana ALL=(ALL) NOPASSWD: ALL

#then save and exit
