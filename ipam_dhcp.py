import os
import sys
import socket, struct
import mysql.connector

router=''
dns=''

def get_ips():

    mydb = mysql.connector.connect(
    host="",
    user="phpipam",
    password="",
    database="phpipam"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM ipaddresses where subnetId='10'")

    myresult = mycursor.fetchall()

    return myresult

def compile(result):
    for x in result:
        mac = x[6]
        if mac is not None:
            ip = socket.inet_ntoa(struct.pack('!L', int(x[2])))
            hostname = x[5]
            print("host", hostname,""'{'"\n  hardware ethernet ", mac ,";\n  fixed-address",ip,";\n  option routers",router,";\n  option domain-name-servers",dns,";\n  option domain-search \"",domainname,"\";\n}\n")
            

def main():
	result = get_ips()
	compile(result)



main()   	
