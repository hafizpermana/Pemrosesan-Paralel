def main():
  a = int(input(""))
  if (a == 1):
    luasSegitiga()
    kelilingSegitiga()
  elif (a == 2):
    luasLingkaran()
    kelilingLingkaran()
  elif (a == 3):
    luasPersegi()
    kelilingPersegi()
  else:
    print("Masukan anda tidak valid")

def luasSegitiga():
  a = float(input(""))
  b = float(input(""))
  c = 0.5 * a * b
  print("Luas Segitiga adalah ", c)
  
def kelilingSegitiga():
  a = float(input(""))
  b = float(input(""))
  c = float(input(""))
  d = a + b + c
  print("Keliling Segitiga adalah ", d)

def luasLingkaran():
  a = float(input(""))
  b = 3.14 * a * a
  print("Luas Lingkaran adalah ", b)
  
def kelilingLingkaran():
  a = float(input(""))
  b = 2 * 3.14 * a
  print("Keliling Lingkaran adalah ", b)

def luasPersegi():
  a = float(input(""))
  b = a * a
  print("Luas Persegi adalah ", b)

def kelilingPersegi():
  a = float(input(""))
  b = 4 * a
  print("Keliling Persegi adalah ", b)
  
main()
