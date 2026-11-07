#port_report.py

start_port = int(input("Start port: "))
end_port = int(input("End port: "))
counter = 0


for port in range(start_port,end_port+1):
    if(port >= 0 and port <=1023 ):
        print(f"{port}: system")
    elif(port >= 1024 and port <= 49151):
        print(f"{port}: user")
    else:
        print(f"{port}: dynamic")
    counter = counter + 1



print(f"Ports checked: {counter}")

