def main():
  node1 = {'ip':'192.168.43.74', 'port':22, 'username':'almuqsitalif', 'password':'bismillahi'}
  node2 = {'ip':'192.168.43.79', 'port':22, 'username':'toni', 'password':'qwerty'}
  node3 = {'ip':'192.168.43.59', 'port':22, 'username':'anton', 'password':'asdfgh'}
  node4 = {'ip':'192.168.43.75', 'port':22, 'username':'reno', 'password':'zxcvbn'}
  return node1, node2, node3, node4

def ssh_tunnel():
  from paramiko import SSHClient,AutoAddPolicy
  import inputKal
  
  bool = True
  while(bool):
    statusNode()
    komp = input("Masukan node yang melakukan komputasi? (delimiter with space) | ")
    print("")
    kompli = list(komp.split(" "))
    kalku = inputKal.main() 
    
    for i in kompli:
      try:
        ip, port, username, password = accessNode(i)
        tunnel = SSHClient()
        tunnel.set_missing_host_key_policy(AutoAddPolicy)
        tunnel.connect(ip, port, username, password, timeout=3)
        print("The Connection was CONNECTED")
        print("Hasil Komputasi dari node%s %s %s \n" % (i, ip, username))
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
  
  print("Terima kasih telah menggunakan program ini. :)")
 
def statusNode():
  from sys import exit
  from paramiko import SSHClient,AutoAddPolicy

  i = 1
  status = []
  print("\nsedang memeriksa connection...\n")
  for j in main():
    try:
      print("node%d %s status " % (i, j['ip']), end="")
      tunnel = SSHClient()
      tunnel.set_missing_host_key_policy(AutoAddPolicy)
      tunnel.connect(j['ip'], j['port'], j['username'], j['password'], timeout=3)
      print("ONLINE  username:%s" % j['username'])
      tunnel.close()
      status.append("ONLINE")
    except:
      print("OFFLINE username:%s" % j['username'])
      status.append("OFFLINE")
    finally:
      i = i + 1
  print("")
  if "ONLINE" in status:
    pass
  else:
    print("Semua node sedang OFFLINE, tidak ada yang dapat dilakukan.")
    print("\nTerima kasih telah menggunakan program ini. :)")
    exit()
    
   
def lagi():
  dec = input("Apakah anda ingin melakukan komputasi lagi? (y/n) | ")
  print("")
  if dec.casefold() == "n":
    return False
  else:
    return True
      
def accessNode(i):
  try:
    i = int(i) - 1
    tempNode = main()[i]
    return tempNode['ip'], tempNode['port'], tempNode['username'], tempNode['password']
  except:
    print("Tidak ada node%s" % (i+1))
    ssh_tunnel()
    
ssh_tunnel()