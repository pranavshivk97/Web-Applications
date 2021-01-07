from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)     # create socket for client
s.bind(('127.0.0.1', 0))            # bind to the port number
server = ('127.0.0.1', 8888)        # define the server

flag = True
while flag:
    inp = input("Hi, enter a command: ")     # input for client to enter the command

    if inp[:4] == "EXIT":
        print("Command: ", inp)
        s.sendto(inp.encode(), server)
        exit(0)
    elif inp[:3] == "GET":      # if GET
        if inp[4:] == "":       # if no text file is specified, ask user to enter a text file
            print("Please enter a text file\n")
            continue
        else:
            print("\nCommand: ", inp)       # Else print the command and encode the command for the server
            s.sendto(inp.encode(), server)
    elif inp[:6] == "BOUNCE":               # if BOUNCE
        if inp[7:] == "":                   # if no message is specified, ask user to enter the message
            print("Please enter a message\n")
            continue
        else:
            print("\nCommand: ", inp)       # else print command and send encoded input to server
            s.sendto(inp.encode(), server)
    else:
        print("\nError: Illegal Input")     # if invalid command
        continue
    c, address = s.recvfrom(1024)
    if len(inp) >= 4 or inp[0:4] == "EXIT":
        print("\nIncoming Message from Server: " + c.decode())
    elif inp[0:4] == "EXIT":
        print("\nIncoming Message from Server: " + c.decode())
    else:
        print("\nIncoming Message from Server: " + c.decode())
