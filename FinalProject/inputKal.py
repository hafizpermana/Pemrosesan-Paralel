def main():
  a = input("Menu Operasi \n1. Hitung Luas dan Keliling Segitiga \n2. Hitung Luas dan Keliling Lingkaran \n3. Hitung Luas dan Keliling Persegi \nMasukan pilihan ... | ")
  print("")
  if (a == "1"):
    a,b = luasSegitiga()
    a = a + "\n" + b
    b,c,d = kelilingSegitiga()
    return "1\n" + a + "\n" + b + "\n" + c + "\n" + d
  elif (a == "2"):
    a = luasLingkaran()
    return "2\n" + a + "\n" + a 
  elif (a == "3"):
    a = luasPersegi()
    return "3\n" + a + "\n" + a
  else:
    print("Masukan anda tidak valid \n")
    return "0"

def luasSegitiga():
  print('''
         /|\ 
        / | \ 
       /  |  \ 
      /   |   \ 
     /ting|gi  \ 
    /_____|_____\ 
        alas ''')
  a = input("Masukan nilai alas   : ")
  print("")
  b = input("Masukan nilai tinggi : ")
  print("")
  return a, b
  
def kelilingSegitiga():
  print('''
          /|\ 
         / | \ 
        /  |  \ 
 sisiB /   |   \ sisiA
      /    |    \ 
     /_____|_____\ 
         sisiC ''')
  a = input("Masukan nilai sisiA : ")
  print("")
  b = input("Masukan nilai sisiB : ")
  print("")
  c = input("Masukan nilai sisiC : ")
  print("")
  return a, b, c

def luasLingkaran():
  print('''
        ___ 
       /   \ 
      /     \ 
     |   ----| jari-jari
      \     / 
       \___/ ''')
  a = input("Masukan nilai jari-jari : ")
  print("")
  return a

def luasPersegi():
  print('''
     ________ 
    |        | 
    |        |sisi 
    |        | 
    |________| 
        sisi''')
  a = input("Masukan nilai sisi : ")
  print("")
  return a
