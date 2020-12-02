def main():
  import file
  
  file.main()
  ssh_tunnel()
  

def ssh_tunnel():
  import paramiko
  import inputKal
  
  bool = True
  while(bool):
    dir = "/home"
    name = "python.py"
    komp = input("Masukan node yang melakukan komputasi? (delimiter with space) | ")
    kompli = list(komp.split(" "))
    kalku = inputKal.main()
    
    for i in kompli:
      try:
        ip, port, username, password = accessNode(i)
        tunnel = paramiko.SSHClient()
        tunnel.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        tunnel.connect(ip, port, username, password)
        print("node%s %s %s was CONNECTED" % (i, ip, username))
        dir, name = dirFile(dir, name)
        stdin, stdout, stderr = tunnel.exec_command("cd %s && %s" % (dir, name))
        stdin.write(kalku)
        stdin.close()
        for i in stdout.readlines():
          print(i)          
        for i in stderr.readlines():
          print(i)
        tunnel.close()
      except(TimeoutError):
        print("node%s %s %s NOT CONNECTED" % (i, ip, username))
        continue
    bool = lagi()
  
  print("\nTerima kasih telah menggunakan program ini. :)")
    
def lagi():
  dec = input("Apakah anda ingin melakukan komputasi lagi? (y/n) | ")
  if dec.casefold() == "n":
    return False
  else:
    return True
      
def dirFile(dir, name):
  dir = input("Masukan lokasi file : ")
  name = input("Masukan perintah : ")
  return dir, name
    
def accessNode(i):
  import node
  
  temp = locals()
  exec("tempNode = node.node%s" % i, globals(), temp)
  tempNode = temp["tempNode"]
  ip = tempNode['ip']
  port = tempNode['port']
  username = tempNode['username']
  password = tempNode['password']
  return ip, port, username, password
  
main()