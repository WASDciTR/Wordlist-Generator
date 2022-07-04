import itertools as t
import time
print("                   )     )   ")
print(" (              ( /(  ( /(   ")
print(" )\ )    (   (  )\()) )\())  ")
print("(()/(    )\  )\((_)\ ((_)\   ")
print(" /(_))_ ((_)((_)_((_)  ((_)  ")
print("(_)) __|\ \ / /| \| | / _ \  ")
print("  | (_ | \ V / | .` || (_) | ")
print("   \___|  \_/  |_|\_| \___/  ")
print("                            Coded By")
print("\n")
print("\n")
time.sleep(1)
chars = input("İstenilen Karakter :")
min = int(input("En Az Karakter :"))
max = int(input("En Fazla Karakter :"))
output = input("Kaydedilecek Dosya İsmi :")

if output == "" or output is None:
    file = open(chars+".txt",'w')
else:
    file = open(output,'w')
if min == max:
    for i in range(min, max + 1):
        for a in t.product(chars, repeat= i):
            s = "".join(a)
            file.write(s+"\n")
        file.close()

elif min < max:
    for i in range(min, max + 1):
        for a in t.product(chars, repeat= i):
            s = "".join(a)
            file.write(s+"\n")
        file.close()
else:
    print("Maksimum tekrar, minimum tekrardan büyük olmalıdır")
    exit
if output == "" or output is None:
    print("Dosyayı adına göre kaydedildi :"+chars+".txt")
else:
    print("Dosyayı adına göre kaydedildi :"+output)
