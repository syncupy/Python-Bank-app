import socket
import sqlite3
#Imports for sockets and database sql library

Connect = sqlite3.connect('Bank.db')
Com = Connect.cursor()


host = '127.0.0.1'                        
port = 5556
buffer = 4096
dbmoney = None

def begin(clientsocket):
   
   while True:
   
      while True:

         data = bytes(clientsocket.recv(buffer))
         if not data: break
         else:
            read(clientsocket, data)
            
def read(clientsocket, data):            
         
   decoder = data.decode('ascii')
   splitter = decoder.split("!")
   ID = splitter[0]
   variable = splitter[1]
#This splits the incoming message into different variable seperated by !
   print (variable, ID, amount)
      
   com.execute("SELECT CustomerID FROM Customers WHERE CustomerID = (?)", (ID, ))
   ifnull()
   c.execute("INSERT CustomerID, Balance INTO Customers VALUES(?,'100')", (ID, ))
   com.commit()
#commit command is saving the database
   print("New Customer Inserted")
#It takes the name and searches for it in the database if not found then it creates a new user
   if variable == "Bal":
     c.execute("SELECT Balance FROM Customers WHERE CustomerID = (?)", (ID, ))
                      # SEND DATA TO CLIENT WITH RESULT

   elif variable == 'With':
      amount = splitter[2]
#if there is an extra piece of data from the message it will save it in a new variable
      com.execute("SELECT Balance FROM Customers WHERE CustomerID = (?)", (ID, ))
      splitter = dbmoney
      dbtotal = splitter[0]
      dbtotal -= amount
#This is is subtracting the amount from the client from their total balance
      com.execute("UPDATE Balance FROM Customers WHERE CustomerID = (?)", (ID, ))
      com.commit()
      
            # SEND UPDATED AMOUNT TO CLIENT


   elif variable == 'Dep':
      amount = splitter[2]
#if there is an extra piece of data from the message it will save it in a new variable
      com.execute("SELECT Balance FROM customers WHERE CustomerID = ?", (ID, ))
      splitter = dbmoney
      dbtotal = splitter[0]
      dbtotal += amount
#This is is adding the amount from the client from their total balance
      com.execute("UPDATE Balance FROM customers WHERE CustomerID = (?)", (ID, ))
      com.commit()
                       #  SEND UPDATED AMOUNT TO CLIENT





serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen(1)
clientsocket,addr = serversocket.accept()                              
connection, address = serversocket.accept()
#creating a new socket and accepting it

print("Got a connection from %s" % str(addr))
#displaying a confirmation of the connection
begin(clientsocket)
#starts the clientsocket method



      
