import socket

def getIP():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('8.8.8.8', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP

def sendAll(ip_broadcast):
    try:
        broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        broadcast_socket.bind(('', 0))
        broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    except Exception as err:
        print ("[!] Error creating broadcast socket: %s" % err)

    
    data = b"what is your ip address ?"
    try:
        broadcast_socket.sendto(data, (ip_broadcast, 5000))
        print("envoyé")
        
    except Exception as err:
        print( "[!] Error sending packet: %s" % err)

#sendAll('.'.join(getIP().split(".")[0:-1])+".255")

def listServer(socket):
    sendAll('.'.join(getIP().split(".")[0:-1])+".255")
    msg=socket.recv(1024).decode("Utf8")
