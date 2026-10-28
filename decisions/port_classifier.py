#port_classifier.py.



port = int(input("enter the port = "))


#Print the Range
if port < 0 or port > 65535:
    print ("Invalid port: use a number from 0 to 65535.")
elif port > 0 or port >= 1023:
    print ("Range: system")
elif port >=1024  or port > 49151:
    print ("Range: user")
else:
    print("Range: dynamic or private")


#print the Service
if port == 22 : 
    print ("Service: ssh")
elif port == 80 :
    print ("Service: http")
elif port == 443 :
    print ("Service: https")
else:
    print ("")