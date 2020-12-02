def main():
  a = int(input("Menu Operasi \n1. Hitung Luas dan Keliling Segitiga \n2. Hitung Luas dan Keliling Lingkaran \n3. Hitung Luas dan Keliling Persegi \nMasukan pilihan ... | "))
  if (a == 1):
    a,b = luasSegitiga()
    a = a + "\n" + b
    b,c,d = kelilingSegitiga()
    return "1\n" + a + "\n" + b + "\n" + c + "\n" + d
  elif (a == 2):
    a = luasLingkaran()
    return "2\n" + a + "\n" + a 
  elif (a == 3):
    a = luasPersegi()
    return "3\n" + a + "\n" + a
  else:
    print("Masukan anda tidak valid")
    return "0"

def luasSegitiga():
  a = input("Masukan nilai alas   : ")
  b = input("Masukan nilai tinggi : ")
  return a, b
  
def kelilingSegitiga():
  a = input("Masukan nilai sisiA : ")
  b = input("Masukan nilai sisiB : ")
  c = input("Masukan nilai sisiC : ")
  return a, b, c

def luasLingkaran():
  a = input("Masukan nilai jari-jari : ")
  return a

def luasPersegi():
  a = input("Masukan nilai sisi : ")
  return a
