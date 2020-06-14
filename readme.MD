PHPipam Module - Basic script for now work still in progress

note: this will only work if mac address are inputted to PHPipam and dns name is entered

Requirements

 - PHPipam 1.4 install with MysqlDB
 - Python3 with mysql-connector-python installed
 - DHCPD server installed

How to Run

- git clone the repo

- create folder /root/scripts

- copy ipam_dhcp.py to /root/scripts

- create a directory /etc/dhcp/reserved_ips (doesnt really matter but it how i set mine up)
command = 'mkdir -p /etc/dhcp/reserved_ips'

- edit /etc/dhcp/dhcpd.conf to include the files generated (continue reading for how to use cron to generate the file)
  
  include "file directort and name her";

- for now where are static variable you will need to change to suit you needs
  - router
  - domainname
  - dnsserver
  - subnetID
  note: mutliple copies of the script are required for each subnet

- create cron to create the files every 5 minutes (this can be changed to suit your needs)
  
  */5 * * * * python3 /root/scripts/ipam_dhcp.py >> /etc/dhcp/reverse_ips/filename here (ends with .conf)
  example: */5 * * * * python3 /root/scripts/ipam_dhcp.py >> /etc/dhcp/reverse_ips/vlan_10_reserved.conf


