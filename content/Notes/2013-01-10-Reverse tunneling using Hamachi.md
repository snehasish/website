Title: Reverse tunneling using Hamachi
Date: 2013-01-10 
Tags: hamachi, ubuntu, tunneling, ssh
Slug: reverse-tunneling-using-hamachi
Author: Snehasish
Summary: Reverse tunneling into a system behind a firewall using Hamachi

Here is how to ssh into a remote host behind a firewall / http proxy using hamachi. 
Root privileges are required in the described method.

1. Install the 32 bit or 64 bit version of hamachi using the [deb files available on their website](https://secure.logmein.com/labs/) on both machines. Use the synaptic package manager or use

		sudo dpkg -i logmein-hamachi_2.1.0.86-1_amd64.deb 

2. The daemon should automatically start after installation. Log into the hamachi network, then set your desired nickname using and create a network from one of the computers using:

		sudo hamachi login
		sudo hamachi set-nick <nickname>
		sudo hamachi create <network-name>

3. This may fail if the machine is behind a http proxy. Hamachi uses ports 12975 and 32976 to communicate with the central server, failing which it tries 443 (SSL). In case the machine is behind a HTTP Proxy, the settings need to be overridden:

		sudo gedit /var/lib/logmein-hamachi/h2-engine-override.cfg

	Add the following lines, where the format should be similar to the file h2-engine.cfg in the same folder:

		Conn.PxyAdd 	<Proxy IP Address>
		Conn.PxyPort 	<Proxy Port>
		Conn.Mask 		4

	Restart the hamachi daemon:

		sudo /etc/init.d/logmein-hamachi restart

	For troubleshooting, take a look at the log file:

		tail /var/lib/logmein-hamachi/h2-engine.log

4. Join the hamachi network from the other computer using 

		sudo hamachi join <network-name>

5. On the machine you wish to log into, install openssh-server
		
		sudo apt-get install openssh-server

6. Check out the hamachi IP of the machine you want to log into (host)

		sudo hamachi list # Third field 
		ifconfig # On the host machine, check the ip address of the ham0 network

7. You can now log into the host using 
		
		ssh username@<hamachi-ip>


For a more detailed guide where you can setup RDP and File Sharing, [check out this link](http://www.thefanclub.co.za/how-to/how-remote-login-access-and-control-computers-using-logmein-hamachi-and-haguichi-ubuntu-1204).