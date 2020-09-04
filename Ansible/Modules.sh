#raw module with the uptime action (-a)
# /usr/bin/uptime is a command

ansible -m raw -a '/usr/bin/uptime' linuxhosts

ansible -m shell -a 'python3 -V' linuxhosts

#check I'm running as sudo Rana

ansible all -a 'whoami'


#elevate to root with -b for become. Why? Because ansible doesn't elevate to sudo by default

ansible all -b -a 'whoami'
