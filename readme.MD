PHPipam Module - Basic script for now work still in progress

note: this will only work if mac address are inputted to PHPipam and dns name is entered or reserve lookup is enabled

Requirements

 - PHPipam 1.4 install with MysqlDB
 - Python3 with mysql-connector-python argparse installed
 - DHCPD server installed

How to Run

- git clone the repo

- create folder /root/scripts

- copy ipam_dhcp.py to /root/scripts

- create a directory /etc/dhcp/reserved_ips (doesnt really matter but it how i set mine up)
command = 'mkdir -p /etc/dhcp/reserved_ips'

- edit /etc/dhcp/dhcpd.conf to include the files generated (continue reading for how to use cron to generate the file)
  
  include "file directort and file name here";

the following variables need to be passed in subnetID, router, dns, search domain:

python3 ipam_dhcp.py -sid subnetID -r router IP -dns dns -searchd search domain
  note: mutliple copies of the script are required for each subnet

- create cron to create the files every 5 minutes (this can be changed to suit your needs)

 */5 * * * *  python3 ipam_dhcp.py -sid subnetID -r routerIP -dns dns -searchd search domain >> /etc/dhcp/reserved_ips/name of file in dhcpd.conf


