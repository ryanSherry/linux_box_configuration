#! /bin/sh
#install squid 3
wget https://raw.githubusercontent.com/serverok/squid-proxy-installer/master/squid3-install.sh -O squid3-install.sh
sudo bash squid3-install.sh
#setup user and password
sudo /usr/bin/htpasswd -b -c /etc/squid/passwd $1 $2
#reload squid
sudo systemctl reload squid
#multiple ips
wget https://raw.githubusercontent.com/serverok/squid-proxy-installer/master/squid-conf-ip.sh
sudo bash squid-conf-ip.sh
#change port i.e.
sudo sed -i "s/^http_port.*$/http_port $3/g" /etc/squid/squid.conf
sudo systemctl restart squid