import os
import sys
import socket, struct
import mysql.connector
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-sid', help='Enter Subnet ID')
parser.add_argument('-r', help='Enter Router ip')
parser.add_argument('-dns', help='Enter Dns servers')
parser.add_argument('-searchd', help='Enter search domain')
args = parser.parse_args()

subnetId = args.sid
router = args.r
dns = args.dns
domainname = args.searchd

def get_ips(subnetId):

    mydb = mysql.connector.connect(
    host="",
    user="phpipam",
    password="",
    database="phpipam"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM ipaddresses where subnetId='"+subnetId+"'")

    myresult = mycursor.fetchall()

    return myresult

def compile(result):
    for x in result:
        mac = x[6]
        if mac is not None:
            ip = socket.inet_ntoa(struct.pack('!L', int(x[2])))
            hostname = x[5]
            print("host", hostname,""'{'"\n  hardware ethernet "+ mac+";\n  fixed-address"+ip+";\n  option routers "+router+";\n  option domain-name-servers "+dns+";\n  option domain-search \""+domainname+"\";\n}\n")
            

def main():
	result = get_ips(subnetId)
	compile(result)
main()   	
