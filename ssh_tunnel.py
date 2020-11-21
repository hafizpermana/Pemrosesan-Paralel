def ssh_tunnel():
  import paramiko
  from getpass import getpass
  
  hostname = input("hostname atau ip address tujuan : ")
  port = int(input("port connection : "))
  username = input("username PC : ")
  password = getpass()
  
  tunnel = paramiko.SSHClient()
  tunnel.set_missing_host_key_policy(paramiko.AutoAddPolicy)
  tunnel.connect(hostname, port, username, password)

  command = input("masukan command : ")
  try :
    while(True):
      stdin, stdout, stderr = tunnel.exec_command(command)
      out = stdout.readlines()
      for i in out :
        print(i)
        
      print("        Tekan Ctrl+C untuk menghentikan Program \n")
  except (KeyboardInterrupt):
    print("       Terima Kasih telah menggunakan program ini. :)")
      
  tunnel.close()
  
ssh_tunnel()
