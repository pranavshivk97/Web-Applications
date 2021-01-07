* Network Programming - HW6 *

If the input is given as GET, BOUNCE, or EXIT, the commands are output at the client terminal and the corresponding output
is output at the server terminal. If any other command is run, the client outputs "Error: Illegal Input".

If GET is run along with a text file, the contents of the text file are displayed on the server terminal, as long as the 
text file exists. If it doesn't exist, the terminal at the client says that the file doesn't exist. If GET alone is run, the 
client terminal asks the user to input a text file as well.

If BOUNCE is run with a message, the message is displayed on the server terminal. If no message is added, only BOUNCE is
sent, the client terminal asks the user to input a message as well. 

In both GET and BOUNCE, a Success message is sent from the server to the client.


If EXIT is run, the client terminates the connection and at the server side, "Connection is terminated" shows up. 
If EXIT ErrorCode is run, the client also terminates the connection but with the message "Connection is terminated with error
code: " and the error code name.

If any other command is given, the terminal asks the user to enter a valid command.

To run the code, open terminals for the server and client respectively. 

Run the commands:
	python server.py for the server
	python client.py for the client

Sample Commands:
	GET test.txt
	BOUNCE hi what's up
	EXIT
	EXIT ErrorCode