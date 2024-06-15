%Define the server address and port
host = '127.0.0.1'; % local host
port = 4000;

% Creates a TCP/IP client
connection = tcpclient(host,port);

% Send the data to the server
message = "Hello Server World, nice to meet you all!";
writeline(connection, message);

% Receive the echoed message
received_message = readline(connection);

% Display the received message
disp(['Recieved froim server: ', received_message]);

% Clear the client
clear connection;