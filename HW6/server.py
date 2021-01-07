from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)  # create socket for the server
s.bind(('127.0.0.1', 8888))  # bind to the port number

while True:
    print("Waiting for the client to connect....\n")
    c, address = s.recvfrom(1024)       # buffer size to received
    print("Connection established from ", address, "\n")

    inp = c.decode()        # decoded input

    if inp is None or inp == "":
        print("Please enter a command: ")
    else:
        if inp[:3] == "GET":        # if GET, read text file and print contents
            try:
                file_name = inp[4:]
                file = open(file_name, 'r')
                print("Reading the file " + file_name + "....")
                lines = file.readlines()
                for line in lines:
                    print(line.strip())
                print("\n")
                s.sendto(b'Success', address)
            except FileNotFoundError:
                print("File not found")
                s.sendto(b'File does not exist!', address)

        elif inp[0:6] == "BOUNCE":      # if BOUNCE, print the message
            print("The client's message is: ", inp[7:len(inp)])
            s.sendto(b'Success', address)
        elif inp[0:4] == "EXIT":        # If EXIT, terminate connection
            if inp[5:] == "":
                print("Connection has been terminated")
                s.sendto(b'Connection Terminated', address)
            else:
                print("The connection has been terminated with code: ", inp[5:len(inp)])
                s.sendto(b'Connection Terminated with error code', address)
        else:
            print("Invalid command\n")
            s.sendto(b'Invalid Command', address)
