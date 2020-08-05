 git clone https://github.com/CiscoDevNet/hello_network
 
 cd hello_network
  
 ./hello_network.sh
 
 sudo apt install python3-virtualenv
 
 python3 -m venv py3-venv
 
 source py3-venv/bin/activate
 
 deactivate
 
 
 sudo apt install nodejs
 
 sudo apt install npm
 
 nodejs -v
 
 ## Applocations need :
 
 sudo snap install postman
 
 snap install ngrok
 
 # Example :
 
 ngrok http 5000
 
 sudo apt install openconnect
 
  # Example Connection
 sudo openconnect -b dcloud-rtp-anyconnect.cisco.com
 
 # Find the running process
 sudo ps -ax | grep openconnect
 
 sudo kill 22741 
 
 # Application container engine
 
 sudo apt install apt-transport-https ca-certificates curl software-properties-common
 
 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  
 sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
 
 sudo apt update
 sudo apt install docker-ce
 
 sudo systemctl status docker
  
 sudo usermod -aG docker $USER
   
 docker run busybox
    
 docker ps -a
  
  
  
  
 
 
 
 
 
  
