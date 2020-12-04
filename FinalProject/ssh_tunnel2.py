def main():
  node1 = {'ip':'192.168.43.74', 'port':22, 'username':'almuqsitalif', 'password':'bismillahi'}
  node2 = {'ip':'192.168.43.79', 'port':22, 'username':'toni', 'password':'qwerty'}
  node3 = {'ip':'192.168.43.59', 'port':22, 'username':'anton', 'password':'asdfgh'}
  node4 = {'ip':'192.168.43.75', 'port':22, 'username':'reno', 'password':'zxcvbn'}
  return node1, node2, node3, node4

def ssh_tunnel():
  import paramiko
  import inputKal
  
  bool = True
  while(bool):
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
        stdin, stdout, stderr = tunnel.exec_command("cd /home/ && python kalkulasi.py")
        stdin.write(kalku)
        stdin.close()
        for i in stdout.readlines():
          print(i)          
        for i in stderr.readlines():
          print(i)
        tunnel.close()
      except:
        print("node%s %s %s NOT CONNECTED\n" % (i, ip, username))
        continue
        
    bool = lagi()
  
  print("\nTerima kasih telah menggunakan program ini. :)")
    
def lagi():
  dec = input("Apakah anda ingin melakukan komputasi lagi? (y/n) | ")
  if dec.casefold() == "n":
    return False
  else:
    return True
      
def accessNode(i):
  node1, node2, node3, node4 = main()
  
  temp = locals()
  exec("tempNode = node%s" % i, globals(), temp)
  tempNode = temp["tempNode"]
  ip = tempNode['ip']
  port = tempNode['port']
  username = tempNode['username']
  password = tempNode['password']
  return ip, port, username, password
  
ssh_tunnel()