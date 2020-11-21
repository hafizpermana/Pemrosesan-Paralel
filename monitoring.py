# Source code by Alif Almuqsit
# Keep exploring
# Trial and Error, but Be Carefull

def monitoring():
  import psutil
  from time import sleep
  
  tx = psutil.net_io_counters().bytes_sent
  rx = psutil.net_io_counters().bytes_recv
  sleep(1)
  tx_new = psutil.net_io_counters().bytes_sent
  rx_new = psutil.net_io_counters().bytes_recv
  rx = operasi(rx, rx_new)
  tx = operasi(tx, tx_new)
  
  cpu = round(psutil.cpu_percent(interval=1), 2)
  memory = psutil.virtual_memory().percent
 
  print(" ")
  print("            SISTEM MONITORING COMPUTER")
  print("                  CPU   : {}%".format(cpu))
  print("                  Memori: {}%".format(memory))
  print("                  tx/rx : {} Kbps/{} Kbps".format(tx,rx))


def operasi(old, new):
  new = new - old
  new = (new * 8) / 1000
  return round(new, 2)
  
  
monitoring()