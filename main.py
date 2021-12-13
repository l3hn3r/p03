#Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!

másik = int(input('kérek egy számot'))
egyik = int(input('kérek egy más számot'))
if egyik > másik:
  print(egyik,'ez a nagyobb')
else:
  print(másik,'ez a nagyobb')