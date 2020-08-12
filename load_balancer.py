import socket
from consistent_hashing import ConsistentHasher
from bst import BST

#keys = ["abcd", "xyza", "pqrs", "wxyz", "mnop", "defg", "gred", "ojfew", "wejfnv", "dgerfg", "ierhgj",
#        "srgergh", "ojrfi", "podjf", "powe"]
#nodes = ["1.2.3.4", "3.4.5.6", "5.6.7.8", "7.8.9.10"]

nodes=["1.2.3.4","3.4.5.6","5.6.7.8"]
server_ports=["5001","5002","5003"]

consistent_hasher = ConsistentHasher()
for node in nodes:
    consistent_hasher.add_node(node)

s=socket.socket()
port=3000
s.bind(('',port))
keys=[]
port_keys=[]
no=2
while no:
    s.listen(5)
    c,addr=s.accept()
    #print("got connection from "+str(addr)) 
    c.send(" ".encode())
    arr=c.recv(1024).decode().split(" ")
    keys.append(arr[0])
    port_keys.append(arr[1])
    no-=1

c.close()
s.close()

assign=[]
for key in keys:
    node_id = consistent_hasher.assign_key_to_node(key)
    #print('Key %s was assigned to node %s' % (key, node_id))
    assign.append(str(node_id))

for i in range(len(port_keys)):
    s=socket.socket()
    p=int(port_keys[i])
    s.connect(('127.0.0.1',p))
    s.recv(1024)
    string="client is connected to "+assign[i]+" via port "+server_ports[nodes.index(assign[i])]
    s.send(string.encode())
    s.close()

node_to_remove = "5.6.7.8"
consistent_hasher.remove_node(node_to_remove)
print('\nRemoved node %s with hashed ID %d\n' % (node_to_remove, consistent_hasher.hash(node_to_remove)))

assign=[]
for key in keys:
    node_id = consistent_hasher.assign_key_to_node(key)
    #print('Key %s was assigned to node %s' % (key, node_id))
    assign.append(str(node_id))    

for i in range(len(port_keys)):
    s=socket.socket()
    p=int(port_keys[i])
    s.connect(('127.0.0.1',p))
    s.recv(1024)
    string="client is connected to "+assign[i]+" via port "+server_ports[nodes.index(assign[i])]
    s.send(string.encode())
    s.close()    

node_to_add = "5.6.7.8"
consistent_hasher.add_node(node_to_add)
print('\nAdded node %s with hashed ID %d\n' % (node_to_add, consistent_hasher.hash(node_to_add)))

assign=[]
for key in keys:
    node_id = consistent_hasher.assign_key_to_node(key)
    #print('Key %s was assigned to node %s' % (key, node_id))
    assign.append(str(node_id))

for i in range(len(port_keys)):
    s=socket.socket()
    p=int(port_keys[i])
    s.connect(('127.0.0.1',p))
    s.recv(1024)
    string="client is connected to "+assign[i]+" via port "+server_ports[nodes.index(assign[i])]
    s.send(string.encode())
    s.close()