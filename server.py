"""Server for multithreaded (asynchronous) application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import sqlite3

import time


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        #client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = "client1"
    #name = client.recv(BUFSIZ).decode("utf8")
    #welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    #client.send(bytes(welcome, "utf8"))
    #msg = "%s has joined the chat!" % name
    #broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        #quest_numb = client.recv(BUFSIZ).decode("utf8")
        quest_num = client.recv(BUFSIZ)

        if quest_num != bytes("{quit}", "utf8"):
            #broadcast(msg, name + ": ")
            conn2 = sqlite3.connect('quiz.db')
            cursor = conn2.cursor()
            cursor.execute("SELECT question FROM questions WHERE id = :new_id ", {"new_id": int(quest_num)})
            results = cursor.fetchone()
            msg = results[0].encode()
            broadcast(msg)
            time.sleep(0.05)

            cursor.execute("SELECT first_variant FROM answers WHERE answ_id = :new_id ", {"new_id": int(quest_num)})
            results = cursor.fetchone()
            msg = results[0].encode()
            broadcast(msg)
            time.sleep(0.05)

            cursor.execute("SELECT second_variant FROM answers WHERE answ_id = :new_id ", {"new_id": int(quest_num)})
            results = cursor.fetchone()
            msg = results[0].encode()
            broadcast(msg)
            time.sleep(0.05)

            cursor.execute("SELECT third_variant FROM answers WHERE answ_id = :new_id ", {"new_id": int(quest_num)})
            results = cursor.fetchone()
            msg = results[0].encode()
            broadcast(msg)
            time.sleep(0.05)

            cursor.execute("SELECT fourth_variant FROM answers WHERE answ_id = :new_id ", {"new_id": int(quest_num)})
            results = cursor.fetchone()
            msg = results[0].encode()
            broadcast(msg)
            time.sleep(0.05)

            cursor.execute("SELECT true FROM answers WHERE answ_id = :new_id ", {"new_id": int(quest_num)})
            results = cursor.fetchone()
            msg = results[0].encode()
            broadcast(msg)

        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            #broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg):
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(msg)


clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()