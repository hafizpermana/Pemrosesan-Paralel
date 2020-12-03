def main():
  fileNode = input("Apakah anda telah membuat file node? (y/n) | ")
  if fileNode.casefold() == "n":
    nodebaru()
  else:
    fileNode = input("Apakah anda ingin memperbarui file node? (y/n) | ")
    if fileNode.casefold() == 'y':
      opennode()
      nodeupdate()
  opennode()
  
def nodebaru():
  node = logic()
  file = open("node.py", "w")
  file.write(node)
  file.close()

def nodeupdate():
  node = logic()
  file = open("node.py", "a")
  file.write(node)
  file.close()

def opennode():
  file = open("node.py", "r")
  for i in file.readlines():
    print(i)
  file.close()

def logic():
  node = ""
  bool = True
  while bool:
    j = input("Node berapa yang ingin dibuat? | ")
    print("Node" + j)
    ip = input("Masukan ip address tujuan : ")
    port = input("Masukan port tujuan : ")
    username = input("Masukan username tujuan : ")
    password = input("Masukan password : ")
    tempNode = "node" + j + " = {'ip':'" + ip + "', 'port':" + port + ", 'username':'" + username + "', 'password':'" + password + "'}"
    node = node + tempNode + "\n"
    dec = input("Masih ingin menambahkan node? (y/n)| ")
    if dec.casefold() == "n":
      bool = False
  
  return node